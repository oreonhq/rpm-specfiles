%undefine __cmake_in_source_build
%global framework networkmanager-qt

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: A Tier 1 KDE Frameworks 5 module that wraps NetworkManager DBus API

License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  pkgconfig(libnm)

%if 0%{?fedora} > 22
Recommends:     NetworkManager
%else
Requires:       NetworkManager >= 0.9.9.0
%endif
Requires:       kf5-filesystem >= %{majmin}

%description
A Tier 1 KDE Frameworks 5 Qt library for NetworkManager.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       pkgconfig(libnm)
%description    devel
Qt libraries and header files for developing applications
that use NetworkManager.


%prep
%autosetup -p1 -n %{framework}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_datadir}/qlogging-categories5/*.categories
%{_kf5_libdir}/libKF5NetworkManagerQt.so.*

%files devel
%{_kf5_libdir}/libKF5NetworkManagerQt.so
%{_kf5_libdir}/cmake/KF5NetworkManagerQt/
%{_kf5_includedir}/NetworkManagerQt/

#{_kf5_archdatadir}/mkspecs/modules/qt_NetworkManagerQt.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
