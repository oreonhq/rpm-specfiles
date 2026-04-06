%global framework kcalendarcore

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-kcalendarcore
Epoch:   1
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 KCalendarCore Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

# libical (and thus kcalendarcore) not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: make
BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  bison
BuildRequires:  libical-devel

BuildRequires:  qt5-qtbase-devel

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libical-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

## TODO: poke upstream about failures seen on f30
#The following tests FAILED:
#         39 - testicaltimezones (Failed)
#        472 - Compat-libical3-AppleICal_1.5.ics (Failed)
#        473 - Compat-libical3-Evolution_2.8.2_timezone_test.ics (Failed)
#        475 - Compat-libical3-KOrganizer_3.1a.ics (Failed)
#        477 - Compat-libical3-MSExchange.ics (Failed)
#        478 - Compat-libical3-Mozilla_1.0.ics (Failed)
%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*kcalendarcore.*
%{_kf5_libdir}/libKF5CalendarCore.so.*

%files devel
%{_kf5_includedir}/kcal*core_version.h
%{_kf5_includedir}/KCalendarCore/
%{_kf5_libdir}/libKF5CalendarCore.so
%{_kf5_libdir}/cmake/KF5CalendarCore/
%{_kf5_libdir}/pkgconfig/KF5CalendarCore.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KCalendarCore.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
