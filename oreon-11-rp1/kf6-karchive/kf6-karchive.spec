%global framework karchive

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	2%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with archive functions
License:        LGPL-2.0-or-later AND BSD-2-Clause
URL:            https://invent.kde.org/frameworks/%{framework}
Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros

# KDE Frameworks
BuildRequires:  extra-cmake-modules

# Qt
BuildRequires:  cmake(Qt6Core)

# Compression
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

# Others
BuildRequires:  pkgconfig(openssl)

%description
KDE Frameworks 6 Tier 1 addon with archive functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
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

%find_lang_kf6 karchive6_qt

%files -f karchive6_qt.lang
%doc AUTHORS README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Archive.so.6
%{_kf6_libdir}/libKF6Archive.so.%{version}

%files devel
%{_kf6_includedir}/KArchive/
%{_kf6_libdir}/cmake/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
