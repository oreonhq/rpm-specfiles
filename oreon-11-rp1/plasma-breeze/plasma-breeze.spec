%global  base_name breeze
# EPEL10 does not have kf5
%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with kf5
%else
%bcond_without kf5
%endif

Name:    plasma-breeze
Version: 6.6.2
Release:	2%{?dist}
Summary: Artwork, styles and assets for the Breeze visual style for the Plasma Desktop

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{base_name}.git
Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

# Misc
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext

%if %{with kf5}
# Qt5
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)

Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif

# Qt6
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)

Requires:       %{name}-qt6

# since we provide a cmake dev-like file
Provides:       %{name}-devel = %{version}-%{release}

%description
%{summary}.


%package        qt6
Summary:        Breeze application style for Qt6
Requires:       %{name}-common = %{version}-%{release}
%description    qt6
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Breeze application style for Qt5
Requires:       %{name}-common = %{version}-%{release}
%description    qt5
%{summary}.
%endif

%package        common
Summary:        Common files shared between Plasma 5 and Plasma 6 versions of the Breeze style
BuildArch:      noarch
%description    common
%{summary}.

%package -n     breeze-cursor-theme
Summary:        Breeze cursor theme
BuildArch:      noarch
Obsoletes:      breeze-icon-theme < 5.17.0
Provides:       breeze-cursor-themes = %{version}-%{release}
%description -n breeze-cursor-theme
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
mkdir -p qt6build
pushd qt6build
%cmake_kf6 -S .. -DBUILD_QT6=ON -DBUILD_QT5=OFF
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
popd

%if %{with kf5}
mkdir -p qt5build
pushd qt5build
%cmake_kf5 -S .. -DBUILD_QT6=OFF -DBUILD_QT5=ON
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
popd
%endif


%install
%if %{with kf5}
pushd qt5build
%cmake_install_kf6
popd
%endif

pushd qt6build
%cmake_install_kf6
popd

%find_lang breeze --all-name


%files -f breeze.lang
%license LICENSES/*.txt
%{_bindir}/breeze-settings6
%{_bindir}/kcursorgen
%{_kf6_datadir}/applications/breezestyleconfig.desktop
%{_kf6_datadir}/applications/kcm_breezedecoration.desktop
%dir %{_kf6_qtplugindir}/kstyle_config/
%{_kf6_qtplugindir}/kstyle_config/breezestyleconfig.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_breezedecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.breeze.so
%{_libdir}/cmake/Breeze/

%if %{with kf5}
%files qt5
%{_kf5_qtplugindir}/styles/breeze5.so
%endif

%files qt6
%{_kf6_qtplugindir}/styles/breeze6.so

%files common
%{_datadir}/color-schemes/*.colors
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/icons/hicolor/*/apps/breeze-settings.*
%dir %{_datadir}/QtCurve/
%{_datadir}/QtCurve/Breeze.qtcurve
%{_datadir}/wallpapers/Next/

%files -n breeze-cursor-theme
%dir %{_kf6_datadir}/icons/Breeze_Light/
%{_kf6_datadir}/icons/Breeze_Light/cursors/
%{_kf6_datadir}/icons/Breeze_Light/cursors_scalable/
%{_kf6_datadir}/icons/Breeze_Light/index.theme
%dir %{_kf6_datadir}/icons/breeze_cursors/
%{_kf6_datadir}/icons/breeze_cursors/cursors/
%{_kf6_datadir}/icons/breeze_cursors/cursors_scalable/
%{_kf6_datadir}/icons/breeze_cursors/index.theme

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
