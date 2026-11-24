# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cbccae52b2c2ecc5d2757e407da567eb681241ff8dadce39d779a7219dbcf449
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine __cmake_in_source_build

%bcond_with     bootstrap

Name:           codec2
Version:        1.2.0
Release:        1%{?dist}
Summary:        Next-Generation Digital Voice for Two-Way Radio
License:        LGPL-2.1-only

URL:            http://rowetel.com/codec2.html
Source0:        https://github.com/drowe67/codec2/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  libsamplerate-devel
%if %{without bootstrap}
BuildRequires:  lpcnetfreedv-devel
%endif
BuildRequires:  speex-devel
%if ! 0%{?rhel} < 8
BuildRequires:  speexdsp-devel
%endif

%description
Codec 2 is an open source (LGPL licensed) speech codec for 2400 bit/s
and below. This is the runtime library package.

%package devel
Summary:        Development files for Codec 2 
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Codec 2 is an open source (LGPL licensed) speech codec for 2400 bit/s
and below. This package contains the development files required to 
compile programs that use codec2.

%package devel-examples
Summary:        Example code for Codec 2
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description devel-examples
Example code for Codec 2

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{without bootstrap}
       -DLPCNET=ON
%endif

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/codec2.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=\${prefix}/include/%{name}
libdir=\${exec_prefix}/%{_lib}

Name: codec2
Description: Next-Generation Digital Voice for Two-Way Radio
Version: 1.2.0
Cflags: -I\${includedir}
Libs: -L\${libdir} -l%{name}
EOF

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
