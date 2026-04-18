%global sover 16

Name:           libavif
Version:        1.3.0
Release:        4%{?dist}
Summary:        Library for encoding and decoding AVIF images
License:        BSD-2-Clause
URL:            https://github.com/AOMediaCodec/libavif
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  nasm
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libyuv)
BuildRequires:  pkgconfig(zlib)

%description
libavif is a portable C implementation of the AV1 Image File Format.


%package        devel
Summary:        Development files for libavif
Requires:       libavif%{?_isa} = %{version}-%{release}

%description    devel
Headers, pkg-config, and CMake metadata for libavif.


%package        tools
Summary:        AVIF encoder and decoder command line tools

%description    tools
%{summary}.


%prep
%autosetup -p1


%build
%cmake \
  -GNinja \
  -DAVIF_CODEC_AOM=SYSTEM \
  -DAVIF_CODEC_DAV1D=SYSTEM \
  -DAVIF_CODEC_RAV1E=SYSTEM \
  -DAVIF_CODEC_SVT=SYSTEM \
  -DAVIF_BUILD_APPS=ON \
  -DAVIF_BUILD_GDK_PIXBUF=OFF \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install


%files
%{_libdir}/libavif.so.%{sover}*

%files devel
%{_includedir}/avif
%{_libdir}/libavif.so
%{_libdir}/cmake/libavif
%{_libdir}/pkgconfig/libavif.pc

%files tools
%{_bindir}/avifdec
%{_bindir}/avifenc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-2
- Add libavif for AVIF codecs in Qt and browsers
