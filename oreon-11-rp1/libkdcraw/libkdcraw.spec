%global stable_kf6 stable

Name:    libkdcraw
Summary: A C++ interface around LibRaw library
Version: 25.12.3
Release: 4%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


## upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: cmake(Qt6Gui)
BuildRequires: pkgconfig(libraw) >= 0.15

Requires: kf6-filesystem

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install


%files
%doc AUTHORS
%license LICENSES/*
%{_kf6_libdir}/libKDcrawQt6.so.*
%{_kf6_datadir}/qlogging-categories6/*

%files devel
%{_kf6_libdir}/libKDcrawQt6.so
%{_includedir}/KDcrawQt6/
%{_kf6_libdir}/cmake/KDcrawQt6/


%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-4
- Rebuild

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-3
- Rebuild for LibRaw SONAME

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-2
- Import from Fedora 43 SRPM libkdcraw-25.12.3-1.fc43
