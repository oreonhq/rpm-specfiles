# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 29c4a53481591faf2f30086a16a58cadd8a963d540c0b0f10ec464a99003d93c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: systemtap
Version: 5.6
Release: 1%{?dist}
Summary: Instrumentation system
License: GPL-2.0-or-later
URL: https://sourceware.org/systemtap/
Source0: https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz
Patch0: stapbpf-warnings.patch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: elfutils-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-wheel
BuildRequires: python3-pyparsing
BuildRequires: pkgconfig(json-c)
BuildRequires: sqlite-devel
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(ncurses)
BuildRequires: readline-devel
BuildRequires: rpm-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libuuid-devel
BuildRequires: gettext-devel
BuildRequires: cpio
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libdebuginfod)
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
Systemtap instrumentation system.

%package sdt-devel
Summary: Static probe header for systemtap
Requires: systemtap-sdt-dtrace = %{version}-%{release}

%description sdt-devel
The sys/sdt.h header used by userspace static probes.

%package sdt-dtrace
Summary: dtrace compatible wrapper for systemtap
Requires: systemtap-sdt-devel = %{version}-%{release}
Requires: python3-pyparsing

%description sdt-dtrace
The dtrace command systemtap ships for static probe generation.

%prep
%oreon_sha256
%autosetup -n systemtap-%{version} -p1

%build
%configure
%make_build

%install
%make_install
%oreon_filelist
grep -E '/sys/sdt\.h$|/sys/sdt-config\.h$' %{_builddir}/%{name}.files > %{_builddir}/%{name}-sdt-devel.files
grep -E '/bin/dtrace$' %{_builddir}/%{name}.files > %{_builddir}/%{name}-sdt-dtrace.files
grep -vxFf %{_builddir}/%{name}-sdt-devel.files %{_builddir}/%{name}.files | grep -vxFf %{_builddir}/%{name}-sdt-dtrace.files > %{_builddir}/%{name}.main
mv %{_builddir}/%{name}.main %{_builddir}/%{name}.files

%check
./stap -V

%files -f %{_builddir}/%{name}.files
%files sdt-devel -f %{_builddir}/%{name}-sdt-devel.files
%files sdt-dtrace -f %{_builddir}/%{name}-sdt-dtrace.files
