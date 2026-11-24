# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 03ad231ad1f9d64b52474392d63c31197b0bc7bd416e58b1c10a329a5ed89caf
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libao
Version:        1.2.0
Release:        1%{?dist}
Summary:        Cross Platform Audio Output Library
License:        GPL-2.0-or-later
URL:            http://xiph.org/ao/
Source0:        http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
Patch1:         0001-ao_pulse.c-fix-latency-calculation.patch
Patch2:         d5221655dfd1a2156aa6be83b5aadea7c1e0f5bd.diff
Patch3:         libao-nanosleep.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires: make

%description
Libao is a cross-platform audio library that allows programs to output audio
using a simple API on a wide variety of platforms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
sed -i "s/-O20 -ffast-math//" configure

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*

%ldconfig_scriptlets

%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/libao.so.*
%{_libdir}/ao
%{_mandir}/man5/*

%files devel
%doc doc/*.html doc/*.c doc/*.css
%{_includedir}/ao
%{_libdir}/ckport
%{_libdir}/libao.so
%{_libdir}/pkgconfig/ao.pc
%{_datadir}/aclocal/ao.m4

%changelog
%autochangelog
