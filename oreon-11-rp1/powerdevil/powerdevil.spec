%global source1_hash 36268547e28189c0f647c59caa913eef1e52d14280bf11c9e80caf2338a2378a
%global source0_hash 6a738fccf01e4d1b10fea68ff8b404a406f95bc36fcb593bcc70fafb1c53258b
%global stable_kf6 stable
Name:    powerdevil
Version:        6.7.5
Release:        1%{?dist}
Summary:        Manages the power consumption settings of a Plasma Shell
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
%ifnarch s390 s390x
Requires:       ddcutil
%global DDCUTIL ON
%else
%global DDCUTIL OFF
%endif
Recommends: ppd-service
%if 0%{?fedora} && 0%{?fedora} < 41 || (0%{?oreon} >= 11)
Suggests: power-profiles-daemon
%else
Suggests: tuned-ppd
%endif
# oreon:deps
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libXrandr-devel
BuildRequires:  libcap-devel
BuildRequires:  libddcutil-devel
BuildRequires:  libkscreen-devel
BuildRequires:  libxcb-devel
BuildRequires:  plasma-workspace-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  wayland-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
# /oreon:deps
%description
Powerdevil is an utility for powermanagement. It consists
of a daemon (a KDED module) and a KCModule for its configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DHAVE_DDCUTIL=%DDCUTIL
%cmake_build
%install
%cmake_install
%find_lang powerdevil6 --with-html --all-name
rm -fv %{buildroot}/%{_libdir}/libpowerdevil{configcommonprivate,core,ui}.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.5-1
- Import
