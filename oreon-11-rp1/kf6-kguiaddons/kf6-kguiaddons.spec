%global source1_hash d4bbaa876410f8217cfa51dc634524633dcb98adfb6d7ad8557c160e1e6ae8f0
%global source0_hash e98864228d1c5e23f3428025eb9928697374fdc3eddebb3a9dec570de028a62d
%global 	framework kguiaddons
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with various classes on top of QtGui
License:	BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-pyside6-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
# /oreon:deps
%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kf6-kguiaddons -f %{oreon_filedir}/python3-kf6-kguiaddons.list
%files -n kf6-kguiaddons-devel -f %{oreon_filedir}/kf6-kguiaddons-devel.list

%changelog

%autochangelog
