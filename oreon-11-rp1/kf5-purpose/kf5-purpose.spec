%global  framework purpose

Name:    kf5-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 5.116.0
Release: 5%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: https://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

Obsoletes:  kf5-purpose-twitter < 5.68.0

## downstream patches
# src/quick/CMakeLists.txt calls 'cmake' directly, use 'cmake3' instead (mostly for epel7)
%if 0%{?rhel} && 0%{?rhel} < 8
Patch100: purpose-5.79.0-cmake3.patch
%endif

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$

BuildRequires: extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires: gettext
BuildRequires: intltool

BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfig-devel >= %{kf5_dl_majmin}
BuildRequires: kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires: kf5-ki18n-devel >= %{kf5_dl_majmin}
BuildRequires: kf5-kio-devel >= %{kf5_dl_majmin}
BuildRequires: kf5-kirigami2-devel >= %{kf5_dl_majmin}
Requires: kf5-bluez-qt >= %{kf5_dl_majmin}

BuildRequires: cmake(KF5Kirigami2)

# optional sharefile plugin
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)

BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: kaccounts-integration-devel

BuildRequires: pkgconfig(accounts-qt5)
BuildRequires: pkgconfig(libaccounts-glib)
%endif

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF5CoreAddons)
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

## unpackaged files
# omit (unused?) conflicting icons with older kamoso (rename to "google-youtube"?)
rm -fv %{buildroot}%{_datadir}/icons/hicolor/*/actions/kipiplugin_youtube.png


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Purpose.so.5*
%{_kf5_libdir}/libKF5PurposeWidgets.so.5*
%{_kf5_libdir}/libPhabricatorHelpers.so.5*
%{_kf5_libdir}/libReviewboardHelpers.so.5*
%{_kf5_libexecdir}/purposeprocess
%{_kf5_datadir}/purpose/
%{_kf5_plugindir}/purpose/
%dir %{_kf5_plugindir}/kfileitemaction/
%{_kf5_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf5_qmldir}/org/kde/purpose/
# this conditional may require adjusting too (e.g. wrt %%twitter)
%if 0%{?fedora} || 0%{?rhel} > 7
%{_kf5_datadir}/accounts/services/kde/google-youtube.service
%{_kf5_datadir}/accounts/services/kde/nextcloud-upload.service
%endif
%{_datadir}/icons/hicolor/*/apps/*-purpose.*
#{_datadir}/icons/hicolor/*/actions/google-youtube.*

%files devel
%{_kf5_libdir}/libKF5Purpose.so
%{_kf5_libdir}/libKF5PurposeWidgets.so
%{_kf5_includedir}/purpose/
%{_kf5_includedir}/purposewidgets/
%{_kf5_libdir}/cmake/KDEExperimentalPurpose/
%{_kf5_libdir}/cmake/KF5Purpose/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
