%global source1_hash 909225848faa9c113117a2b1d8a6ccfef711eb018663befa3f6890b4b4d1e2da

%global source0_hash 6d59a98f58c66842d29fd7a00e07e0f74e375061aabdfb4c52bbe3140c278225

%global		framework kdnssd

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module for DNS-SD services (Zeroconf)
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	avahi-devel
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	nss-mdns
Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 integration module for DNS-SD services (Zeroconf)

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 kdnssd6_qt

%files -f kdnssd6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6DNSSD.so.*

%files devel
%{_kf6_includedir}/KDNSSD/
%{_kf6_libdir}/libKF6DNSSD.so
%{_kf6_libdir}/cmake/KF6DNSSD/


%changelog
%autochangelog
