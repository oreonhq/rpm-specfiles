%global source4_hash 3ccec8c0cf848b3fdf5a843fe66b793e28c34a2a4f8f9c9a2ce96a5d0840b650
%global source3_hash 026e12a86214e7a2c24477a307c82240f07dcc65b53b68763b7b408c43d5d2cb
%global source2_hash b18b92ba60ec3186dc36ef671d3c2ae542cbb63eb6dc0e258476c6111a67c971
%global source1_hash 75ff666a4ce1615b3ca26abbb17b10f5cb5cf5f86c9c293ec430c34750d3ea27
%global source0_hash 75ff666a4ce1615b3ca26abbb17b10f5cb5cf5f86c9c293ec430c34750d3ea27
%global krita_python 1
%global versiondir %(echo %{version} | cut -d. -f1-3)
%global zug_version 0.1.2
%global immer_version 0.9.1
%global lager_version 0.1.2
%global raqm_version 0.10.1
%global gmic_version 3.6.6.2
Name:           krita
Version:        6.0.4
Release:        1%{?dist}
Summary:        Krita is a sketching and painting program
License:        GPL-2.0-or-later
URL:            https://krita.org
Source0:        https://download.kde.org/unstable/krita/%{version}/krita-%{version}.tar.xz
Source1:        https://github.com/arximboldi/zug/archive/v%{zug_version}/zug-%{zug_version}.tar.gz
Source2:        https://github.com/arximboldi/immer/archive/v%{immer_version}/immer-%{immer_version}.tar.gz
Source3:        https://github.com/arximboldi/lager/archive/v%{lager_version}/lager-%{lager_version}.tar.gz
Source4:        https://github.com/vanyossi/gmic/releases/download/v%{gmic_version}/gmic-%{gmic_version}.tar.gz
Patch: 0001-KoStreamedMath-fix-build-on-XSIMD_NO_SUPPORTED_ARCHI.patch
Patch: krita-6.0.0-appstream_validate.patch
ExcludeArch:    %{ix86}
%if 0%{?krita_python}
Requires: python3-pyqt6-base
%endif
Requires: hicolor-icon-theme
Provides: bundled(zug) = %{zug_version}
Provides: bundled(immer) = %{immer_version}
Provides: bundled(lager) = %{lager_version}
Provides: bundled(raqm) = %{raqm_version}
Provides: bundled(CImg) = %{gmic_version}
Provides: bundled(gmic) = %{gmic_version}
Obsoletes: %{name}-libs < %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  cmake(Catch2)
BuildRequires:  cmake(Eigen3)
BuildRequires:  cmake(KDcrawQt6)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Mlt7)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  cmake(WebP)
BuildRequires:  cmake(kseexpr)
BuildRequires:  cmake(sdl2)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libtiff-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libunibreak)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xsimd)
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt6-devel
BuildRequires:  sip6
BuildRequires:  zlib-devel
# /oreon:deps
%description
Krita is a sketching and painting program.
It was created with the following types of art in mind:
- concept art
- texture or matte painting
- illustrations and comics

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version} -a 1 -a 2 -a 3 -a 4
%autopatch -p1
# fix gmic
sed -i -e 's/lrelease-qt5/lrelease-qt6/g' \
  gmic-v%{gmic_version}/gmic-qt/translations/lrelease.sh

%build

%cmake -Dzug_BUILD_EXAMPLES=FALSE \
       -Dzug_BUILD_DOCS:BOOL=FALSE  \
       -B zug -S zug-%{zug_version}/
DESTDIR=$(pwd) cmake --install zug --prefix /
%cmake  -Dimmer_BUILD_DOCS:BOOL=FALSE \
        -Dimmer_BUILD_EXAMPLES:BOOL=FALSE \
        -Dimmer_BUILD_EXTRAS:BOOL=FALSE \
        -DDISABLE_WERROR:BOOL=TRUE \
        -B immer -S immer-%{immer_version}/
DESTDIR=$(pwd) cmake --install immer --prefix /
%cmake  -Dlager_BUILD_EXAMPLES:BOOL=FALSE \
        -Dlager_BUILD_DEBUGGER_EXAMPLES:BOOL=FALSE \
        -Dlager_BUILD_DOCS:BOOL=FALSE -DCMAKE_PREFIX_PATH=$(pwd) \
        -B lager -S lager-%{lager_version}/
DESTDIR=$(pwd) cmake --install lager --prefix /
%cmake_kf6 -G Ninja \
   -DCMAKE_PREFIX_PATH=$(pwd) \
   -DBUILD_WITH_QT6:BOOL=ON \
   -DBUILD_TESTING:BOOL=OFF
%cmake_build
CXXFLAGS+=" -I$(pwd)/plugins/extensions/qmic" \
%cmake -DGMIC_QT_HOST=krita-plugin \
       -DENABLE_SYSTEM_GMIC=FALSE \
       -DKIS_IMAGE_INTERFACE_DIR="$(pwd)/%{__cmake_builddir}/plugins/extensions/qmic" \
       -DKIS_IMAGE_INTERFACE_LIBRARY="$(pwd)/%{__cmake_builddir}/bin/libkritaqmicinterface.so" \
       -B gmic-qt -S gmic-v%{gmic_version}/gmic-qt
%__cmake --build gmic-qt %{_smp_mflags} --verbose
%install
%cmake_install
DESTDIR=%{buildroot} %__cmake --install gmic-qt
rm -f %{buildroot}%{_datadir}/gmic/*.gmz
chrpath --delete %{buildroot}%{_libdir}/kritaplugins/krita_gmic_qt.so
rm -fv %{buildroot}%{_includedir}/*
rm -fv %{buildroot}%{_libdir}/libkrita*.so
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.krita.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.krita.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
