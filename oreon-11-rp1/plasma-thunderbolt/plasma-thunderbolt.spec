%global base_name    plasma-thunderbolt


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-thunderbolt
Summary: Plasma integration for controlling Thunderbolt devices
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Notifications)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  desktop-file-utils

Requires:       bolt

%description
Plasma Sytem Settings module and a KDED module to handle authorization of
Thunderbolt devices connected to the computer. There's also a shared library
(libkbolt) that implements common interface between the modules and the
system-wide bolt daemon, which does the actual hard work of talking to the
kernel.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_bolt.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libkbolt.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_bolt.so
%{_kf6_qtplugindir}/kf6/kded/kded_bolt.so
%{_kf6_datadir}/knotifications6/kded_bolt.notifyrc
%{_kf6_datadir}/applications/kcm_bolt.desktop

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
