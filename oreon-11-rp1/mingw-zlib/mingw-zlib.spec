# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d7a0654783a4da529d1bb793b7ad9c3318020af77667bcae35f95d0e42a792f3

%{?mingw_package_header}

Name: mingw-zlib
Version: 1.3.2
Release: 1%{?dist}
Summary: MinGW Windows zlib compression library
License: Zlib
URL: https://www.zlib.net/
Source0: https://github.com/madler/zlib/releases/download/v%{version}/zlib-%{version}.tar.xz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: mingw32-binutils
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc

%description
Cross-compiled zlib compression libraries for Windows.

%package -n mingw32-zlib
Summary: MinGW Windows 32-bit zlib compression library

%description -n mingw32-zlib
Cross-compiled 32-bit zlib compression library for Windows.

%package -n mingw64-zlib
Summary: MinGW Windows 64-bit zlib compression library

%description -n mingw64-zlib
Cross-compiled 64-bit zlib compression library for Windows.

%{?mingw_debug_package}

%prep
%oreon_sha256
%autosetup -n zlib-%{version}

%build
%mingw_cmake \
  -G Ninja \
  -DZLIB_BUILD_STATIC=OFF \
  -DZLIB_BUILD_TESTING=ON
%mingw_ninja

%install
%mingw_ninja_install
%mingw_debug_install_post
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/doc/zlib
rm -rf %{buildroot}%{mingw64_datadir}/doc/zlib

%check
mingw32-objdump -p %{buildroot}%{mingw32_bindir}/zlib1.dll |
  grep -F zlibVersion
mingw64-objdump -p %{buildroot}%{mingw64_bindir}/zlib1.dll |
  grep -F zlibVersion

%files -n mingw32-zlib
%license LICENSE
%{mingw32_bindir}/zlib1.dll
%{mingw32_includedir}/zconf.h
%{mingw32_includedir}/zlib.h
%{mingw32_libdir}/libz.dll.a
%{mingw32_libdir}/cmake/zlib/
%{mingw32_libdir}/pkgconfig/zlib.pc

%files -n mingw64-zlib
%license LICENSE
%{mingw64_bindir}/zlib1.dll
%{mingw64_includedir}/zconf.h
%{mingw64_includedir}/zlib.h
%{mingw64_libdir}/libz.dll.a
%{mingw64_libdir}/cmake/zlib/
%{mingw64_libdir}/pkgconfig/zlib.pc

%changelog
%autochangelog
