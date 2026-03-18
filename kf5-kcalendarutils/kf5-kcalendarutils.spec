%undefine __cmake_in_source_build
%global framework kcalutils

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-kcalendarutils
Version: 23.08.5
Release: 5%{?dist}
Summary: The KCalendarUtils Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# libical (and thus kcalendarcore) not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5TextEditTextToSpeech)
# when macros.grantlee5 was introduced
BuildRequires:  grantlee-qt5-devel >= 5.1.0-2
%{?grantlee5_requires}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel >= 5.15
BuildRequires:  kf5-kconfig-devel >= 5.15
BuildRequires:  kf5-ki18n-devel >= 5.15
BuildRequires:  kf5-kdelibs4support-devel >= 5.15
BuildRequires:  kf5-kcodecs-devel >= 5.15
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  qt5-qtbase-devel
%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

Provides:       kf5-%{framework} = %{version}-%{release}
Provides:       kf5-%{framework}%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       kf5-%{framework}-devel = %{version}-%{release}
Provides:       kf5-%{framework}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kdelibs4support-devel
Requires:       kf5-kcalendarcore-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 60" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5CalendarUtils.so.*
%{grantlee5_plugindir}/kcalendar_grantlee_plugin.so

%files devel
%{_includedir}/KPim5/KCalUtils/
%{_kf5_libdir}/libKPim5CalendarUtils.so
%{_kf5_libdir}/cmake/KPim5CalendarUtils/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCalUtils.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
