%global source0_hash 810c399f3b9fbfd72e24e61417ede24243925f9c0d03040a8aba0d4866676d93
%global qtcolor_commit 352bc8f99bf2174d5724ee70623427aa31ddc26a
%global qtcolor_url https://gitlab.com/mattbas/Qt-Color-Widgets
Name: flameshot
Version: 14.0.0
Release:        1%{?dist}
License: GPL-3.0-or-later AND Apache-2.0 AND GPL-2.0-only AND LGPL-3.0-or-later AND (LGPL-3.0-only OR GPL-3.0-only) AND LAL-1.3
Summary:        Powerful and simple to use screenshot software
URL: https://github.com/flameshot-org/%{name}
Source0:        https://github.com/%{name}-org/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{qtcolor_url}/-/archive/%{qtcolor_commit}/Qt-Color-Widgets-%{qtcolor_commit}.tar.gz
Requires: grim
Requires: hicolor-icon-theme
Requires: qt6-qtsvg%{?_isa}
Recommends: xdg-desktop-portal%{?_isa}
Recommends: (xdg-desktop-portal-gnome%{?_isa} if gnome-shell%{?_isa})
Recommends: (xdg-desktop-portal-kde%{?_isa} if plasma-workspace-wayland%{?_isa})
Recommends: (xdg-desktop-portal-wlr%{?_isa} if wlroots%{?_isa})
Provides: bundled(qt-color-widgets) = 2.2.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
# /oreon:deps
%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir -p external/Qt-Color-Widgets
tar -xf %{SOURCE1} -C external/Qt-Color-Widgets --strip-components=1

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_BUNDLED_KDSINGLEAPPLICATION:BOOL=OFF \
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DUSE_LAUNCHER_ABSOLUTE_PATH:BOOL=OFF
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_includedir}/QtColorWidgets
rm -rf %{buildroot}%{_libdir}/cmake/QtColorWidgets
rm -f %{buildroot}%{_libdir}/libQtColorWidgets.*
rm -f %{buildroot}%{_libdir}/pkgconfig/QtColorWidgets.pc
%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
