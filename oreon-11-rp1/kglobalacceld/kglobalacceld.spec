%global source1_hash fa9d58f8c91445a7a8762da14c4f2faaf78c7869720b1c28974754ca31de60bf
%global source0_hash 83e9a4e226e695fe1544cfa19a9659c5f1000be46c669fe3a9e299029c6c2abf
Name:    kglobalacceld
Summary:        Daemon providing Global Keyboard Shortcut functionality
Version: 6.7.5
Release:        1%{?dist}
License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:  https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:  kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  systemd
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kglobalacceld-devel -f %{oreon_filedir}/kglobalacceld-devel.list

%changelog

%autochangelog
