%global source0_hash d04f7fb35452da9b8fcdad1e0458c0d3ffe24af08b9bcfb4bc5ab43e196df049
%global forgeurl https://github.com/linuxdeepin/dde-tray-loader
Version:        2.0.41
%global tag %{version}
%forgemeta
%global repo dde-tray-loader
Name:           deepin-tray-loader
Release:        1%{?dist}
Summary:        A set of tray plugins for Deepin
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND CC-BY-4.0 AND CC0-1.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{repo}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  wayland-devel
# /oreon:deps
%description
The dde-tray-loader project provides a set of tray plugins that integrated into
task bar and the tool loader which can load the plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
sed -i '/LIBRARY DESTINATION/s|lib/dde-dock|${CMAKE_INSTALL_LIBDIR}/dde-dock|' \
    $(find ./plugins -name '*CMakeLists.txt')

%build

%cmake -GNinja \
    -DVERSION=%{version} \
    -DDTL_BUILD_WITH_QT6=ON \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n deepin-tray-loader-devel -f %{oreon_filedir}/deepin-tray-loader-devel.list

%changelog

%autochangelog
