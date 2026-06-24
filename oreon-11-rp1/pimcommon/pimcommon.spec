%global source0_hash none

Name:    pimcommon
Version: 26.04.2
Release: 1%{?dist}
Summary: PIM common libraries

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://api.kde.org/kdepim/pimcommon/html/

Source0:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextTemplate)

# Pim
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6LdapWidgets)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6AkonadiSearch)

# qt6
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(PlasmaActivities)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Obsoletes:      pimcommon-akonadi < 24.02.0-1
Conflicts:      pimcommon-akonadi < 24.02.0-1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6TextAutoCorrectionWidgets)
# akonadi
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiContactWidgets)
Requires:       cmake(KF6Contacts)
Requires:       cmake(KPim6IMAP)
Requires:       cmake(PlasmaActivities)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKPim6PimCommon.so.*
%{_kf6_libdir}/libKPim6PimCommonAkonadi.so.*
%{_kf6_libdir}/libKPim6PimCommonActivities.so.*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*

%files devel
%{_includedir}/KPim6/PimCommon/
%{_includedir}/KPim6/PimCommonActivities/
%{_includedir}/KPim6/PimCommonAkonadi/
%{_kf6_libdir}/libKPim6PimCommon.so
%{_kf6_libdir}/libKPim6PimCommonActivities.so
%{_kf6_libdir}/libKPim6PimCommonAkonadi.so
%{_kf6_libdir}/cmake/KPim6PimCommon/
%{_kf6_libdir}/cmake/KPim6PimCommonActivities/
%{_kf6_libdir}/cmake/KPim6PimCommonAkonadi/
%{_qt6_plugindir}/designer/pimcommon6widgets.so
%{_qt6_plugindir}/designer/pimcommon6akonadiwidgets.so

%files doc

%changelog
%autochangelog

