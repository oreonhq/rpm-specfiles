%global source1_hash ae0e101b6c0b856eda73fbf082233e822e4a411f931ec6e0ee3865c8f0b50c67

%global source0_hash 4fda64d235927e3cc230416d5c9304f5d3e040dc2553b77b2c69bf54c6f04862

%global framework purpose

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:    kf6-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 6.30.0
Release:        1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


# upstream patches

BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config) >= %{version}
BuildRequires: cmake(KF6CoreAddons) >= %{version}
BuildRequires: cmake(KF6I18n) >= %{version}
BuildRequires: cmake(KF6KIO) >= %{version}
BuildRequires: cmake(KF6Kirigami2) >= %{version}
BuildRequires: cmake(KF6Notifications) >= %{version}
BuildRequires: cmake(KAccounts6)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: accounts-qml-module-qt6
Requires:      accounts-qml-module-qt6
BuildRequires: cmake(KF6Declarative) >= %{version}
Requires:      kf6-kdeclarative
BuildRequires: cmake(KF6Prison) >= %{version}
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
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
%autochangelog
