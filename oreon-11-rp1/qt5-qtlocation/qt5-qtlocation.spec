%global source0_hash ea2ed52b085989fe38d0e7f9080da4104d4707d60d8d3b5f5a478b9bec325a3c
%global qt_module qtlocation
Summary:        Qt5 - Location component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: (LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND ISC AND BSL-1.0 AND MIT
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch1:   0001-Fix-appendChildNode-call.patch
Patch5:   0005-Fix-build-of-Qt.labs.location-QML-plugin.patch
Patch6:   0006-Fix-HereMap-plugin-not-supporting-authentication-via.patch
Patch100: 0100-Add-some-missing-cstdint-inclusions-872.patch
Patch101: 0101-Add-missing-include.patch
Patch102: 0102-Removed-non-compiling-assignment-operator.-Fixed-718.patch
Patch103: 0103-Explicitly-disable-copy-assignment-operator.patch
Patch104: 0104-Fix-build-with-ICU-75.patch
Patch200: 0200-Bump-mapbox-gl-native-deps.patch
Patch201: 0201-mapbox-gl-fix-smart-ptr.patch
%global __provides_exclude_from ^(%{_qt5_archdatadir}/qml/.*\\.so|%{_qt5_plugindir}/.*\\.so)$
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Provides: bundled(geojson-cpp) = 0.5.1
Provides: bundled(geojson-vt-cpp) = 6.6.5
Provides: bundled(kdbush-hpp) = 0.1.3
Provides: bundled(shelf-pack-cpp) = 2.1.1
Provides: bundled(supercluster-hpp) = 0.5.0
Provides: bundled(unique-resource) = 0~gcba309e
Provides: bundled(vector-tile) = 1.0.4
Provides: bundled(nunicode) = 1.11
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  earcut-hpp-devel
BuildRequires:  geometry-hpp-devel
BuildRequires:  make
BuildRequires:  mapbox-variant-devel
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  polylabel-devel
BuildRequires:  protozero-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  rapidjson-devel
BuildRequires:  wagyu-devel
# /oreon:deps
%description
The Qt Location and Qt Positioning APIs gives developers the ability to
determine a position by using a variety of possible sources, including
satellite, or wifi, or text file, and so on.

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
rm -rf src/3rdparty/mapbox-gl-native/deps/{boost,earcut,geometry,optional,polylabel,protozero,rapidjson,wagyu,tao_tuple,variant}

%build

%define _lto_cflags %{nil}
%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtlocation-devel -f %{oreon_filedir}/qt5-qtlocation-devel.list
%files -n qt5-qtlocation-examples -f %{oreon_filedir}/qt5-qtlocation-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
