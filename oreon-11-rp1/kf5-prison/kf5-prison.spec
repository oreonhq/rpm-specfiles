%global source0_hash da9f3617a1be62832148e9d22152877ebc17d456f231f0f28d9083afda51f472

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
