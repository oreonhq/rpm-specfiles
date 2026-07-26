%global source0_hash 43d29b785a7217ac27bc94ce1b1827eaaf0191a13c56162eb23b07bd3fccf9c5

%global base_name libkcddb

Name:    kf5-%{base_name}
Version: 23.08.5
Release: 5%{?dist}
Summary: CDDB retrieval library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://www.kde.org/applications/multimedia/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5WidgetsAddons)

BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)

BuildRequires: pkgconfig(libmusicbrainz5)

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package kcm
Summary:  KDE control module for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires:  %{name}-doc = %{version}-%{release}
%description kcm
%{summary}.

%package doc
Summary: Documentation for %{name}
License: GFDL
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name}-kcm --all-name --with-man
%find_lang %{name}-doc --all-name --with-html --without-mo

%files
%license LICENSES/*
%{_kf5_libdir}/libKF5Cddb.so.5*
%{_kf5_datadir}/qlogging-categories5/%{base_name}*

%files kcm -f %{name}-kcm.lang
%{_kf5_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_kf5_datadir}/applications/kcm_cddb.desktop
%{_kf5_datadir}/config.kcfg/libkcddb5.kcfg

%files devel
%{_kf5_libdir}/libKF5Cddb.so
%{_kf5_includedir}/KCddb/
%{_includedir}/KCddb5/
%{_kf5_libdir}/cmake/KF5Cddb/
%{_qt5_archdatadir}/mkspecs/modules/qt_KCddb.pri

%files doc -f %{name}-doc.lang

%changelog
%autochangelog
