%undefine __cmake_in_source_build
%global framework kxmlgui

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution for user-configurable main windows

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-attica-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kglobalaccel-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-ktextwidgets-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(Qt5UiPlugin)

%description
KDE Frameworks 5 Tier 3 solution for user-configurable main windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kconfigwidgets-devel >= %{majmin}
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

# Own the kxmlgui directory
mkdir -p %{buildroot}%{_kf5_datadir}/kxmlgui5/

%find_lang %{name} --all-name


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%dir %{_kf5_sysconfdir}/xdg/ui/
%config %{_kf5_sysconfdir}/xdg/ui/ui_standards.rc
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5XmlGui.so.*
%{_kf5_libexecdir}/ksendbugmail
%dir %{_kf5_datadir}/kxmlgui5/
%{_kf5_qtplugindir}/designer/*5widgets.so

%files devel

%{_kf5_includedir}/KXmlGui/
%{_kf5_libdir}/libKF5XmlGui.so
%{_kf5_libdir}/cmake/KF5XmlGui/
%{_kf5_archdatadir}/mkspecs/modules/qt_KXmlGui.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
