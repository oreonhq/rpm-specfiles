%global framework libksieve


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 23.08.5
Release: 6%{?dist}
Summary: Sieve support library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  cmake(KF5TextEditTextToSpeech)

%global kf5_ver 5.23.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}
BuildRequires:  kf5-karchive-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_ver}
BuildRequires:  kf5-knewstuff-devel >= %{kf5_ver}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_ver}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-kwindowsystem-devel >= %{kf5_ver}
BuildRequires:  kf5-syntax-highlighting-devel >= %{kf5_ver}

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-contacts-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  kf5-kmailtransport-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-kpimtextedit-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5SyntaxHighlighting)
%description    devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libksieve5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libksieve/libksieve5/" src/CMakeLists.txt
sed -i "s/libksieve/libksieve5/" src/Messages.sh


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/knsrcfiles/ksieve_script.knsrc
%{_kf5_datadir}/sieve/

%files libs
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5KManageSieve.so.*
%{_kf5_libdir}/libKPim5KSieve.so.*
%{_kf5_libdir}/libKPim5KSieveUi.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_KManageSieve.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KSieveUi.pri
%{_includedir}/KPim5/KManageSieve/
%{_includedir}/KPim5/KSieveUi/
%{_kf5_includedir}/KSieve/libksieve_version.h
%{_kf5_libdir}/cmake/KPim5LibKSieve/
%{_kf5_libdir}/libKPim5KManageSieve.so
%{_kf5_libdir}/libKPim5KSieve.so
%{_kf5_libdir}/libKPim5KSieveUi.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-6
- Prepare for Oreon 11 (RP1)
