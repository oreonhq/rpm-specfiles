%global source0_hash df317e03acfadfcbc68981b78131750103fadf4d5c5df6368c9e91e698677219
%undefine __cmake_in_source_build
%global stable_plasma stable
%global plasma_ver 6.7.4
Name:           libkscreen
Version:        6.7.5
Release:        1%{?dist}
Summary:        KDE screen management library
License:        LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND CC0-1.0
URL:            https://invent.kde.org/plasma/libkscreen
Source0:        https://download.kde.org/%{stable_plasma}/plasma/%{version}/%{name}-%{version}.tar.xz
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
libkscreen provides runtime support for listing outputs, reading display
configuration, Wayland and X11 backends, and helpers used by Plasma
(powerdevil, kscreen, kwin, etc.).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)
%description    devel
Headers and CMake package KF6Screen for software that links libkscreen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libkscreen-%{version}
%oreon_prep
%build

%cmake_kf6 -DBUILD_QCH:BOOL=OFF
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 libkscreen6_qt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libkscreen-devel -f %{oreon_filedir}/libkscreen-devel.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.7.4-1
- Latest upstream release

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-4
- Package versioned .so, zsh completion; turn off QCH (no qt6 help install)

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-3
- Fix kscreen backend glob (no double kf6 under %%{_kf6_plugindir})

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Plasma 6.6.3 source, backends, launcher, translations (KF6Screen)
