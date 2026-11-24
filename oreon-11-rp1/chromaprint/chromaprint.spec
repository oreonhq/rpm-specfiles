# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d54ada62c16b2db396d3251ec54fc7a58909c163131a1cfcf7fa6407dbc14360
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_with bootstrap

%if 0%{?rhel} && 0%{?rhel} < 9
%bcond_with ffmpeg
%else
%bcond ffmpeg %{?_with_bootstrap:0}%{!?_with_bootstrap:1}
%endif
%global sover 1

Name:           chromaprint
Version:        1.6.2
Release:        1%{?dist}
Summary:        Library implementing the AcoustID fingerprinting

License:        GPL-2.0-or-later
URL:            http://www.acoustid.org/chromaprint
Source0:        https://github.com/acoustid/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3
BuildRequires:  ninja-build

%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+

%package -n libchromaprint
Summary:        Library implementing the AcoustID fingerprinting
Obsoletes:      python-chromaprint < 0.6-3

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+

%package -n libchromaprint-devel
Summary:        Headers for developing programs that will use %{name}
Requires:       libchromaprint%{?_isa} = %{version}-%{release}

%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%if %{with ffmpeg}
%package tools
Summary:        Chromaprint audio fingerprinting tools
BuildRequires:  ffmpeg-free-devel
Requires:       libchromaprint%{?_isa} = %{version}-%{release}

%description tools
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

This is a set of Chromaprint tools related to acoustic fingerprinting
featuring fpcalc an standalone AcoustID tool used by Picard.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+
%endif

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TESTS=ON \
        -DBUILD_TOOLS=%{?with_ffmpeg:ON}%{!?with_ffmpeg:OFF}

%cmake_build

%install
%cmake_install

rm  -f %{buildroot}%{_libdir}/lib*.la

%check
%ctest

%files -n libchromaprint
%doc NEWS.txt README.md
%license LICENSE.md
%{_libdir}/lib*.so.%{sover}*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/Chromaprint/
%{_libdir}/cmake/Chromaprint/*.cmake

%if %{with ffmpeg}
%files tools
%{_bindir}/fpcalc
%endif

%changelog
%autochangelog
