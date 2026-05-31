%global source0_hash none

%global stable_kf6 stable


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ksystemstats
Version: 6.6.3
Release: 1%{?dist}
Summary: Plugin based system monitoring daemon for Plasma

License: BSD-2-Clause
URL:     https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  libksysguard-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  libnl3-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libcap)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  libdrm-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)

Requires:       kf6-filesystem
Requires:       lm_sensors-libs%{?_isa}

%description
KSystemStats is a plugin based system monitoring daemon used by Plasma for
CPU, memory, network, disk, power and GPU statistics.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/ksystemstats
%{_kf6_bindir}/kstatsviewer
%{_datadir}/dbus-1/services/org.kde.ksystemstats1.service
%{_userunitdir}/plasma-ksystemstats.service
%{_qt6_plugindir}/ksystemstats/
%caps(cap_perfmon=ep) %{_libexecdir}/ksystemstats_intel_helper
%{_kf6_datadir}/qlogging-categories6/ksystemstats.categories


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add ksystemstats package for Plasma system monitoring stack
