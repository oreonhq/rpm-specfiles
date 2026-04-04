%global framework kconfigwidgets

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	5%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for creating configuration dialogs

# The following licenses are in LICENSES but go unused: BSD-3-Clause, MIT
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  pkgconfig(xkbcommon)

Requires:  kf6-filesystem

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kauth-devel
Requires:       kf6-kcodecs-devel
Requires:       cmake(KF6ColorScheme)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6WidgetsAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6ConfigWidgets.so.*
%{_datadir}/locale/*/kf6_entry.desktop
%{_kf6_datadir}/qlogging-categories6/%{framework}*

%files devel
%{_kf6_includedir}/KConfigWidgets/
%{_kf6_libdir}/libKF6ConfigWidgets.so
%{_kf6_libdir}/cmake/KF6ConfigWidgets/
%{_kf6_libdir}/qt6/plugins/designer/kconfigwidgets6widgets.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

