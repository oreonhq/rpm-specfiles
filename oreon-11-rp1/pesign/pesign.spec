%global source0_hash 35331f75689863e5be595f2bb04a8bc934ce734b8d76fa5d6aeb4d85424e8996
%global source1_hash fd6cf1da31f5e7a1ddc91799d3bfd174f7c8612468bffe58b37d1bed1c12d71f

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# No.  I have enough trouble already.
%undefine _auto_set_build_flags

Name:    pesign
Summary: Signing utility for UEFI binaries
Version: 116
Release: 8%{?dist}
License: GPL-2.0-only
URL:     https://github.com/rhboot/pesign

Obsoletes: pesign-rh-test-certs <= 0.111-7
BuildRequires: efivar-devel >= 38-1
BuildRequires: gcc
BuildRequires: git
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: mandoc
BuildRequires: nspr
BuildRequires: nspr-devel >= 4.9.2-1
BuildRequires: nss
BuildRequires: nss-devel >= 3.13.6-1
BuildRequires: nss-tools
BuildRequires: nss-util
BuildRequires: popt-devel
BuildRequires: python3
BuildRequires: python3-rpm-macros
BuildRequires: tar
BuildRequires: xz
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
BuildRequires: systemd-rpm-macros
%endif
Requires:      nspr
Requires:      nss
Requires:      nss-tools >= 3.53
Requires:      nss-util
Requires:      popt
Requires:      rpm
ExclusiveArch: %{ix86} x86_64 ia64 aarch64 %{arm} riscv64
%if 0%{?rhel} == 7 || (0%{?oreon} >= 11)
BuildRequires: rh-signing-tools >= 1.20-2
%endif

Source0:        https://github.com/rhboot/pesign/releases/download/%{version}/pesign-%{version}.tar.bz2
Source1: certs.tar.xz
Source2: pesign.py
Source3: pesign.patches

# generate with tool
%include %{SOURCE3}

%description
This package contains the pesign utility for signing UEFI binaries as
well as other associated tools.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%setup -q -T -b 0
%setup -q -T -D -c -n pesign-%{version}/ -a 1
git init
git config user.email "pesign-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null
git config --unset user.email
git config --unset user.name

# Create a sysusers.d config file
cat >pesign.sysusers.conf <<EOF
u pesign - 'Group for the pesign signing daemon' /run/pesign -
EOF

%build
make PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
mkdir -p %{buildroot}/%{_libdir}
make PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} \
	install
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
make PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} \
	install_systemd
%endif

# there's some stuff that's not really meant to be shipped yet
rm -rf %{buildroot}/boot %{buildroot}/usr/include
rm -rf %{buildroot}%{_libdir}/libdpe*
mkdir -p %{buildroot}%{_sysconfdir}/pki/pesign/
mkdir -p %{buildroot}%{_sysconfdir}/pki/pesign-rh-test/
cp -a etc/pki/pesign/* %{buildroot}%{_sysconfdir}/pki/pesign/
cp -a etc/pki/pesign-rh-test/* %{buildroot}%{_sysconfdir}/pki/pesign-rh-test/

if [ %{macrosdir} != %{_sysconfdir}/rpm ]; then
	mkdir -p %{buildroot}%{macrosdir}
	mv %{buildroot}%{_sysconfdir}/rpm/macros.pesign \
		%{buildroot}%{macrosdir}
	rmdir %{buildroot}%{_sysconfdir}/rpm
fi
rm -vf %{buildroot}/usr/share/doc/pesign-%{version}/COPYING

# and find-debuginfo.sh has some pretty awful deficencies too...
cp -av libdpe/*.[ch] src/

install -d -m 0755 %{buildroot}%{python3_sitelib}/mockbuild/plugins/
install -m 0755 %{SOURCE2} %{buildroot}%{python3_sitelib}/mockbuild/plugins/

install -m0644 -D pesign.sysusers.conf %{buildroot}%{_sysusersdir}/pesign.conf


%if 0%{?rhel} >= 7 || 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
%post
%systemd_post pesign.service

%preun
%systemd_preun pesign.service

%postun
%systemd_postun_with_restart pesign.service

%posttrans
certutil -d %{_sysconfdir}/pki/pesign/ -X -L > /dev/null

# this is disabled currently because it breaks the fedora kernel build root
# generation - because we don't currently have a good way of populating
# /etc/pesign/{users,groups} before the buildroot is installed, or
# populating them and re-running pesign-authorize afterwards but before the
# package build of e.g. kernel
#%%{_libexecdir}/pesign/pesign-authorize
%endif

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md TODO
%{_bindir}/authvar
%{_bindir}/efikeygen
%{_bindir}/pesigcheck
%{_bindir}/pesign
%{_bindir}/pesign-client
%{_bindir}/pesum
%dir %{_libexecdir}/pesign/
%dir %attr(0770,pesign,pesign) %{_sysconfdir}/pki/pesign/
%config(noreplace) %attr(0660,pesign,pesign) %{_sysconfdir}/pki/pesign/*
%dir %attr(0775,pesign,pesign) %{_sysconfdir}/pki/pesign-rh-test/
%config(noreplace) %attr(0664,pesign,pesign) %{_sysconfdir}/pki/pesign-rh-test/*
%{_libexecdir}/pesign/pesign-authorize
%{_libexecdir}/pesign/pesign-rpmbuild-helper
%config(noreplace)/%{_sysconfdir}/pesign/users
%config(noreplace)/%{_sysconfdir}/pesign/groups
%{_sysconfdir}/popt.d/pesign.popt
%{macrosdir}/macros.pesign
%{_mandir}/man*/*
%dir %attr(0770, pesign, pesign) %{_rundir}/%{name}
%ghost %attr(0660, -, -) %{_rundir}/%{name}/socket
%ghost %attr(0660, -, -) %{_rundir}/%{name}/pesign.pid
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
%{_tmpfilesdir}/pesign.conf
%{_unitdir}/pesign.service
%endif
%{python3_sitelib}/mockbuild/plugins/*/pesign.*
%{python3_sitelib}/mockbuild/plugins/pesign.*
%{_sysusersdir}/pesign.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 116-8
- Import
