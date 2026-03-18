%global framework knewstuff

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 module for downloading application assets

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-attica-devel >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kcompletion-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-kpackage-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-ktextwidgets-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-syndication-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel

%description
KDE Frameworks 5 Tier 3 module for downloading and sharing additional
application data like plugins, themes, motives, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-attica-devel >= %{majmin}
Requires:       kf5-kservice-devel >= %{majmin}
Requires:       kf5-kxmlgui-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_bindir}/knewstuff*
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_libdir}/libKF5NewStuff.so.*
%{_kf5_libdir}/libKF5NewStuffCore.so.*
%{_kf5_libdir}/libKF5NewStuffWidgets.so.*
%{_kf5_datadir}/kf5/kmoretools/
%{_kf5_datadir}/applications/org.kde.knewstuff-dialog.desktop
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/newstuff/

%files devel
%{_kf5_includedir}/KNewStuff3/
%{_kf5_includedir}/KMoreTools/
%{_kf5_libdir}/libKF5NewStuff.so
%{_kf5_libdir}/libKF5NewStuffCore.so
%{_kf5_libdir}/libKF5NewStuffWidgets.so
%{_kf5_libdir}/cmake/KF5NewStuff/
%{_kf5_libdir}/cmake/KF5NewStuffCore/
%{_kf5_libdir}/cmake/KF5NewStuffQuick/
%{_kf5_archdatadir}/mkspecs/modules/qt_KNewStuff.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KNewStuffCore.pri
%{_kf5_qtplugindir}/designer/knewstuffwidgets.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
