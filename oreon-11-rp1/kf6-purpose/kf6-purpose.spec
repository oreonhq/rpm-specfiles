%global framework purpose

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 6.24.0
Release:	3%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# upstream patches

BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KAccounts6)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: accounts-qml-module-qt6
Requires:      accounts-qml-module-qt6
BuildRequires: cmake(KF6Declarative)
Requires:      kf6-kdeclarative
BuildRequires: cmake(KF6Prison)
Requires:      kf6-prison
BuildRequires: kf6-kitemmodels
Requires:      qt6qml(org.kde.kitemmodels)


Requires: hicolor-icon-theme
Requires: kf6-bluez-qt >= %{version}

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF6CoreAddons)
%description devel
%{summary}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Purpose.so.6
%{_kf6_libdir}/libKF6Purpose.so.%{version}
%{_kf6_libdir}/libKF6PurposeWidgets.so.6
%{_kf6_libdir}/libKF6PurposeWidgets.so.%{version}
%{_kf6_libexecdir}/purposeprocess
%{_kf6_datadir}/kf6/purpose/
%{_kf6_datadir}/accounts/services/kde/*.service
%{_kf6_plugindir}/purpose/
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf6_qmldir}/org/kde/purpose/
%{_datadir}/icons/hicolor/*/apps/*-purpose6.*

%files devel
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/cmake/KF6Purpose/

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
