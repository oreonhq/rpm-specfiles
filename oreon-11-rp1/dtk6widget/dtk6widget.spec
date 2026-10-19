%global source0_hash b9c31cc91ea56b322d4f165e9c2c465ab4393f25e59ae87ff0234be23bace254
Name:           dtk6widget
Version:        6.7.32
Release:        1%{?dist}
Summary:        Deepin base graphical widgets library
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        https://github.com/linuxdeepin/dtkwidget/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         dtk6widget-fix-build-with-qt-6-10-2.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupportPrivate)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
# /oreon:deps
%description
Deepin Tool Kit Widget(DtkWidget) provides the base widgets on Deepin.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

%autosetup -p1
sed -i 's|/dtk@DTK_VERSION_MAJOR@/DWidget||' misc/DtkWidget.pc.in

%build

%cmake -GNinja -DDTK5=OFF -DQCH_INSTALL_DESTINATION=%{_qt6_docdir}
%cmake_build
%install
%cmake_install
%find_lang dtkwidget --all-name --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtk6widget-devel -f %{oreon_filedir}/dtk6widget-devel.list

%changelog

%autochangelog
