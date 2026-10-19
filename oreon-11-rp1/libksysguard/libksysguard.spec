%global source1_hash 4cedcb90248fd7359f2eb61aab41b5b4537aa77fcf66524ce410cc541629e110
%global source0_hash 9069bcf3fe4e491ea774d0d70eb17f99b567299871045a38543fcabcdb56dfc4
%global stable_kf6 stable
Name:    libksysguard
Summary:        Library for managing processes running on the system
Version:        6.7.5
Release:        1%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
%ifarch %{qt6_qtwebengine_arches}
%endif
Obsoletes:      kf5-ksysguard < 5.1.95
Provides:       kf5-ksysguard = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Conflicts: ksysguard-backend < 5.21.90
# oreon:deps
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libXres-devel
BuildRequires:  libcap-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  qt6-qttools-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KSysGuard library provides API to read and manage processes
running on the system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6I18n)
Requires:       cmake(KF6IconThemes)
Obsoletes:      kf5-ksysguard-devel < 5.1.95
Provides:       kf5-ksysguard-devel = %{version}-%{release}
Conflicts:      kde-workspace-devel < 1:4.11.16-11
%package        common
Summary:        Runtime data files shared by libksysguard and ksysguard-libs
Conflicts:      libksysguard < 5.2.1-2
Conflicts:      ksysguard < 5.2
%description    common
%{summary}.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DENABLE_KAUTH_HELPER:BOOL=%{!?flatpak:ON}%{?flatpak:OFF}
%cmake_build
%install
%cmake_install
%find_lang ksysguard_qt6 --with-qt --with-kde --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libksysguard-devel -f %{oreon_filedir}/libksysguard-devel.list
%files -n libksysguard-common -f %{oreon_filedir}/libksysguard-common.list

%changelog

%autochangelog
