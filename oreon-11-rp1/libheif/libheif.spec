%global source0_hash 3be49950c75d3fd9318ba775e8253248dd9e08c61ea955fca81b6b89c02d6b2b
%global somajor 1
%bcond bootstrap 0
Name:           libheif
Version:        1.23.5
Release:        1%{?dist}
Summary:        HEIF and AVIF file format decoder and encoder
License:        LGPL-3.0-or-later and MIT
URL:            https://github.com/strukturag/libheif
Source0:        https://github.com/strukturag/libheif/archive/refs/tags/v%{version}.tar.gz#/libheif-%{version}.tar.gz
%if !%{with bootstrap}
%endif
Obsoletes:      heif-pixbuf-loader < %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  openjpeg2-tools
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libsharpyuv)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format)
file format decoder and encoder.

%package        tools
Summary:        Tools for manipulating HEIF files
License:        MIT
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       shared-mime-info
%description    tools
This package provides tools for manipulating HEIF files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
rm -rf third-party/

%build

%cmake \
 -GNinja \
 -DBUILD_TESTING=ON \
 -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
 -DPLUGIN_DIRECTORY=%{_libdir}/%{name} \
 -DWITH_AOM=OFF \
 -DWITH_AOM_PLUGIN=OFF \
 -DWITH_DAV1D=ON \
 -DWITH_DAV1D_PLUGIN=OFF \
 -DWITH_JPEG_DECODER=ON \
 -DWITH_JPEG_ENCODER=ON \
 -DWITH_OpenJPEG_DECODER=ON \
 -DWITH_OpenJPEG_DECODER_PLUGIN=OFF \
 -DWITH_OpenJPEG_ENCODER=ON \
 -DWITH_OpenJPEG_ENCODER_PLUGIN=OFF \
 -DWITH_OPENJPH_DECODER=OFF \
 -DWITH_OPENJPH_ENCODER=OFF \
 -DWITH_OPENJPH_ENCODER_PLUGIN=OFF \
 -DWITH_OpenH264_DECODER=OFF \
 -DWITH_OpenH264_ENCODER=OFF \
 -DWITH_RAV1E=OFF \
 -DWITH_RAV1E_PLUGIN=OFF \
 -DWITH_SvtEnc=OFF \
 -DWITH_SvtEnc_PLUGIN=OFF \
%if %{with bootstrap}
 -DWITH_EXAMPLE_HEIF_VIEW=OFF \
%endif
 -DWITH_UNCOMPRESSED_CODEC=ON \
 -DWITH_GDK_PIXBUF=OFF \
 -Wno-dev
%cmake_build
%install
%cmake_install
function multilibFileVersions(){
mv $1 ${1%%.h}-%{__isa_bits}.h
local basename=$(basename $1)
cat >$1 <<EOF
EOF
}
multilibFileVersions %{buildroot}%{_includedir}/%{name}/heif_version.h
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd redhat-linux-build
ctest %{?_smp_mflags} --output-on-failure -E '^region$'
%files -f %{oreon_filedir}/main.list
%files -n libheif-tools -f %{oreon_filedir}/libheif-tools.list
%files -n libheif-devel -f %{oreon_filedir}/libheif-devel.list

%changelog

%autochangelog
