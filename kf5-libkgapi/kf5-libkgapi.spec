%global srcname libkgapi

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# https://bugzilla.redhat.com/show_bug.cgi?id=1895674
%global _lto_cflags %{nil}

Name:    kf5-libkgapi
Version: 23.08.5
Release: 5%{?dist}
Summary: Library to access to Google services

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/pim/%{srcname}

Source0: https://download.kde.org/stable/release-service/%{version}/src/%{srcname}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qttools-static

BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kwindowsystem-devel

BuildRequires:  kf5-kcalendarcore-devel >= %{version}
BuildRequires:  kf5-kcontacts-devel >= %{version}

BuildRequires:  cyrus-sasl-devel

%description
Library to access to Google services, this package is needed by kdepim-runtime
to build akonadi-google resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kcalendarcore-devel
Requires:       kf5-kcontacts-devel
%description devel
Libraries and header files for developing applications that use akonadi-google
resources.


%prep
%autosetup -n %{srcname}-%{version}


%build
find ./poqm -type f -execdir mv {} libkgapi_qt5.po \;
sed -i "/ecm_create_qm_loader/ s/libkgapi_qt/libkgapi_qt5/" src/core/CMakeLists.txt
sed -i "/EXTRACT_TR_STRINGS/ s/libkgapi_qt/libkgapi_qt5/" Messages.sh

%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang_kf5 libkgapi_qt5

# Remove unpackaged files
rm %{buildroot}%{_libdir}/sasl2/libkdexoauth2.so*


%files -f libkgapi_qt5.lang
%doc README*
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{srcname}.*
%{_kf5_libdir}/libKPim5GAPIBlogger.so.5*
%{_kf5_libdir}/libKPim5GAPICalendar.so.5*
%{_kf5_libdir}/libKPim5GAPICore.so.5*
%{_kf5_libdir}/libKPim5GAPIDrive.so.5*
%{_kf5_libdir}/libKPim5GAPILatitude.so.5*
%{_kf5_libdir}/libKPim5GAPIMaps.so.5*
%{_kf5_libdir}/libKPim5GAPIPeople.so.5*
%{_kf5_libdir}/libKPim5GAPITasks.so.5*

%files devel
%{_kf5_libdir}/libKPim5GAPIPeople.so
%{_kf5_libdir}/libKPim5GAPIBlogger.so
%{_kf5_libdir}/libKPim5GAPICalendar.so
%{_kf5_libdir}/libKPim5GAPICore.so
%{_kf5_libdir}/libKPim5GAPIDrive.so
%{_kf5_libdir}/libKPim5GAPILatitude.so
%{_kf5_libdir}/libKPim5GAPIMaps.so
%{_kf5_libdir}/libKPim5GAPITasks.so
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPIBlogger.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPICalendar.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPICore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPIDrive.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPILatitude.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPIMaps.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPITasks.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGAPIPeople.pri
%{_kf5_libdir}/cmake/KPimGAPI/
%{_kf5_libdir}/cmake/KPim5GAPI/
%dir %{_includedir}/KPim5/
%{_includedir}/KPim5/KGAPI/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
