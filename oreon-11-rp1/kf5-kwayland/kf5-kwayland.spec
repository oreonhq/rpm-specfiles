%global framework kwayland

%global wayland_min_version 1.3

## uncomment to enable bootstrap mode
#global bootstrap 1

## currently includes no tests
%if !0%{?bootstrap}
%if 0%{?fedora}
%global tests 1
%endif
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 11%{?dist}
Summary: KDE Frameworks 5 library that wraps Client and Server Wayland libraries

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND MIT-CMU
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

Patch0:  kwayland-fix-build.patch

BuildRequires: make
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  qt5-qtbase-devel
# https://bugs.kde.org/show_bug.cgi?id=365569#c8 claims this is needed
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static

BuildRequires:  wayland-devel >= %{wayland_min_version}
BuildRequires:  wayland-protocols-devel
BuildRequires:  qt5-qttools-devel

BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(PlasmaWaylandProtocols) > 1.1

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: weston
BuildRequires: xorg-x11-server-Xvfb
%endif


Requires:       kf5-filesystem >= %{version}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_libdir}/libKF5WaylandClient.so.5*
%{_kf5_libdir}/libKF5WaylandServer.so.5*
# not sure if this belongs here or in -devel --rex
%{_libexecdir}/org-kde-kf5-kwayland-testserver

%files devel
%{_kf5_includedir}/KWayland/
%{_kf5_libdir}/cmake/KF5Wayland/
%{_kf5_libdir}/libKF5WaylandClient.so
%{_kf5_libdir}/libKF5WaylandServer.so
%{_kf5_libdir}/pkgconfig/KF5WaylandClient.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KWaylandClient.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KWaylandServer.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-11
- Prepare for Oreon 11 (RP1)
