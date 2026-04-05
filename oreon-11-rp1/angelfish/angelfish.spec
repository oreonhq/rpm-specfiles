# adblock requires rust and corrosion
%bcond adblock 1

Name:           angelfish
Version:        25.12.3
Release:	2%{?dist}
Summary:        Plasma Mobile minimal web browser

# Cargo license summary:
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
# Automatically converted from old format: MIT and GPLv2+ and LGPLv2 and LGPLv2+ AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) - review is highly recommended.
License:        MIT AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/network/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(FutureSQL6)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Quick)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QmlPrivate)
BuildRequires:  cmake(Qt6CorePrivate)

%if %{with adblock}
BuildRequires:  cmake(Corrosion)
BuildRequires:  rust-packaging
%endif

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-purpose%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtwayland%{?_isa}
Requires:       qt6-qtwebengine%{?_isa}

%description
Web browser for mobile devices with Plasma integration

%prep
%autosetup -n %{name}-%{version} -p1
%if %{with adblock}
%cargo_prep
%endif

%if %{with adblock}
%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%if %{with adblock}
# Rust dependency handling
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%endif

%install
%cmake_install_kf6
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/{MIT,GPL-2.0-or-later,LGPL-2.0-only,LGPL-2.0-or-later}.txt
%if %{with adblock}
%license LICENSE.dependencies
%endif
%doc README.md

%{_kf6_bindir}/%{name}
%{_kf6_bindir}/%{name}-webapp

%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/%{name}settings.kcfg
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/knotifications6/%{name}.notifyrc

%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
