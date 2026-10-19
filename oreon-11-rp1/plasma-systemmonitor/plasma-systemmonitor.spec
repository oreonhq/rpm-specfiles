%global source1_hash 78c1c94d7a0ce5a68100ae2f2c81cb187cb3c7dde1b24c750e440a0954bb4d43
%global source0_hash 5708e8f0e1833e0829144a14aba1f177262661cc57b20c4a5a34bfd6973d1f1b
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    plasma-systemmonitor
Version:        6.7.5
Release:        1%{?dist}
Summary:        An application for monitoring system resources
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires: kf6-kirigami%{?_isa}
Requires: kf6-kirigami-addons%{?_isa}
Requires: kf6-kiconthemes%{?_isa}
Requires: ksystemstats%{?_isa}
Requires: libksysguard%{?_isa}
Obsoletes: ksysguard < 5.23
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  ksystemstats
BuildRequires:  libksysguard-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
# /oreon:deps
%description
An interface for monitoring system sensors, process information and other system
resources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
