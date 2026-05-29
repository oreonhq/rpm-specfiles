%global source0_hash 0a545e953cc049bf5bcf4ee467306a2f113a75110edf59e61248873101cd26c1
%global source1_hash 7727b0498851e5b6a6fcd734eb667a8a231897e2c86a357aec51cc0664813060

%global sover 16
# Same commit as cmake/Modules/LocalLibargparse.cmake in this libavif release
%global libargparse_commit ee74d1b53bd680748af14e737378de57e2a0a954

Name:           libavif
Version:        1.3.0
Release:        9%{?dist}
Summary:        Library for encoding and decoding AVIF images
License:        BSD-2-Clause
URL:            https://github.com/AOMediaCodec/libavif
Source0:        https://github.com/AOMediaCodec/libavif/archive/v1.3.0/libavif-1.3.0.tar.gz
# Vendored libargparse tarball so we never use FetchContent/git in mock (see ext/libargparse.patch)
Source1:        https://github.com/kmurray/libargparse/archive/ee74d1b53bd680748af14e737378de57e2a0a954/libargparse-ee74d1b53bd680748af14e737378de57e2a0a954.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(libxml-2.0)
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
mkdir -p ext
tar -xzf %{SOURCE1} -C ext
mv "ext/libargparse-%{libargparse_commit}" ext/libargparse
patch -p1 --fuzz=0 -d ext/libargparse < ext/libargparse.patch


%build
# Produce ext/libargparse/build/libargparse.a so LocalLibargparse.cmake skips FetchContent (no git, no network)
%{__cmake} -GNinja -S ext/libargparse -B ext/libargparse/build \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_BUILD_TYPE=Release
%{__cmake} --build ext/libargparse/build %{?_smp_build_ncpus:--parallel %{_smp_build_ncpus}} --target libargparse

%cmake \
  -GNinja \
  -DAVIF_CODEC_AOM=OFF \
  -DAVIF_CODEC_RAV1E=OFF \
  -DAVIF_CODEC_SVT=OFF \
  -DAVIF_CODEC_DAV1D=SYSTEM \
  -DAVIF_LIBYUV=OFF \
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
%{_bindir}/avifgainmaputil


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-2
- Add libavif for AVIF codecs in Qt and browsers
