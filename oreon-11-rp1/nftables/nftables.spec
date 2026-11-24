# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 372931bda8556b310636a2f9020adc710f9bab66f47efe0ce90bff800ac2530c
%global source1_hash 291422e027502bd83a1e1e12653ea3f4725b8a06891956e2f72d0cde416d36af
%global source2_hash 961f5e8d3dcffab4c04c891a3f26e27bedf49301e53cbf83660001de3d9390c8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           nftables
Version:        1.1.6
Release:        %{autorelease}
Epoch:          1
Summary:        Netfilter Tables userspace utilities

License:        GPL-2.0-only
URL:            https://netfilter.org/projects/nftables/
Source0:        %{url}/files/%{name}-%{version}.tar.xz
Source1:        %{url}/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
Source3:        nftables.service
Source4:        nftables.conf
Source5:        main.nft
Source6:        router.nft
Source7:        nat.nft

Patch01: 0001-build-fix-.-configure-with-non-bash-shell.patch
Patch02: 0002-doc-fix-typo-in-man-page.patch

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: clang
BuildRequires: gcc
BuildRequires: flex
BuildRequires: bison
BuildRequires: pkgconfig(libmnl) >= 1.0.4
BuildRequires: gmp-devel
BuildRequires: pkgconfig(libnftnl) >= 1.3.1
BuildRequires: systemd
BuildRequires: asciidoc
BuildRequires: pkgconfig(xtables) >= 1.6.1
BuildRequires: jansson-devel
BuildRequires: python3-devel
BuildRequires: readline-devel
BuildRequires: libedit-devel
BuildRequires: python3-setuptools
BuildRequires: gnupg2

Requires:	%{name}-services = %{epoch}:%{version}-%{release}

%generate_buildrequires
cd py/
%pyproject_buildrequires

%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
Headers, man pages and other development files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-nftables}
BuildArch:	noarch

%description -n python3-nftables
The nftables python module provides an interface to libnftables via ctypes.

%package	services
Summary:	Systemd service for nftables
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description	services
Manage an nftables-based firewall defined by ruleset snippets in /etc/nftables
and /etc/sysconfig/nftables.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -fi
%configure --disable-silent-rules --with-xtables --with-json
%make_build
cd py/
%pyproject_wheel

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -f $RPM_BUILD_ROOT/%{_libdir}/libnftables.a

rm -f $RPM_BUILD_ROOT/%{_datadir}/nftables/*.nft

chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man8/nft*

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp -a %{SOURCE3} $RPM_BUILD_ROOT/%{_unitdir}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
cp -a %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/

cp %{SOURCE5} %{SOURCE6} %{SOURCE7} \
	$RPM_BUILD_ROOT/%{_sysconfdir}/nftables/

find $RPM_BUILD_ROOT/%{_sysconfdir} \
	\( -type d -exec chmod 0700 {} \; \) , \
	\( -type f -exec chmod 0600 {} \; \)

cd py/
%pyproject_install
%pyproject_save_files nftables

%post services
if [ $1 -eq 1 ] && [[ ! -h /etc/systemd/system/multi-user.target.wants/nftables.service ]]; then
  %systemd_post nftables.service
fi

%preun services
%systemd_preun nftables.service

%postun services
%systemd_postun_with_restart nftables.service

%files
%license COPYING
%{_sbindir}/nft
%{_libdir}/libnftables.so.*
%{_mandir}/man5/libnftables-json.5*
%{_mandir}/man8/nft*
%{_docdir}/nftables/

%files devel
%{_libdir}/libnftables.so
%{_libdir}/pkgconfig/libnftables.pc
%{_includedir}/nftables/libnftables.h
%{_mandir}/man3/libnftables.3*

%files -n python3-nftables -f %{pyproject_files}

%files services
%config(noreplace) %{_sysconfdir}/nftables/
%config(noreplace) %{_sysconfdir}/sysconfig/nftables.conf
%{_unitdir}/nftables.service

%changelog
%autochangelog
