%global source0_hash bab458278f4bee2b5b59b7df5cff51a52ad71bb74b551151c9587f63d86d01b8
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%undefine _auto_set_build_flags
Name:    pesign
Summary:        Signing utility for UEFI binaries
Version: 117
Release:        1%{?dist}
License: GPL-2.0-only
URL:     https://github.com/rhboot/pesign
Obsoletes: pesign-rh-test-certs <= 0.111-7
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
%endif
Requires:      nspr
Requires:      nss
Requires:      nss-tools >= 3.53
Requires:      nss-util
Requires:      popt
Requires:      rpm
ExclusiveArch: %{ix86} x86_64 ia64 aarch64 %{arm} riscv64
Source0:        https://github.com/rhboot/pesign/archive/refs/tags/%{version}.tar.gz#/pesign-%{version}.tar.bz2
Source1:        certs.tar.xz
Source2:        pesign.py
Patch0003:        0003-Work-around-OpenSC-changing-token-names-on-fedora-bu.patch
# oreon:deps
BuildRequires:  efivar-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  mandoc
BuildRequires:  nspr
BuildRequires:  nspr-devel
BuildRequires:  nss
BuildRequires:  nss-devel
BuildRequires:  nss-tools
BuildRequires:  nss-util
BuildRequires:  popt-devel
BuildRequires:  python3
BuildRequires:  python3-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  tar
BuildRequires:  xz
# /oreon:deps
%description
This package contains the pesign utility for signing UEFI binaries as
well as other associated tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
cp -av libdpe/*.[ch] src/
install -d -m 0755 %{buildroot}%{python3_sitelib}/mockbuild/plugins/
install -m 0755 %{SOURCE2} %{buildroot}%{python3_sitelib}/mockbuild/plugins/
install -m0644 -D pesign.sysusers.conf %{buildroot}%{_sysusersdir}/pesign.conf
%oreon_autofiles main
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
%post

%systemd_post pesign.service
%preun

%systemd_preun pesign.service
%postun

%systemd_postun_with_restart pesign.service
%posttrans

certutil -d %{_sysconfdir}/pki/pesign/ -X -L > /dev/null
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
