Name:           jpegxl
Version:        0.11.1
Release:        8%{?dist}
Summary:        JPEG XL reference encoder and decoder (libjxl)
License:        BSD-3-Clause
URL:            https://github.com/libjxl/libjxl
Source0:        %{url}/archive/v%{version}/libjxl-%{version}.tar.gz

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


%package -n libjxl-tools
Summary:        Command-line tools for JPEG XL
Requires:       libjxl%{?_isa} = %{version}-%{release}

%description -n libjxl-tools
cjxl, djxl, jxlinfo, and benchmark_xl from libjxl.


%prep
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

%files -n libjxl-tools
%{_bindir}/cjxl
%{_bindir}/djxl
%{_bindir}/jxlinfo
%{_bindir}/benchmark_xl

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.1-2
- Add JPEG XL (libjxl) stack
