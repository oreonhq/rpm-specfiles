%global framework kconfigwidgets

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon for creating configuration dialogs

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz


BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kauth-devel >= %{majmin}
BuildRequires:  kf5-kcodecs-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

# KColorScheme requires color schemes to be installed
# https://pagure.io/fedora-workstation/issue/314
Requires:       plasma-breeze-common

BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake(Qt5UiPlugin)

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kauth-devel >= %{majmin}
Requires:       kf5-kcodecs-devel >= %{majmin}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kwidgetsaddons-devel >= %{majmin}
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

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_libdir}/libKF5ConfigWidgets.so.*
## fixme: %%lang'ify these -- rex
%{_kf5_datadir}/locale/*/kf5_entry.desktop

%files devel
%{_kf5_bindir}/preparetips5
%{_kf5_includedir}/KConfigWidgets/
%{_kf5_libdir}/libKF5ConfigWidgets.so
%{_kf5_libdir}/cmake/KF5ConfigWidgets/
%{_kf5_archdatadir}/mkspecs/modules/qt_KConfigWidgets.pri
%{_kf5_mandir}/man1/preparetips5.1*
%{_kf5_qtplugindir}/designer/kconfigwidgets5widgets.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
