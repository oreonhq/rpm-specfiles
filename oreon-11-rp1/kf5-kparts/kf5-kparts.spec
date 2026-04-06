%undefine __cmake_in_source_build
%global framework kparts

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution for KParts

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-kconfig-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-ki18n-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kio-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kjobwidgets-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-knotifications-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kservice-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 3 solution for KParts

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kio-devel >= %{kf5_dl_majmin}
Requires:       kf5-ktextwidgets-devel >= %{kf5_dl_majmin}
Requires:       kf5-kxmlgui-devel >= %{kf5_dl_majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

# create/own parts plugin dir
mkdir -p %{buildroot}%{_kf5_plugindir}/parts/


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Parts.so.*
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_datadir}/kservicetypes5/*.desktop
# own plugin dir
%dir %{_kf5_plugindir}/parts/

%files devel

%{_kf5_includedir}/KParts/
%{_kf5_libdir}/libKF5Parts.so
%{_kf5_libdir}/cmake/KF5Parts/
%{_kf5_archdatadir}/mkspecs/modules/qt_KParts.pri
# 
%dir %{_kf5_datadir}/kdevappwizard/
%dir %{_kf5_datadir}/kdevappwizard/templates/
%{_kf5_datadir}/kdevappwizard/templates/kpartsapp.tar.bz2


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
