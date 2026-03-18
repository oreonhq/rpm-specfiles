%global framework kdnssd

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module for DNS-SD services (Zeroconf)

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  avahi-devel
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       nss-mdns
Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 integration module for DNS-SD services (Zeroconf)

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

%find_lang_kf5 kdnssd5_qt


%ldconfig_scriptlets

%files -f kdnssd5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5DNSSD.so.*

%files devel
%{_kf5_includedir}/KDNSSD/

%{_kf5_libdir}/libKF5DNSSD.so
%{_kf5_libdir}/cmake/KF5DNSSD/
%{_kf5_archdatadir}/mkspecs/modules/qt_KDNSSD.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
