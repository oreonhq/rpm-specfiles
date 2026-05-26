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
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 2ddabe29794489d11096ed831ad4d5c1626130019322d4305d58df84c835b279
%global source0_file kwayland-server-5.24.5.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/kwayland-server-5.24.5.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2ddabe29794489d11096ed831ad4d5c1626130019322d4305d58df84c835b279" || { echo "oreon: Source0 SHA256 mismatch for kwayland-server-5.24.5.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-11
- Import
