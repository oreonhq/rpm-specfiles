%global source0_hash 4ceb62714637f02c80dfdcc7995f205f68930bc38ed5e503ef2e29a20016f5aa

Name:           itinerary
Version:        25.12.3
Release:        1%{?dist}
Summary:        Itinerary and boarding pass management application

License:        Apache-2.0 and BSD-3-Clause and LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/en-gb/itinerary/

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# Qt
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  qt6-qtbase-private-devel

# KDE Frameworks
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  kf6-qqc2-desktop-style

# KDE PIM
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6Itinerary)

# KDE Libraries
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOSMIndoorMap)
BuildRequires:  cmake(KHealthCertificate)
BuildRequires:  cmake(QuotientQt6)
BuildRequires:  cmake(QCoro6)

# Misc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

# Runtime requirements
Requires:       qt6-qtlocation
Requires:       qt6-qtmultimedia
Requires:       kf6-kitemmodels
Requires:       kf6-prison
Requires:       kf6-qqc2-desktop-style

%description
%summary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang kde-itinerary
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.itinerary.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f kde-itinerary.lang
%license LICENSES/*
%{_bindir}/itinerary
%{_libdir}/libSolidExtras.so
%{_qt6_plugindir}/kf6/kfilemetadata/kfilemetadata_itineraryextractor.so
%{_qt6_plugindir}/kf6/thumbcreator/itinerarythumbnail.so
%{_qt6_qmldir}/org/kde/solidextras/
%{_datadir}/applications/org.kde.itinerary.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.itinerary.svg
%{_datadir}/knotifications6/itinerary.notifyrc
%{_metainfodir}/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories6/org_kde_itinerary.categories

%changelog
%autochangelog
