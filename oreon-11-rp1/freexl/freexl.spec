# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 176705f1de58ab7c1eebbf5c6de46ab76fcd8b856508dbd28f5648f7c6e1a7f0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond autoreconf 1

%if 0%{?oreon}
%bcond mingw 0
%else
%bcond mingw %{undefined el10}
%endif

Name:           freexl
Version:        2.0.0
%global so_version 1
Release:        %{autorelease}
Summary:        Library to extract data from within an Excel spreadsheet

License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://www.gaia-gis.it/fossil/freexl/index
Source0:        https://www.gaia-gis.it/gaia-sins/freexl-%{version}.tar.gz

Patch:          freexl-2.0.0-iconv-mingw32.patch

%if %{with autoreconf}
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  expat-devel
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel

BuildRequires:  doxygen

%if %{with mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-libcharset
BuildRequires:  mingw32-minizip
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-libcharset
BuildRequires:  mingw64-minizip
BuildRequires:  mingw64-win-iconv
%endif

%description
FreeXL is a library to extract valid data from within spreadsheets.

Design goals:
  • to be simple and lightweight
  • to be stable, robust and efficient
  • to be easily and universally portable
  • completely ignoring any GUI-related oddity

%package doc
Summary:        Documentation and examples for FreeXL

License:        %{license} AND MIT

BuildArch:      noarch

%{?doxygen_js_requires}

%description doc
%{summary}.

%package devel
Summary:  Development Libraries for FreeXL
Requires: freexl%{?_isa} = %{version}-%{release}

%description devel
The freexl-devel package contains libraries and header files for
developing applications that use freexl.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows freexl library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows freexl library.

%package -n mingw64-%{name}
Summary:       MinGW Windows freexl library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows freexl library.

%{?mingw_debug_package}
%endif

%prep
%oreon_sha256
%autosetup -p1

mkdir --parents clean
cp --recursive --preserve examples clean/
rm --verbose clean/examples/Makefile.*

mkdir build_native
cp --archive tests build_native

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

pushd build_native
%global _configure ../configure
%configure --disable-static
popd

%if %{with mingw}
%mingw_configure --disable-static
%endif

%build
pushd build_native
%make_build

doxygen Doxyfile
%{doxygen_unbundle html}
popd

%if %{with mingw}
%mingw_make_build
%endif

%install
%make_install --directory=build_native

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif

%check
%make_build --directory=build_native check

%files
%license COPYING
%{_libdir}/libfreexl.so.%{so_version}{,.*}

%files devel
%{_includedir}/freexl.h
%{_libdir}/libfreexl.so
%{_libdir}/pkgconfig/freexl.pc

%files doc
%license COPYING
%doc AUTHORS
%doc README
%doc clean/examples/
%doc build_native/html/

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libfreexl-1.dll
%{mingw32_includedir}/freexl.h
%{mingw32_libdir}/libfreexl.dll.a
%{mingw32_libdir}/pkgconfig/freexl.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libfreexl-1.dll
%{mingw64_includedir}/freexl.h
%{mingw64_libdir}/libfreexl.dll.a
%{mingw64_libdir}/pkgconfig/freexl.pc
%endif

%changelog
%autochangelog
