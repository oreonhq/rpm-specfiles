%undefine __cmake_in_source_build
%global framework kwidgetsaddons

Name:           kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with various classes on top of QtWidgets

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 addon with various classes on top of QtWidgets.

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

%find_lang_kf5 kwidgetsaddons5_qt

%files -f kwidgetsaddons5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5WidgetsAddons.so.*
%{_kf5_datadir}/kf5/kcharselect/
%{_kf5_datadir}/qlogging-categories5/*categories

%files devel
%{_kf5_includedir}/KWidgetsAddons/
%{_kf5_libdir}/libKF5WidgetsAddons.so
%{_kf5_libdir}/cmake/KF5WidgetsAddons/
%{_kf5_archdatadir}/mkspecs/modules/qt_KWidgetsAddons.pri
%{_kf5_qtplugindir}/designer/kwidgetsaddons5widgets.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
