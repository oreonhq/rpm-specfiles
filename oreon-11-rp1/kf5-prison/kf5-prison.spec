%global framework prison 

Name:    kf5-%{framework}
Summary: KDE Frameworks 5 Tier 1 barcode library
Version: 5.116.0
Release: 5%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Quick)

BuildRequires:  cmake(ZXing)
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)

Requires: kf5-filesystem >= %{majmin}

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README* 
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Prison.so.5*
%{_kf5_libdir}/libKF5PrisonScanner.so.5*
%{_kf5_qmldir}/org/kde/prison/

%files devel
%{_kf5_includedir}/Prison/
%{_kf5_includedir}/PrisonScanner/
%{_kf5_libdir}/libKF5Prison.so
%{_kf5_libdir}/libKF5PrisonScanner.so
%{_kf5_libdir}/cmake/KF5Prison/
%{_kf5_archdatadir}/mkspecs/modules/qt_Prison.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
