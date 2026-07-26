%global source0_hash 2f57ea993a720b1ce7ea4948350c8e3af9380736621d42ae42ae3b6eb539a53c

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

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# libical (and thus kcalendarcore) not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: make
BuildRequires:  extra-cmake-modules >= %{majmin}
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
