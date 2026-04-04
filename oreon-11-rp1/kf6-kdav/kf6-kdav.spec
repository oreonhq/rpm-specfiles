%global framework kdav

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	2%{?dist}
Summary: A DAV protocol implementation with KJobs

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Gui)

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
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

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6DAV.so.6
%{_kf6_libdir}/libKF6DAV.so.%{version}

%files devel
%{_kf6_includedir}/KDAV/
%{_kf6_libdir}/libKF6DAV.so
%{_kf6_libdir}/cmake/KF6DAV/

%changelog
* Fri Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
