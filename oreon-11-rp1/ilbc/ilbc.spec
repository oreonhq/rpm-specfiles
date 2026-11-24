# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c5ec9e3ec53a0a913f81504e202c7bfefbe9c070b7f5599c5e13a6c75d6af913
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:       ilbc
Summary:    Internet Low Bitrate Codec
Version:    3.0.4
Release:    1%{?dist}
License:    BSD-3-Clause
URL:        https://github.com/TimothyGu/libilbc

Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     %{name}-flags.patch
Patch1:     %{name}-s390.patch
Patch2:     %{name}-loongarch.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%package    devel
Summary:    development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Additional header files for development with %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n libilbc-%{version}
sed -r -i 's/(set\(CMAKE_CXX_STANDARD[[:blank:]]+)14\b/\117/' CMakeLists.txt

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

rm -fr %{buildroot}%{_docdir}/libilbc

%files
%doc README.md NEWS.md
%license COPYING
%{_libdir}/lib%{name}.so.3
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_bindir}/%{name}_test
%{_includedir}/%{name}.h
%{_includedir}/%{name}_export.h
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
