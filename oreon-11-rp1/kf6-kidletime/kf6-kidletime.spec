%global source1_hash 27c73b2f559813cdc1930770b30ef854debc0b5232bd382016bc45e61a5fd012
%global source0_hash 22873204292ddb757e5a0a57004c57debe1285cd0fd4e796d07e9de2402e60c3
%bcond x11 %[%{undefined rhel}]
%global		framework kidletime
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module for idle time detection
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:	kf6-filesystem
%if %{with x11}
Recommends:	%{name}-x11%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 1 integration module for idle time detection.

%if %{with x11}
%package	x11
Summary:	Idle time detection plugins for X11 environments
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-sync)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xkbcommon)
Requires:	%{name}%{?_isa} = %{version}-%{release}
Conflicts:	%{name} < 6.6.0-1
Provides:	deprecated()
%description	x11
The %{name}-x11 package contains plugins for applications using
%{name} to detect idle time on X11 environments.
%endif

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

%cmake_kf6 \
  -DWITH_X11=%{?with_x11:ON}%{?!with_x11:OFF}
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kidletime-x11 -f %{oreon_filedir}/kf6-kidletime-x11.list
%files -n kf6-kidletime-devel -f %{oreon_filedir}/kf6-kidletime-devel.list

%changelog

%autochangelog
