%global source0_hash none

%global qt_module qtsvg

Summary: Qt5 - Support for rendering and displaying SVG
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
## upstream patches
## repo: https://invent.kde.org/qt/qt/qtsvg
## branch: kde/5.15
## git format-patch v5.15.16-lts-lgpl
Patch1:  0001-Avoid-buffer-overflow-in-isSupportedSvgFeature.patch
Patch2:  0002-Support-font-size-not-in-pixels.patch
Patch3:  0003-Fix-text-x-y-when-the-length-is-not-in-pixels.patch
Patch4:  0004-Improve-parsing-of-r.patch
Patch5:  0005-SVG-Image-reading-Reject-oversize-svgs-as-corrupt.patch

# backport for CVE-2025-10729
Patch10: qtsvg-5.15.17-CVE-2025-10729.patch

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: pkgconfig(zlib)

BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Scalable Vector Graphics (SVG) is an XML-based language for describing
two-dimensional vector graphics. Qt provides classes for rendering and
displaying SVG drawings in widgets and on other paint devices.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5Svg.so.5*
%{_qt5_plugindir}/iconengines/libqsvgicon.so
%{_qt5_plugindir}/imageformats/libqsvg.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QSvg*Plugin.cmake

%files devel
%{_qt5_headerdir}/QtSvg/
%{_qt5_libdir}/libQt5Svg.so
%{_qt5_libdir}/libQt5Svg.prl
%dir %{_qt5_libdir}/cmake/Qt5Svg/
%{_qt5_libdir}/cmake/Qt5Svg/Qt5SvgConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5Svg.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_svg*.pri

%files examples
%{_qt5_examplesdir}/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
