
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kde-dev-utils
Summary: Utilities for developers using KDE
Version: 25.12.3
Release: 1%{?dist}

License: LGPL-2.0-only AND LGPL-3.0-only
URL:     https://invent.kde.org/sdk/%{name}.git

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires:  desktop-file-utils

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6UiTools)

Requires:       kpartloader = %{version}-%{release}
Requires:       kuiviewer = %{version}-%{release}

%description
Small utilities for developers using KDE/Qt libs/frameworks

%package common
Summary: Common files for %{name}
Conflicts: kdesdk-common < 4.10.80
# translations moved here
Conflicts: kde-l10n < 17.03
Obsoletes: kdesdk-devel < 4.10.80
Obsoletes: kdesdk-kmtrace < 4.10.80
Obsoletes: kdesdk-kmtrace-libs < 4.10.80
Obsoletes: kdesdk-kmtrace-devel < 4.10.80
Obsoletes: kdesdk-kstartperf < 4.10.80
Obsoletes: kde-dev-utils-devel < 17.03
Obsoletes: kde-dev-utils-kmtrace < 17.03
Obsoletes: kde-dev-utils-kmtrace-libs < 17.03
Obsoletes: kde-dev-utils-kmtrace-devel < 17.03
Obsoletes: kde-dev-utils-kstartperf < 17.03
BuildArch: noarch
%description common
%{summary}.

%package -n kpartloader
Summary: KPart loader
Obsoletes: kdesdk-kpartloader < 4.10.80
Obsoletes: kde-dev-utils-kpartloader < 17.03
Provides:  kde-dev-utils-kpartloader = %{version}-%{release}
Requires:  %{name}-common = %{version}-%{release}
%description -n kpartloader
%{summary}.

%package -n kuiviewer
Summary: Displays designer UI files 
Obsoletes: kdesdk-kuiviewer < 4.10.80
Obsoletes: kde-dev-utils-kuiviewer < 17.03
Provides:  kde-dev-utils-kuiviewer = %{version}-%{release}
Requires:  %{name}-common = %{version}-%{release}
%description -n kuiviewer 
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install

%find_lang kpartloader --with-html
%find_lang kuiviewer --with-html


%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.kuiviewer.desktop


%files
#empty metapackage

%files common
%license LICENSES/*

%files -n kpartloader -f kpartloader.lang
%{_kf6_bindir}/kpartloader

%files -n kuiviewer -f kuiviewer.lang
%{_kf6_bindir}/kuiviewer
%{_kf6_plugindir}/parts/kuiviewerpart.so
%{_kf6_datadir}/applications/org.kde.kuiviewer.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kuiviewer.*
%{_kf6_plugindir}/thumbcreator/quithumbnail.so
%{_kf6_metainfodir}/org.kde.kuiviewer.metainfo.xml
%{_kf6_metainfodir}/org.kde.kuiviewerpart.metainfo.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
