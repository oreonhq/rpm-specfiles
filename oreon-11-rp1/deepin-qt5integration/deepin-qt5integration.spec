%global source0_hash 8297e40670cfad5a13743fc2e5d9ae6fae928dcb53e9343bc2af8ce68baa4abc

%global repo qt5integration
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\.so$

Name:           deepin-qt5integration
Version:        5.7.5
Release:        %autorelease
Summary:        Qt platform theme integration plugins for DDE
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/qt5integration
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5ThemeSupport)

# for Qt5::ThemeSupport
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  cmake(DtkWidget) >= %{version}

BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(x11)

Requires:       deepin-qt5platform-plugins%{?_isa}

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build
%cmake -DENABLE_QT_XDG_ICON_LOADER=OFF -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_qt5_plugindir}/iconengines/libdicon.so
%{_qt5_plugindir}/iconengines/libdsvgicon.so
%{_qt5_plugindir}/imageformats/libdci.so
%{_qt5_plugindir}/imageformats/libdsvg.so
%{_qt5_plugindir}/platformthemes/libqdeepin.so
%{_qt5_plugindir}/styles/libchameleon.so

%changelog
%autochangelog
