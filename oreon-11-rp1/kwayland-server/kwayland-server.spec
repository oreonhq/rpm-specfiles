%global  wayland_min_version 1.3

Name:    kwayland-server
Version: 5.24.5
Release: 14%{?dist}
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
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Patch0:  kwayland-server-drm-fourcc-linux-types.patch

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
%autosetup -p1


%build
%cmake_kf5

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
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-14
- Fix drm_fourcc patch complete hunk counts so patch applies in prep

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-13
- Patch drm_fourcc.h use linux types on Linux fix aarch64 __u64 conflict

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-12
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-11
- Prepare for Oreon 11 (RP1)
