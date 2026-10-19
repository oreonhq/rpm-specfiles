%global source0_hash e8b84ac98b0b689a244e4036c4b56394c1d58ce2d9abc05e0a060ef9f756dc36
Name: darktable
Version: 5.6.1
Release:        1%{?dist}
Summary:        Utility to organize and develop raw images
License: GPL-3.0-or-later
URL: http://www.darktable.org/
Source0:        https://github.com/darktable-org/darktable/releases/download/release-%{version}/%{name}-%{version}.tar.xz
Patch0: 0001-Add-5.4.1-in-appdata.patch
Requires: iso-codes >= 3.66
Provides: bundled(rawspeed)
Provides: bundled(libraw)
ExcludeArch: armv7hl i686 s390x
# oreon:deps
BuildRequires:  GraphicsMagick-devel
BuildRequires:  cairo-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(SDL2)
BuildRequires:  cmake(libavif)
BuildRequires:  colord-devel
BuildRequires:  colord-gtk-devel
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  exiv2-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gmic-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  json-glib-devel
BuildRequires:  lcms2-devel
BuildRequires:  lensfun-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libheif-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  llvm-devel
BuildRequires:  opencl-headers
BuildRequires:  openjpeg2-devel
BuildRequires:  osm-gps-map-devel
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lua)
BuildRequires:  po4a
BuildRequires:  portmidi-devel
BuildRequires:  pugixml-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
darktable manages your camera raw files and images in a database, lets you
view them through lighttable mode and develop/enhance them in darkroom mode.

%package tools-noise
Summary:        The noise profiling tools to support new cameras
Requires:       ImageMagick
Requires:       gnuplot
%description tools-noise
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

%package tools-basecurve
Summary:        The basecurve tool from tools/basecurve/
Requires:       ImageMagick
Requires:       dcraw
Requires:       perl-Image-ExifTool
%description tools-basecurve
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

This package provides the basecurve tool from tools/basecurve/.
Another option to solve the same problem might be the darktable-chart module
from the darktable package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Remove bundled OpenCL headers.
rm -rf src/external/CL
sed -i -e 's, \"external/CL/\*\.h\" , ,' src/CMakeLists.txt

%build

%cmake \
        -DCMAKE_LIBRARY_PATH:PATH=%{_libdir} \
        -DUSE_GEO:BOOLEAN=ON \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DBINARY_PACKAGE_BUILD=1 \
        -DBUILD_NOISE_TOOLS=ON \
        -DBUILD_CURVE_TOOLS=ON \
        -DRAWSPEED_ENABLE_LTO=ON
%make_build
popd
%install
pushd %{_target_platform}
%make_install
popd
%find_lang %{name}
rm -rf %{buildroot}%{_datadir}/doc/darktable
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.darktable.darktable.appdata.xml
%oreon_autofiles darktable-tools-noise usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles darktable-tools-basecurve usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n darktable-tools-noise -f %{oreon_filedir}/darktable-tools-noise.list
%files -n darktable-tools-basecurve -f %{oreon_filedir}/darktable-tools-basecurve.list

%changelog

%autochangelog
