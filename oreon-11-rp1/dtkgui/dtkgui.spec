%global source0_hash 7c253db6823d8283a5a4fccdea4d0575cce9264a19b94d1e66e4c1d412c30fa8
Name:           dtkgui
Version:        6.7.50
Release:        1%{?dist}
Summary:        Deepin dtkgui
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkgui
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  dtkcommon-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
# /oreon:deps
%description
Dtkgui is the GUI module for DDE look and feel.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -GNinja \
    -DDTK_VERSION=%{version} \
    -DBUILD_DOCS=OFF \
    -DDTK_DISABLE_LIBXDG=ON \
    -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtkgui-devel -f %{oreon_filedir}/dtkgui-devel.list

%changelog

%autochangelog
