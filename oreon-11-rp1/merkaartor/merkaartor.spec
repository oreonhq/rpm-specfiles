%global source0_hash 31b73a9d50cb6366a7c15ab36e030467ffe9f7de2be38bad5f3832314d4a5751
Name:           merkaartor
Version:        0.20.0
Release:        1%{?dist}
Summary:        Qt-Based OpenStreetMap editor
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only)
URL:            http://www.merkaartor.be
Source0:        https://github.com/openstreetmap/merkaartor/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         merkaartor-0.19.0-CMAKE_INSTALL_LIBDIR.patch
Patch1:         merkaartor-0.20.0-system-qtsingleapplication.patch
Patch2:         https://github.com/openstreetmap/merkaartor/commit/28cca84e9f5db0aaba87c2084ed32f9677598823.patch
%if 0%{?system_qtsingleapplication}
%else
Provides:       bundled(qtsingleapplication) = 2.6.1
%endif
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtchooser
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{name}.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.%{name}.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
