%global framework attica

Name:   kf5-attica
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks Tier 1 Addon with Open Collaboration Services API

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  qt5-qtbase-devel

Requires: kf5-filesystem >= %{majmin}

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version}


%build
%cmake_kf5
%cmake_build


%install
%cmake_install


%files
%doc AUTHORS ChangeLog README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5Attica.so.*
%{_kf5_datadir}/qlogging-categories5/%{framework}.*

%files devel
%{_kf5_includedir}/Attica/
%{_kf5_libdir}/libKF5Attica.so
%{_kf5_libdir}/cmake/KF5Attica/
%{_kf5_libdir}/pkgconfig/libKF5Attica.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_Attica.pri

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
