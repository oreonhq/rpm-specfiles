# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash add272bb09e6384a4833ffca4896350fdb16e0ca22df68c0384773c67a175594
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine __cmake_in_source_build

Name:           woff2
Version:        1.0.2
Release:        1%{?dist}
Summary:        Web Open Font Format 2.0 library

License:        MIT
URL:            https://github.com/google/woff2
Source0:        https://github.com/google/woff2/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         covscan.patch
Patch1:         include-cstdint.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  brotli-devel >= 1.0

%description
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF 1.0 with
improved compression that is achieved by using the Brotli algorithm. The primary
purpose of the WOFF2 format is to efficiently package fonts linked to Web
documents by means of CSS @font-face rules.

%package        tools
Summary:        Web Open Font Format 2.0 tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Tools for compressing TTF files to WOFF2 format, decompressing WOFF2
files back to TTF files and dumping WOFF2 file information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files and utils for %{name}

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{version}
sed -i 's/VERSION 2.8.6/VERSION 3.5...4.0/g' CMakeLists.txt

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}" \
    -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_bindir}/

cd %{_vpath_builddir}
install -m 755 woff2_decompress %{buildroot}%{_bindir}/
install -m 755 woff2_compress %{buildroot}%{_bindir}/
install -m 755 woff2_info %{buildroot}%{_bindir}/
cd -

%files
%license LICENSE
%{_libdir}/libwoff2common.so.*
%{_libdir}/libwoff2dec.so.*
%{_libdir}/libwoff2enc.so.*

%files tools
%attr(755, root, root) %{_bindir}/woff2_compress
%attr(755, root, root) %{_bindir}/woff2_decompress
%attr(755, root, root) %{_bindir}/woff2_info

%files devel
%{_includedir}/woff2
%{_libdir}/libwoff2common.so
%{_libdir}/libwoff2dec.so
%{_libdir}/libwoff2enc.so
%{_libdir}/pkgconfig/libwoff2common.pc
%{_libdir}/pkgconfig/libwoff2dec.pc
%{_libdir}/pkgconfig/libwoff2enc.pc

%changelog
%autochangelog
