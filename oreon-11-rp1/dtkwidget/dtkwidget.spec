%global source0_hash e0f403e7acb3479de9216aff83bb2ade8d6b1f3d58d81a9fd76a1c030a751b13
Name:           dtkwidget
Version:        6.7.50
Release:        1%{?dist}
Summary:        Deepin tool kit widget modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(DtkGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  qt5-qtbase-private-devel
# /oreon:deps
%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
%oreon_prep
%build

%cmake -GNinja \
    -DDTK_VERSION=%{version} \
    -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtkwidget-devel -f %{oreon_filedir}/dtkwidget-devel.list

%changelog

%autochangelog
