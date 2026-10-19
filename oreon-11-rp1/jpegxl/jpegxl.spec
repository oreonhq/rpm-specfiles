%global source0_hash 03e9be69a30be4011f559da75328b6d7cea8ad921fabfbd551ce10bf45cdc992
Name:           jpegxl
Version:        0.12.0
Release:        1%{?dist}
Summary:        JPEG XL reference encoder and decoder (libjxl)
License:        BSD-3-Clause
URL:            https://github.com/libjxl/libjxl
Source0:        https://github.com/libjxl/libjxl/archive/v%{version}/%{name}-%{version}.tar.gz#/jpegxl-%{version}.tar.gz
# oreon:deps
BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  highway-devel
BuildRequires:  lcms2-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
JPEG XL shared libraries (binary packages include libjxl).

%package -n libjxl
Summary:        JPEG XL shared library
%description -n libjxl
Runtime library for JPEG XL.

%package -n libjxl-devel
Summary:        Development files for libjxl
Requires:       libjxl%{?_isa} = %{version}-%{release}
%description -n libjxl-devel
Headers and pkg-config files for libjxl (this release does not ship CMake package config).

%package -n libjxl-static
Summary:        Static libraries for libjxl
Requires:       libjxl-devel%{?_isa} = %{version}-%{release}
%description -n libjxl-static
Static libjxl_extras_codec archive for builds that link the codec helpers without shared libjxl extras.

%package -n libjxl-tools
Summary:        Command-line tools for JPEG XL
Requires:       libjxl%{?_isa} = %{version}-%{release}
%description -n libjxl-tools
cjxl, djxl, jxlinfo, and benchmark_xl from libjxl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libjxl-%{version}
%oreon_prep
%build

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF \
  -DJPEGXL_ENABLE_SKCMS=OFF \
  -DJPEGXL_ENABLE_PLUGINS=OFF \
  -DJPEGXL_ENABLE_DEVTOOLS=OFF \
  -DJPEGXL_ENABLE_SJPEG=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles libjxl usr/*/lib*.so.*
%oreon_autofiles libjxl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libjxl-static usr/*/lib*.so.*
%oreon_autofiles libjxl-tools usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libjxl -f %{oreon_filedir}/libjxl.list
%files -n libjxl-devel -f %{oreon_filedir}/libjxl-devel.list
%files -n libjxl-static -f %{oreon_filedir}/libjxl-static.list
%files -n libjxl-tools -f %{oreon_filedir}/libjxl-tools.list

%changelog

%autochangelog
