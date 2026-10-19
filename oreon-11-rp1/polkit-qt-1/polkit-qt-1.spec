%global source0_hash 95d8e2cae530c546d9437459deb8a1bea38d572f0f9772cc2860dc143637f256
Name:            polkit-qt-1
Version:         0.201.1
Release:        1%{?dist}
Summary:        Qt bindings for PolicyKit
License:         BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:             https://api.kde.org/kdesupport-api/polkit-qt-1-apidocs/
Source0:        https://download.kde.org/stable/%{name}/polkit-qt-1-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
# /oreon:deps
%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt5-1
Summary: PolicyKit Qt5 bindings
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes: polkit-qt5 < 0.112.0-3
Provides:  polkit-qt5 = %{version}-%{release}
%description -n polkit-qt5-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt5-1-devel
Summary: Development files for PolicyKit Qt5 bindings
Obsoletes: polkit-qt5-devel < 0.112.0-3
Provides:  polkit-qt5-devel = %{version}-%{release}
Requires: polkit-qt5-1%{?_isa} = %{version}-%{release}
%description -n polkit-qt5-1-devel
%{summary}.

%package -n polkit-qt6-1
Summary: PolicyKit Qt6 bindings
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
%description -n polkit-qt6-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt6-1-devel
Summary: Development files for PolicyKit Qt5 bindings
Requires: polkit-qt6-1%{?_isa} = %{version}-%{release}
%description -n polkit-qt6-1-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%global _vpath_builddir %{_target_platform}-qt5
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DQT_MAJOR_VERSION=5
%cmake_build
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DQT_MAJOR_VERSION=6
%cmake_build
%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%oreon_autofiles polkit-qt5-1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles polkit-qt5-1-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles polkit-qt6-1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles polkit-qt6-1-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n polkit-qt5-1 -f %{oreon_filedir}/polkit-qt5-1.list
%files -n polkit-qt5-1-devel -f %{oreon_filedir}/polkit-qt5-1-devel.list
%files -n polkit-qt6-1 -f %{oreon_filedir}/polkit-qt6-1.list
%files -n polkit-qt6-1-devel -f %{oreon_filedir}/polkit-qt6-1-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.201.1-1
- Import
