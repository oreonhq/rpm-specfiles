%global source0_hash none

%global  wayland_min_version 1.3

Name:    kwayland-server
Version: 5.24.5
Release: 11%{?dist}
Summary: Wayland server components built on KDE Frameworks

# Automatically converted from old format: LGPLv2+ and MIT and BSD - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/plasma/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

Patch0:        kwayland-server-drm-fourcc-u64.patch

BuildRequires:  qt5-qtbase-devel

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kwayland-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

BuildRequires:  plasma-wayland-protocols-devel >= 1.2
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(Qt5WaylandClient)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%cmake_kf5 -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/kwaylandserver.categories
%{_kf5_libdir}/libKWaylandServer.so.*

%files devel
%{_kf5_libdir}/libKWaylandServer.so
%{_includedir}/KWaylandServer/
%{_includedir}/kwaylandserver_version.h
%{_libdir}/cmake/KWaylandServer/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-11
- Import
