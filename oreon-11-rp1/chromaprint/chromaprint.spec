%global source0_hash 3368805af0ee47b9df74df10b5001a44569e01df2844dab520031720dde9ad23
%bcond_with bootstrap
%bcond ffmpeg %{?_with_bootstrap:0}%{!?_with_bootstrap:1}
%global sover 1
Name:           chromaprint
Version:        1.6.1
Release:        1%{?dist}
Summary:        Library implementing the AcoustID fingerprinting
License:        GPL-2.0-or-later
URL:            http://www.acoustid.org/chromaprint
Source0:        https://github.com/acoustid/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TESTS=ON \
        -DBUILD_TOOLS=%{?with_ffmpeg:ON}%{!?with_ffmpeg:OFF}
%cmake_build
%install
%cmake_install
rm  -f %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles libchromaprint usr/*/lib*.so.*
%oreon_autofiles libchromaprint-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles chromaprint-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libchromaprint -f %{oreon_filedir}/libchromaprint.list
%files -n libchromaprint-devel -f %{oreon_filedir}/libchromaprint-devel.list
%files -n chromaprint-tools -f %{oreon_filedir}/chromaprint-tools.list

%changelog

%autochangelog
