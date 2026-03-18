%undefine __cmake_in_source_build
%global framework kpeople

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 library for contact and people aggregation

License: CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

%description
KDE Frameworks 5 Tier 3 library for interaction with XML RPC services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5} \
    -DENABLE_EXAMPLES:BOOL=OFF
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}%{_kf5_qtplugindir}/kpeople/{actions,datasource,widgets}

%find_lang %{name} --all-name


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5People.so.*
%{_kf5_libdir}/libKF5PeopleWidgets.so.*
%{_kf5_libdir}/libKF5PeopleBackend.so.*
%{_kf5_qmldir}/org/kde/people/
%dir %{_kf5_qtplugindir}/kpeople/
%dir %{_kf5_qtplugindir}/kpeople/actions
%dir %{_kf5_qtplugindir}/kpeople/datasource
%dir %{_kf5_qtplugindir}/kpeople/widgets

%files devel
%{_kf5_includedir}/KPeople/
%{_kf5_libdir}/libKF5People.so
%{_kf5_libdir}/libKF5PeopleWidgets.so
%{_kf5_libdir}/libKF5PeopleBackend.so
%{_kf5_libdir}/cmake/KF5People/
%{_kf5_archdatadir}/mkspecs/modules/qt_KPeople.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KPeopleWidgets.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
