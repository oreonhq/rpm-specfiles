%global framework knewstuff

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	2%{?dist}
Summary: KDE Frameworks 6 Tier 3 module for downloading application assets
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Attica)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Syndication)
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 3 module for downloading and sharing additional
application data like plugins, themes, motives, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Attica)
Requires:       cmake(KF6Service)
Requires:       cmake(KF6XmlGui)
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
    -DQDOC_BIN=/bin/true
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --all-name

%files -f %{name}.lang
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/knewstuff*
%{_kf6_datadir}/applications/org.kde.knewstuff-dialog6.desktop
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6NewStuffCore.so.*
%{_kf6_libdir}/libKF6NewStuffWidgets.so.*
%{_kf6_qmldir}/org/kde/newstuff/

%files devel
%{_kf6_includedir}/KNewStuff
%{_kf6_includedir}/KNewStuffCore
%{_kf6_includedir}/KNewStuffWidgets
%{_kf6_libdir}/cmake/KF6NewStuff/
%{_kf6_libdir}/cmake/KF6NewStuffCore/
%{_kf6_libdir}/libKF6NewStuffCore.so
%{_kf6_libdir}/libKF6NewStuffWidgets.so
%{_kf6_libdir}/qt6/plugins/designer/knewstuff6widgets.so

%changelog
* Fri Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
