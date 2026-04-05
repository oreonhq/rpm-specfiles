%global         base_name oxygen

# Disable kf5 support for RHEL 10+
%bcond kf5 %[%{undefined rhel} || 0%{?rhel} < 10]


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-%{base_name}
Version: 6.6.2
Release:	2%{?dist}
Summary: Plasma and Qt widget style and window decorations for Plasma

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{base_name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig


# Misc
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  libxcb-devel
BuildRequires:  cmake(Plasma)

%if %{with kf5}
# Qt5
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
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
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6KirigamiPlatform)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

Requires:       kf6-filesystem

Requires:       %{name}-qt6

Requires:       oxygen-cursor-themes >= %{version}
Requires:       oxygen-sound-theme
# for oxygen look-and-feel
Requires:       oxygen-icon-theme

# kwin-oxygen was removed in 5.1.95
Obsoletes:      kwin-oxygen < 5.1.95-1
Obsoletes:      plasma-oxygen < 5.1.1-2
Conflicts:      plasma-desktop < 5.16.90

%description
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Oxygen widget style for Qt 5
Obsoletes:      qt5-style-oxygen < %{version}-%{release}
Provides:       qt5-style-oxygen = %{version}-%{release}
%description    qt5
%{summary}.
%endif

%package        qt6
Summary:        Oxygen widget style for Qt 6
%description    qt6
%{summary}.

%package -n     oxygen-cursor-themes
Summary:        Oxygen cursor themes
BuildArch:      noarch
Obsoletes:      plasma-oxygen-common < 5.1.1-2
%description -n oxygen-cursor-themes
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
pushd qt6build
%cmake_install_kf6
popd

%if %{with kf5}
pushd qt5build
%cmake_install_kf6
popd
%endif

%find_lang oxygen --with-qt --all-name


%files -f oxygen.lang
%license LICENSES/*
%{_bindir}/oxygen-settings6
%{_kf6_datadir}/applications/kcm_oxygendecoration.desktop
%{_kf6_datadir}/color-schemes/Oxygen.colors
%{_kf6_datadir}/color-schemes/OxygenCold.colors
%{_kf6_datadir}/icons/hicolor/*/apps/oxygen-settings.*
%{_kf6_datadir}/kstyle/themes/oxygen.themerc
%{_kf6_datadir}/plasma/look-and-feel/org.kde.oxygen/
%{_kf6_datadir}/plasma/desktoptheme/oxygen/
%{_kf6_qtplugindir}/kstyle_config/kstyle_oxygen_config.so
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_oxygendecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.oxygen.so

%if %{with kf5}
%files qt5
%{_bindir}/oxygen-demo5
%{_libdir}/liboxygenstyle5.so.*
%{_libdir}/liboxygenstyleconfig5.so.*
%{_kf5_qtplugindir}/styles/oxygen5.so
%endif

%files qt6
%{_bindir}/oxygen-demo6
%{_libdir}/liboxygenstyle6.so.*
%{_libdir}/liboxygenstyleconfig6.so.*
%{_kf6_qtplugindir}/styles/oxygen6.so

%files -n   oxygen-cursor-themes
%{_datadir}/icons/KDE_Classic/
%{_datadir}/icons/Oxygen_Black/
%{_datadir}/icons/Oxygen_Blue/
%{_datadir}/icons/Oxygen_White/
%{_datadir}/icons/Oxygen_Yellow/
%{_datadir}/icons/Oxygen_Zion/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
