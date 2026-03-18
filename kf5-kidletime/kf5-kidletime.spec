%global framework kidletime

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module for idle time detection

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-sync)

BuildRequires:  pkgconfig(xscrnsaver)

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 integration module for idle time detection.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5IdleTime.so.*
%dir %{_kf5_plugindir}/org.kde.kidletime.platforms/
%{_kf5_plugindir}/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin0.so
%{_kf5_plugindir}/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin1.so
%{_kf5_plugindir}/org.kde.kidletime.platforms/KF5IdleTimeWaylandPlugin.so

%files devel
%{_kf5_includedir}/KIdleTime/
%{_kf5_libdir}/libKF5IdleTime.so
%{_kf5_libdir}/cmake/KF5IdleTime/
%{_kf5_archdatadir}/mkspecs/modules/qt_KIdleTime.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
