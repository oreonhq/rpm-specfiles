%global source0_hash 1492dfef8dd6c3036446ac3b340005d92ab92f7d48ee3271b5dac1d36945d3d9

Name:           jpegxl
Version:        0.11.1
Release:        9%{?dist}
Summary:        JPEG XL reference encoder and decoder (libjxl)
License:        BSD-3-Clause
URL:            https://github.com/libjxl/libjxl
Source0:        https://github.com/libjxl/libjxl/archive/v%{version}/%{name}-%{version}.tar.gz#/jpegxl-0.11.1.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  brotli-devel
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  highway-devel
BuildRequires:  lcms2-devel

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
%autosetup -n libjxl-%{version} -p1


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


%files -n libjxl
%{_libdir}/libjxl.so.*
%{_libdir}/libjxl_threads.so.*
%{_libdir}/libjxl_cms.so.*

%files -n libjxl-devel
%{_includedir}/jxl
%{_libdir}/libjxl.so
%{_libdir}/libjxl_threads.so
%{_libdir}/libjxl_cms.so
%{_libdir}/pkgconfig/libjxl.pc
%{_libdir}/pkgconfig/libjxl_cms.pc
%{_libdir}/pkgconfig/libjxl_threads.pc

%files -n libjxl-static
%{_libdir}/libjxl_extras_codec.a

%files -n libjxl-tools
%{_bindir}/cjxl
%{_bindir}/djxl
%{_bindir}/jxlinfo
%{_bindir}/benchmark_xl

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.1-2
- Add JPEG XL (libjxl) stack
