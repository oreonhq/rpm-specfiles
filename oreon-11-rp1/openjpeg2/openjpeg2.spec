Name:           openjpeg2
Version:        2.5.3
Release:        4%{?dist}
Summary:        JPEG 2000 codec library
License:        BSD-2-Clause
URL:            https://www.openjpeg.org/
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}/openjpeg-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  ninja-build
BuildRequires:  zlib-devel

%description
OpenJPEG is an open-source JPEG 2000 codec released under the BSD license.


%package        libs
Summary:        OpenJPEG runtime libraries

%description    libs
Shared libraries for JPEG 2000.

%package        devel
Summary:        Development files for OpenJPEG
Requires:       openjpeg2-libs%{?_isa} = %{version}-%{release}

%description    devel
Headers and CMake files for OpenJPEG 2.x.


%prep
%autosetup -n openjpeg-%{version} -p1


%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF
%cmake_build


%install
%cmake_install


%files
%{_bindir}/opj_*

%files libs
# 2.5.x uses SOVERSION 7 (see upstream CMake version table)
%{_libdir}/libopenjp2.so.7*

%files devel
%{_includedir}/openjpeg-2.5/
%{_libdir}/libopenjp2.so
%{_libdir}/cmake/openjpeg-2.5/
%{_libdir}/pkgconfig/libopenjp2.pc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.3-2
- Add OpenJPEG2 for PDF and imaging stacks
