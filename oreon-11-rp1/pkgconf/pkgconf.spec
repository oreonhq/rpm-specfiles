# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9371b2f6372da574d4c6dc96fe9b1463037bcf6afcb6671c1555afde7b17e2de
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: pkgconf
Version: 3.0.10
Release: 5%{?dist}
Summary: compiler and linker flags for development libraries
License: ISC
URL: https://gitea.treehouse.systems/ariadne/pkgconf
Source0: https://distfiles.ariadne.space/pkgconf/pkgconf-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

Requires: libpkgconf%{?_isa} = %{version}-%{release}

%description
pkgconf is a program which helps to configure compiler and linker flags for development libraries. It provides pkg-config compatible behavior.

%package pkg-config
Summary: pkg-config compatibility links for pkgconf
Requires: pkgconf%{?_isa} = %{version}-%{release}
Requires: pkgconf-m4 = %{version}-%{release}
Provides: pkg-config = %{version}-%{release}
Provides: pkg-config%{?_isa} = %{version}-%{release}
Provides: pkgconfig = 1:%{version}-%{release}
Provides: pkgconfig%{?_isa} = 1:%{version}-%{release}
Provides: pkgconfig(pkg-config) = %{version}

%description pkg-config
The pkg-config command and target-prefixed pkg-config links provided by pkgconf.

%package m4
Summary: autoconf macros for pkgconf
BuildArch: noarch

%description m4
The pkg.m4 autoconf macros for PKG_CHECK_MODULES and related checks.

%package -n libpkgconf
Summary: pkgconf library

%description -n libpkgconf
libpkgconf is a library which provides access to most of pkgconf's functionality, to allow other tooling such as compilers and IDEs to discover and use libraries configured by pkgconf.

%package -n libpkgconf-devel
Summary: Development files for libpkgconf
Requires: libpkgconf%{?_isa} = %{version}-%{release}
Obsoletes: pkgconf-devel < 3.0.10-3

%description -n libpkgconf-devel
Headers and pkg-config file for libpkgconf.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --with-system-libdir=%{_libdir} --with-system-includedir=%{_includedir} --with-pkg-config-dir=%{_libdir}/pkgconfig:%{_datadir}/pkgconfig
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
ln -sf pkgconf %{buildroot}%{_bindir}/pkg-config
ln -sf pkgconf %{buildroot}%{_bindir}/%{_target_platform}-pkg-config

mkdir -p %{buildroot}%{_datadir}/pkgconfig
rm -rf %{buildroot}%{_docdir}/pkgconf

%ldconfig_scriptlets -n libpkgconf

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/pkgconf
%{_bindir}/bomtool
%{_bindir}/pccritic
%{_bindir}/spdxtool
%dir %{_datadir}/pkgconfig
%{_mandir}/man1/pkgconf.1*
%{_mandir}/man1/bomtool.1*
%{_mandir}/man1/pccritic.1*
%{_mandir}/man1/spdxtool.1*
%{_mandir}/man5/pc.5*
%{_mandir}/man5/pkgconf-personality.5*

%files pkg-config
%{_bindir}/pkg-config
%{_bindir}/%{_target_platform}-pkg-config

%files m4
%{_datadir}/aclocal/pkg.m4
%{_mandir}/man7/pkg.m4.7*

%files -n libpkgconf
%license COPYING
%{_libdir}/libpkgconf.so.8
%{_libdir}/libpkgconf.so.8.*

%files -n libpkgconf-devel
%{_includedir}/pkgconf/
%{_libdir}/libpkgconf.so
%{_libdir}/pkgconfig/libpkgconf.pc
