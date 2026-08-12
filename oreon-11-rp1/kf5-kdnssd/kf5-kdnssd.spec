%global source0_hash 35676df6570a5019d723ccd92cb2bc141a35ff50b97244e4c0deef6e72f45dfc

%global framework kdnssd

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module for DNS-SD services (Zeroconf)

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
