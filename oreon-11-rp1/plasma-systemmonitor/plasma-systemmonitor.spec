
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-systemmonitor
Version: 6.6.2
Release:	2%{?dist}
Summary: An application for monitoring system resources

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

## upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6NewStuff)
# runtime
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: ksystemstats

BuildRequires: libksysguard-devel

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel

# runtime
Requires: kf6-kirigami%{?_isa}
Requires: kf6-kirigami-addons%{?_isa}
Requires: kf6-kiconthemes%{?_isa}
Requires: ksystemstats%{?_isa}

Obsoletes: ksysguard < 5.23

%description
An interface for monitoring system sensors, process information and other system
resources.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*.txt
%{_bindir}/plasma-systemmonitor
%{_datadir}/applications/org.kde.plasma-systemmonitor.desktop
%{_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_kf6_datadir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop
%{_kf6_datadir}/knsrcfiles/
%{_kf6_datadir}/metainfo/org.kde.plasma-systemmonitor.metainfo.xml
%{_kf6_datadir}/ksysguard/sensorfaces/
%{_kf6_datadir}/plasma-systemmonitor/
%{_kf6_qmldir}/org/kde/ksysguard/
%{_libdir}/libPlasmaSystemMonitorPage.so
%{_libdir}/libPlasmaSystemMonitorTable.so
%{_kf6_datadir}/kconf_update/plasma-systemmonitor*

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
