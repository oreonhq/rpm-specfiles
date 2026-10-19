%global source1_hash ce88e0a66230d584051213e680f3f350302d7d12de5c13d0fd632f1e39bd74b2
%global source0_hash 639a501b877446b19905399d27e2be2b6ebb0bb481abe3209dc4d535a12e12ca
%global		framework kwindowsystem
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module with classes for windows management
License:	CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:	kf6-filesystem
Requires:	libXfixes%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  egl-wayland-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
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
%find_lang_kf6 kwindowsystem6_qt
%fdupes %{buildroot}%{_kf6_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kwindowsystem-devel -f %{oreon_filedir}/kf6-kwindowsystem-devel.list

%changelog

%autochangelog
