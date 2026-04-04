%global framework ksvg
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-ksvg
Summary: Components for handling SVGs
Version: 6.24.0
Release:	5%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules >= %{version}

BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Svg)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6ColorScheme)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{framework}-%{version}

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%license LICENSES/*
%{_kf6_libdir}/libKF6Svg.so.*
%{_kf6_libdir}/qt6/qml/org/kde/ksvg
%{_kf6_datadir}/qlogging-categories6/ksvg.categories

%files devel
%{_kf6_includedir}/KSvg
%{_kf6_libdir}/cmake/KF6Svg
%{_kf6_libdir}/libKF6Svg.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

