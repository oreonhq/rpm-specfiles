%global source0_hash 880ec0de2b7734cde4cfe7b1e6e1bcde030f3808ab78ead42907cfeac260c09a
Name:           dtk6gui
Version:        6.7.32
Release:        1%{?dist}
Summary:        Deepin Toolkit, gui module for DDE look and feel
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkgui
Source0:        https://github.com/linuxdeepin/dtkgui/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(DtkBuildHelper)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  wayland-devel
# /oreon:deps
%description
Deepin Tool Kit (DtkGui) is the development graphical user interface of all
C++/Qt Developer work on Deepin.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -GNinja -DDTK5=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtk6gui-devel -f %{oreon_filedir}/dtk6gui-devel.list

%changelog

%autochangelog
