Name:    plasma-disks
Summary: Hard disk health monitoring for KDE Plasma
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-only AND GPL-3.0-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kauth-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6KCMUtils)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core)

BuildRequires:  smartmontools
Requires:       smartmontools
BuildRequires:  desktop-file-utils

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

%description
Plasma Disks monitors S.M.A.R.T. data of disks and alerts the user when
signs of imminent failure appear.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_disks.desktop

%files -f %{name}.lang
%license LICENSES/*.txt
%{_libexecdir}/kf6/kauth/kded-smart-helper
%{_qt6_plugindir}/plasma/kcms/kinfocenter/kcm_disks.so
%{_kf6_plugindir}/kded/smart.so
%{_kf6_datadir}/applications/kcm_disks.desktop
%{_kf6_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kded.smart.conf
%{_kf6_datadir}/knotifications6/org.kde.kded.smart.notifyrc
%{_kf6_datadir}/metainfo/org.kde.plasma.disks.metainfo.xml
%{_kf6_datadir}/polkit-1/actions/org.kde.kded.smart.policy

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
