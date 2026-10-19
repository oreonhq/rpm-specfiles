%global source0_hash 0af711d8a37c4355b8e914855a637f47d0fd3ca8c66ba239523a65d45d5a15f5
Name:           zeal
Version:        0.9.1
Release:        1%{?dist}
Summary:        Offline documentation browser inspired by Dash
License:        GPL-3.0-or-later
URL:            https://zealdocs.org/
Source0:        https://github.com/zealdocs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{qt6_qtwebengine_arches}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(httplib)
BuildRequires:  cmake(tomlplusplus)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
Zeal is a simple offline documentation browser inspired by Dash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_qt6 \
  -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.zealdocs.zeal.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.zealdocs.zeal.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
