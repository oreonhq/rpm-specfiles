%global source0_hash 27cfb9a189244b897ae23f3a8681e7c4b45cc67ec27faff8961783edce16f1fc
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    ksystemstats
Version:        6.7.5
Release:        1%{?dist}
Summary:        Plugin based system monitoring daemon for Plasma
License: BSD-2-Clause
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Requires:       kf6-filesystem
Requires:       lm_sensors-libs%{?_isa}
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libdrm-devel
BuildRequires:  libksysguard-devel
BuildRequires:  libnl3-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libcap)
BuildRequires:  systemd-devel
# /oreon:deps
%description
KSystemStats is a plugin based system monitoring daemon used by Plasma for
CPU, memory, network, disk, power and GPU statistics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add ksystemstats package for Plasma system monitoring stack
