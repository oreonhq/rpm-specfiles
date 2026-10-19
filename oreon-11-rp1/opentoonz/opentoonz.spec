%global source0_hash d0daf60d06510efe15d0db3f9eed0162499ed58061504dca27892c2b9ea5f22d
%undefine __cmake_in_source_build
%define _vpath_srcdir toonz/sources
Name:    opentoonz
Version: 1.7.1
Release:        1%{?dist}
Summary:        2D animation software
License: LicenseRef-Callaway-BSD
URL:     https://opentoonz.github.io/
Source0:        https://github.com/opentoonz/opentoonz/archive/refs/tags/v%{version}.tar.gz
Patch0: opentoonz-1.5.0-lzo-fix.patch
Patch1: opentoonz-1.5.0-tiff-fix.patch
Patch2: opentoonz-1.7.1-exr-fix.patch
Patch3: opentoonz-1.7.0-gethostbyname.patch
Patch4: opentoonz-1.7.0-install-path-fix.patch
Patch5: opentoonz-1.7.1-kissfft-fix.patch       
Patch6: opentoonz-1.7.0-toonzrle-rm.patch
Patch7: opentoonz-1.7.0-tzp-tiffiop-fix.patch
Patch8: opentoonz-1.7.1-appdata.patch
Patch9: opentoonz-1.7.1-funcptr-fix.patch
Requires: opencv
Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SuperLU-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  flexiblas-devel
BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  kiss-fft-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmypaint-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  tinyexr-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  xz-devel
# /oreon:deps
%description
OpenToonz is a 2D animation software published by DWANGO. It is based on 
Toonz Studio Ghibli Version, originally developed in Italy by 
Digital Video, Inc., and customized by Studio Ghibli over many years of 
production.
This version was packaged for Fedora using the latest stable libraries
available in the distribution, in exchange some features were disabled.

%package data
Summary: OpenToonz data files
BuildArch: noarch
%description data
Data files for the OpenToonz application.

%package doc
Summary: OpenToonz doc files
BuildArch: noarch
%description doc
Documentation about the OpenToonz application.

%prep

%autosetup -p1

# Remove all thirdparty libraries
rm -rf thirdparty
find stuff/doc/LICENSE/ -type f -not -name 'LICENSE.txt' -delete

# add flexiblas
sed -i 's/OPENBLAS_LIB NAMES/& flexiblas/' toonz/sources/CMakeLists.txt

%build

%cmake \
    -DWITH_SYSTEM_LZO:BOOL=ON \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DWITH_TRANSLATION:BOOL=OFF
%cmake_build
%install
%cmake_install
chmod 0755 ${RPM_BUILD_ROOT}%{_libdir}/%{name}/*.so
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/io.github.OpenToonz.desktop
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/io.github.OpenToonz.appdata.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n opentoonz-data -f %{oreon_filedir}/opentoonz-data.list
%files -n opentoonz-doc -f %{oreon_filedir}/opentoonz-doc.list

%changelog

%autochangelog
