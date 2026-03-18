%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global framework plasma-framework

Name:    kf5-plasma
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 framework is foundation to build a primary user interface

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/plasma

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# hackish cache invalidation
# upstream has worked on this issue recently (.31 or .32?) so may consider dropping this -- rex
Source10: fedora-plasma-cache.sh.in

## upstream patches

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kactivities-devel >= %{majmin}
BuildRequires:  kf5-kactivities-devel >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kdeclarative-devel >= %{majmin}
BuildRequires:  kf5-kdesu-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-kglobalaccel-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-knotifications-devel >= %{majmin}
BuildRequires:  kf5-kpackage-devel >= %{majmin}
BuildRequires:  kf5-kparts-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kirigami2-devel >= %{majmin}
BuildRequires:  kf5-kwayland-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-solid-devel >= %{majmin}
BuildRequires:  libGL-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  openssl-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel

Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}

# https://bugzilla.redhat.com/1293415
Conflicts:      kdeplasma-addons < 5.5.0-3

# upstream name
# used by the plasma-framework package in Plasma 6
%if %{without kf6_compat}
Provides: plasma-framework = %{version}-%{release}
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
# https://bugzilla.redhat.com/1292506
Conflicts:      kapptemplates < 15.12.0-1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kpackage-devel >= %{majmin}
Requires:       kf5-kservice-devel >= %{majmin}
Requires:       kf5-kwindowsystem-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%if %{without kf6_compat}
Provides: plasma-framework-devel = %{version}-%{release}
%endif
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1

install -m644 -p %{SOURCE10} .


%build
%cmake_kf5 %{?with_kf6_compat:-DBUILD_DESKTOPTHEMES=OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-man --all-name

# create/own dirs
mkdir -p %{buildroot}%{_kf5_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf5_qmldir}/org/kde/private

mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env
sed -e "s|@@VERSION@@|%{version}|g" fedora-plasma-cache.sh.in > \
  %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/fedora-plasma-cache.sh


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_sysconfdir}/xdg/plasma-workspace/env/fedora-plasma-cache.sh
%{_kf5_bindir}/plasmapkg2
%{_kf5_libdir}/libKF5Plasma.so.*
%{_kf5_libdir}/libKF5PlasmaQuick.so.*
%{_kf5_datadir}/qlogging-categories5/*plasma*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/private/
%{_kf5_qmldir}/org/kde/plasma/
%{_kf5_qmldir}/org/kde/kirigami.2/styles
%{_kf5_qmldir}/QtQuick/Controls/Styles/Plasma/
%{_kf5_qmldir}/QtQuick/Controls.2/Plasma/
%{_kf5_qtplugindir}/plasma/
%{_kf5_qtplugindir}/kpackage/packagestructure/*.so
%{_kf5_plugindir}/kirigami/
%{_kf5_datadir}/plasma/
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man1/plasmapkg2.1.*

%files devel
%{_kf5_libdir}/cmake/KF5Plasma/
%{_kf5_libdir}/cmake/KF5PlasmaQuick/
%{_kf5_libdir}/libKF5Plasma.so
%{_kf5_libdir}/libKF5PlasmaQuick.so

%{_kf5_includedir}/plasma/
%{_kf5_includedir}/Plasma/
%{_kf5_includedir}/PlasmaQuick/
%{_kf5_includedir}/plasmaquick/
%dir %{_kf5_datadir}/kdevappwizard/
%{_kf5_datadir}/kdevappwizard/templates/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
