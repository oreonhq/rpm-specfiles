%undefine __cmake_in_source_build
%global framework kitemviews

Name:           kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with item views

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0:        http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros >= %{kf5_dl_majmin}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem >= %{kf5_dl_majmin}

%description
KDE Frameworks 5 Tier 1 addon with item views.


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
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang_kf5 kitemviews5_qt

%files -f kitemviews5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5ItemViews.so.*
%{_kf5_datadir}/qlogging-categories5/*categories

%files devel
%{_kf5_includedir}/KItemViews/
%{_kf5_libdir}/libKF5ItemViews.so
%{_kf5_libdir}/cmake/KF5ItemViews/
%{_kf5_archdatadir}/mkspecs/modules/qt_KItemViews.pri
%{_kf5_qtplugindir}/designer/kitemviews5widgets.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
