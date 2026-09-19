%global source0_hash ad60c9bb9530d1d51c479995683d3368cd094cf9e415525cdedc784ef2d61873

%if 0%{?fedora} > 39 || 0%{?rhel} > 9
%global system_qtsingleapplication 1
%endif

Name:           merkaartor
Version:        0.20.0
Release:        8%{?dist}
Summary:        Qt-Based OpenStreetMap editor

# GPL-2.0-or-later: main program
# GPL-3.0-or-later: plugins/background/MCadastreFranceBackground/qadastre
# LGPL-3.0-or-later:
# - src/ImportExport/fileformat.proto
# - src/ImportExport/osmformat.proto
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only: src/QToolBarDialog
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only)
URL:            http://www.merkaartor.be
Source0:        https://github.com/openstreetmap/merkaartor/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/openstreetmap/merkaartor/pull/291
Patch0:         merkaartor-0.19.0-CMAKE_INSTALL_LIBDIR.patch
# https://github.com/openstreetmap/merkaartor/pull/292
Patch1:         merkaartor-0.20.0-system-qtsingleapplication.patch
# Fix build against gdal-3.12.0
Patch2:         https://github.com/openstreetmap/merkaartor/commit/28cca84e9f5db0aaba87c2084ed32f9677598823.patch

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(proj) >= 6.0.0
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtchooser
%if 0%{?system_qtsingleapplication}
BuildRequires:  qtsingleapplication-qt6-devel
%else
Provides:       bundled(qtsingleapplication) = 2.6.1
%endif
Requires:       hicolor-icon-theme

%description
Merkaartor is a small editor for OpenStreetMap available under the
GNU General Public License and developed using the Qt toolkit.

It has some unique features like anti-aliased displaying,
transparent display of map features like roads and curved roads.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%patch -P0 -p1 -b .CMAKE_INSTALL_LIBDIR
%patch -P1 -p1 -b .system-qtsingleapplication
%patch -P2 -p1 -b .gdal312

%if 0%{?system_qtsingleapplication}
# Use packaged qtsingleapplication instead of bundled version
rm -rfv 3rdparty/qtsingleapplication-2.6_1-opensource
%endif

%build
# ZBAR: zbar is still Qt 5, Merkaartor is now Qt 6
# WEBENGINE: QtWebEngine support is not implemented yet, the flag does nothing
%if 0%{?system_qtsingleapplication}
%global system_qtsingleapplication_cmake ON
%else
%global system_qtsingleapplication_cmake OFF
%endif
%cmake -DZBAR=OFF \
       -DGEOIMAGE=ON \
       -DGPSD=ON \
       -DWEBENGINE=OFF \
       -DUSE_SYSTEM_QTSINGLEAPPLICATION=%{system_qtsingleapplication_cmake}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.%{name}.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS CHANGELOG HACKING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/%{name}/
%{_metainfodir}/org.%{name}.%{name}.appdata.xml

%changelog
%autochangelog
