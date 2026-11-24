# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 882901ea485c35c26222b72a42972aeeb8cef9212fb7e3306fe276a819f7ce32
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%undefine _auto_set_build_flags

Name:    pesign
Summary: Signing utility for UEFI binaries
Version: 117
Release: 1%{?dist}
License: GPL-2.0-only
URL:     https://github.com/rhboot/pesign

Obsoletes: pesign-rh-test-certs <= 0.111-7
BuildRequires: oreon-rpm-macros
BuildRequires: efivar-devel >= 38-1
BuildRequires: clang
BuildRequires: llvm
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
BuildRequires: systemd-rpm-macros
Requires:      nspr
Requires:      nss
Requires:      nss-tools >= 3.53
Requires:      nss-util
Requires:      popt
Requires:      rpm
ExclusiveArch: %{ix86} x86_64 ia64 aarch64 %{arm} riscv64

Source0: https://github.com/rhboot/pesign/releases/download/%{version}/pesign-%{version}.tar.bz2
Source1: certs.tar.xz
Source2: pesign.py

Patch0001: 0001-Work-around-OpenSC-changing-token-names-on-fedora-bu.patch

%description
This package contains the pesign utility for signing UEFI binaries as
well as other associated tools.

%prep
%oreon_sha256
%setup -q -T -b 0
%setup -q -T -D -c -n pesign-%{version}/ -a 1
git init
git config user.email "packaging@oreonhq.com"
git config user.name "Oreon Packaging"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null
git config --unset user.email
git config --unset user.name

cat >pesign.sysusers.conf <<EOF
u pesign - 'Group for the pesign signing daemon' /run/pesign -
EOF

%build
make CC=%{__cc} PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
mkdir -p %{buildroot}/%{_libdir}
make CC=%{__cc} PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} \
	install
make CC=%{__cc} PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} \
	install_systemd

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

%post
%systemd_post pesign.service

%preun
%systemd_preun pesign.service

%postun
%systemd_postun_with_restart pesign.service

%posttrans
certutil -d %{_sysconfdir}/pki/pesign/ -X -L > /dev/null


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
%{_libexecdir}/pesign/pesign-rpmbuild-helper
%config(noreplace)/%{_sysconfdir}/pesign/users
%config(noreplace)/%{_sysconfdir}/pesign/groups
%{_sysconfdir}/popt.d/pesign.popt
%{macrosdir}/macros.pesign
%{_mandir}/man*/*
%dir %attr(0770, pesign, pesign) %{_rundir}/%{name}
%ghost %attr(0660, -, -) %{_rundir}/%{name}/socket
%ghost %attr(0660, -, -) %{_rundir}/%{name}/pesign.pid
%{_tmpfilesdir}/pesign.conf
%{_unitdir}/pesign.service
%{python3_sitelib}/mockbuild/plugins/*/pesign.*
%{python3_sitelib}/mockbuild/plugins/pesign.*
%{_sysusersdir}/pesign.conf

%changelog
%autochangelog
