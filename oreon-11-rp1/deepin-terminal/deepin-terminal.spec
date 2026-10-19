%global source0_hash f5f8199c4595aa41cc237d06af7914b8c99d6ff06f8f504f0a8d7bdaae0749d4
Name:           deepin-terminal
Version:        6.5.40
Release:        1%{?dist}
Summary:        Default terminal emulation application for Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Recommends:     deepin-manual
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  qt6-linguist
BuildRequires:  uchardet-devel
# /oreon:deps
%description
Deepin Terminal is an advanced terminal emulator with workspace , multiple
windows, remote management, quake mode and other features.

%prep

%autosetup -p1

sed -i 's|SHARED|STATIC|' 3rdparty/terminalwidget/CMakeLists.txt
sed -i 's|/lib|%{_libdir}|' cmake/translation-generate.cmake
sed -i 's|DDE;||' src/deepin-terminal.desktop

%build

%cmake -GNinja
%cmake_build
%install
%cmake_install
rm -r %{buildroot}%{_includedir}/terminalwidget6/ \
    %{buildroot}%{_libdir}/libterminalwidget6.a \
    %{buildroot}%{_libdir}/cmake/terminalwidget6/ \
    %{buildroot}%{_libdir}/pkgconfig/terminalwidget6.pc \
    %{buildroot}%{_datadir}/terminalwidget6/
chmod u+w %{buildroot}%{_bindir}/deepin-terminal
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
