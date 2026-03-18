%global base_name libkdcraw

Name:    kf5-libkdcraw
Summary: A C++ interface around LibRaw library
Version: 23.08.5
Release: 6%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{base_name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

#Patch0: libraw.patch
#Fixed upstream @ https://invent.kde.org/graphics/libkdcraw/-/commit/0843c601cbb9a9bb5774ed01b7d90e68fd17950a

%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le %{arm}
%endif

## upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig(libraw) >= 0.15
BuildRequires: cmake(Qt5Gui)

Requires: kf5-filesystem

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
%description devel
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc AUTHORS
%license LICENSES/*
%{_kf5_libdir}/libKF5KDcraw.so.5*
%{_kf5_datadir}/qlogging-categories5/*%{base_name}.*

%files devel
%{_kf5_libdir}/libKF5KDcraw.so
%{_kf5_includedir}/KDCRAW/
%{_kf5_libdir}/cmake/KF5KDcraw/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-6
- Prepare for Oreon 11 (RP1)
