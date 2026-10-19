%global source0_hash 2ddabe29794489d11096ed831ad4d5c1626130019322d4305d58df84c835b279
%global  wayland_min_version 1.3
Name:    kwayland-server
Version: 5.24.5
Release:        11%{?dist}
Summary:        Wayland server components built on KDE Frameworks
License: LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:     https://invent.kde.org/plasma/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Patch0:        kwayland-server-drm-fourcc-u64.patch
# oreon:deps
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
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
%setup -q
%patch 0 -p1

%build

%cmake_kf5 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kwayland-server-devel -f %{oreon_filedir}/kwayland-server-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.24.5-11
- Import
