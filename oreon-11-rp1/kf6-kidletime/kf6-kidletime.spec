# Disable X11 for RHEL
%bcond x11 %[%{undefined rhel}]

%global		framework kidletime
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	3%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module for idle time detection
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Qt6WaylandClient)
Requires:	kf6-filesystem
%if %{with x11}
Recommends:	%{name}-x11%{?_isa} = %{version}-%{release}
%endif

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
# X11 is deprecated and this will be removed eventually...
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
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
  -DWITH_X11=%{?with_x11:ON}%{?!with_x11:OFF}
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6IdleTime.so.*
%dir %{_kf6_plugindir}/org.kde.kidletime.platforms/
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so

%if %{with x11}
%files x11
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin0.so
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin1.so
%endif

%files devel
%{_kf6_includedir}/KIdleTime/
%{_kf6_libdir}/libKF6IdleTime.so
%{_kf6_libdir}/cmake/KF6IdleTime/

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
