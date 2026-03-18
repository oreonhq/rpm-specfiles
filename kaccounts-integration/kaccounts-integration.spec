# EPEL10 does not have kf5
%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with kf5
%else
%bcond_without kf5
%endif

Name:    kaccounts-integration
Version: 25.12.3
Release: 1%{?dist}
Summary: Small system to administer web accounts across the KDE desktop
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/network/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream fixes

## upstreamable fixes

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-kdeclarative-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kwallet-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  cmake(QCoro6)

BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)

BuildRequires:  pkgconfig(accounts-qt6)
BuildRequires:  pkgconfig(libaccounts-glib) >= 1.21
BuildRequires:  cmake(SignOnQt6)

%if %{with kf5}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  cmake(QCoro5)

BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  pkgconfig(accounts-qt5)
BuildRequires:  cmake(SignOnQt5)
%endif

# For AutoReq cmake-filesystem
BuildRequires:  cmake

%description
Small system to administer web accounts for the sites and services
across the KDE desktop.

%if %{with kf5}
%package        qt5
Summary:        qt5 runtime for %{name}
Obsoletes:      kaccounts < 15.03
Provides:       kaccounts = %{version}-%{release}
Obsoletes:      kaccounts-integration < 24.01.75
Provides:       kaccounts-integration = %{version}-%{release}
# translations moved here
Conflicts: kde-l10n < 17.03

%description    qt5
Small system to administer web accounts for the sites and services
across the KDE desktop.

%package        qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt5Widgets)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(AccountsQt5)
Requires:       cmake(SignOnQt5)
Requires:       pkgconfig(libaccounts-glib)
Requires:       intltool
Obsoletes:      kaccounts-integration-devel < 24.01.75
Provides:       kaccounts-integration-devel = %{version}-%{release}

%description    qt5-devel
Headers, development libraries and documentation for %{name}.
%endif

%package        qt6
Summary:        qt6 runtime for %{name}

%description    qt6
Small system to administer web accounts for the sites and services
across the KDE desktop.

%package        qt6-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(AccountsQt6)
Requires:       cmake(SignOnQt6)
Requires:       pkgconfig(libaccounts-glib)
Requires:       intltool

%description    qt6-devel
Headers, development libraries and documentation for %{name}.



%prep
%autosetup -p1


%build
mkdir %{name}_qt6
pushd %{name}_qt6
%cmake_kf6 -S ..
%cmake_build
popd

%if %{with kf5}
mkdir %{name}_qt5
pushd %{name}_qt5
%cmake_kf5 -DKF6_COMPAT_BUILD=ON -S ..
%cmake_build
popd
%endif

%install
pushd %{name}_qt6
%cmake_install
popd
%find_lang %{name} --all-name --with-html

%if %{with kf5}
pushd %{name}_qt5
%cmake_install
popd
%endif

%files qt6 -f %{name}.lang
%doc README*
%license LICENSES/*
%{_kf6_datadir}/applications/kcm_kaccounts.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_kaccounts.so
%{_kf6_plugindir}/kded/kded_accounts.so
%dir %{_qt6_plugindir}/kaccounts/daemonplugins
%{_qt6_plugindir}/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
%{_kf6_libdir}/libkaccounts6.so.*
%{_kf6_qmldir}/org/kde/kaccounts/
%{_kf6_datadir}/qlogging-categories6/kaccounts.categories

%files qt6-devel
%{_kf6_libdir}/libkaccounts6.so
%{_kf6_libdir}/cmake/KAccounts6/
%{_includedir}/KAccounts6/

%if %{with kf5}
%files qt5
%doc README*
%license LICENSES/*
%{_kf5_libdir}/libkaccounts.so.*
%{_kf5_qmldir}/org/kde/kaccounts/
%{_kf5_datadir}/qlogging-categories5/kaccounts.categories

%files qt5-devel
%{_kf5_libdir}/libkaccounts.so
%{_kf5_libdir}/cmake/KAccounts/
%{_includedir}/KAccounts/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
