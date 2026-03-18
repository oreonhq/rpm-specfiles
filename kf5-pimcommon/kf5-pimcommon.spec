%global framework pimcommon

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: PIM common libraries

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://api.kde.org/kdepim/pimcommon/html/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  boost-devel

BuildRequires:  cmake(Grantlee5)
# kf5
%global kf5_ver 5.28
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
# qt5
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

# kde-apps
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-contacts-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-search-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kimap-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-kpimtextedit-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}

BuildRequires:  pkgconfig(libxslt)

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        akonadi
Summary:        The PimCommonAkondi runtime library
Obsoletes:      kf5-libkdepim-akonadi < 20.08.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description akonadi
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Config)
# This dependency should probably be fixed upstrea
# https://invent.kde.org/pim/pimcommon/-/issues/2
Requires:       cmake(KF5TextAutoCorrectionWidgets)
# akonadi
Requires:       %{name}-akonadi%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KPim5AkonadiContact)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5IMAP)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libpimcommon5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libpimcommon/libpimcommon5/" src/CMakeLists.txt
sed -i "s/libpimcommon/libpimcommon5/" src/Messages.sh


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5PimCommon.so.*
%{_kf5_libdir}/libKPim5PimCommonAkonadi.so.*
%{_qt5_plugindir}/designer/pimcommon5widgets.so

%ldconfig_scriptlets akonadi

%files akonadi
%{_qt5_plugindir}/designer/pimcommon5akonadiwidgets.so

%files devel
%{_kf5_libdir}/libKPim5PimCommon.so
%{_kf5_libdir}/libKPim5PimCommonAkonadi.so
%{_kf5_libdir}/cmake/KPim5PimCommon/
%{_kf5_libdir}/cmake/KPim5PimCommonAkonadi/
%{_includedir}/KPim5/PimCommon/
%{_includedir}/KPim5/PimCommonAkonadi/
%{_kf5_archdatadir}/mkspecs/modules/qt_PimCommon.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_PimCommonAkonadi.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
