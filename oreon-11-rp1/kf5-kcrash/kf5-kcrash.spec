%undefine __cmake_in_source_build
%global framework kcrash

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 2 addon for handling application crashes

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0:        http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

%description
KCrash provides support for intercepting and handling application crashes.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} \
  %{?fedora:-DKCRASH_CORE_PATTERN_RAISE:BOOL=OFF}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Crash.so.*

%files devel

%{_kf5_includedir}/KCrash/
%{_kf5_libdir}/libKF5Crash.so
%{_kf5_libdir}/cmake/KF5Crash/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCrash.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
