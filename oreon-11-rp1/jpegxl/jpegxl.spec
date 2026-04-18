Name:           jpegxl
Version:        0.11.1
Release:        5%{?dist}
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
Headers and CMake files for libjxl.


%prep
%autosetup -n libjxl-%{version} -p1


%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF \
  -DJPEGXL_ENABLE_SKCMS=OFF \
  -DJPEGXL_ENABLE_PLUGINS=OFF \
  -DJPEGXL_ENABLE_DEVTOOLS=OFF
%cmake_build


%install
%cmake_install


%files -n libjxl
%{_libdir}/libjxl.so.*
%{_libdir}/libjxl_threads.so.*

%files -n libjxl-devel
%{_includedir}/jxl
%{_libdir}/libjxl.so
%{_libdir}/libjxl_threads.so
%{_libdir}/cmake/libjxl
%{_libdir}/pkgconfig/libjxl.pc

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.1-2
- Add JPEG XL (libjxl) stack
