%global source0_hash 880ec0de2b7734cde4cfe7b1e6e1bcde030f3808ab78ead42907cfeac260c09a

Name:           dtk6gui
Version:        6.7.32
Release:        %autorelease
Summary:        Deepin Toolkit, gui module for DDE look and feel
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkgui
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)

BuildRequires:  cmake(Dtk6Core) >= %{version}
BuildRequires:  cmake(DtkBuildHelper)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(libraw)

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

%autosetup -p1 -C

%build
%cmake -GNinja -DDTK5=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdtk6gui.so.6*
%{_libexecdir}/dtk6/DGui/

%files devel
%{_libdir}/libdtk6gui.so
%{_includedir}/dtk6/DGui/
%{_libdir}/cmake/Dtk6Gui/
%{_libdir}/pkgconfig/dtk6gui.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri

%changelog
%autochangelog
