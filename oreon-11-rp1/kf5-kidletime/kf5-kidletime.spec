%global source0_hash 706f44ef35dc9182021847c9c9348d0cab2812bd4ba0d9050a71783c6fb74997

%global framework kidletime

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module for idle time detection

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
