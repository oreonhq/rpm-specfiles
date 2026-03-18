%global base_name akonadi-calendar

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{base_name}
Version: 23.08.5
Release: 5%{?dist}
Summary: The Akonadi Calendar Library

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{base_name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5MessageCore)
BuildRequires:  grantlee-qt5-devel
BuildRequires:  kf5-rpm-macros
%global kf5_ver 5.87.0
BuildRequires:  kf5-kdelibs4support-devel >= %{kf5_ver}
BuildRequires:  kf5-kio-devel >= %{kf5_ver}
BuildRequires:  kf5-kwallet-devel >= %{kf5_ver}
BuildRequires:  kf5-kcodecs-devel >= %{kf5_ver}
#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarutils-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-contacts-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  qt5-qtbase-devel
%if 0%{?tests}
BuildRequires: kf5-akonadi-server >= %{majmin_ver}
BuildRequires: kf5-akonadi-server-mysql
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-akonadi-contacts-devel
Requires:       kf5-akonadi-server-devel
Requires:       kf5-kcalendarcore-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang libakonadi-calendar5
%find_lang libakonadi-calendar5-serializer
cat libakonadi-calendar5-serializer.lang >> libakonadi-calendar5.lang

%find_lang kalendarac


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f kalendarac.lang
%license LICENSES/*
%{_kf5_bindir}/kalendarac
%{_kf5_datadir}/akonadi/plugins/serializer/
%{_kf5_datadir}/dbus-1/services/org.kde.kalendarac.service
%{_kf5_datadir}/knotifications5/kalendarac.notifyrc
%{_kf5_datadir}/qlogging-categories5/org_kde_kalendarac.categories
%{_kf5_qtplugindir}/akonadi_serializer_kcalcore.so
%{_kf5_qtplugindir}/kf5/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so
%{_kf5_sysconfdir}/xdg/autostart/org.kde.kalendarac.desktop

%files libs -f libakonadi-calendar5.lang
%{_kf5_libdir}/libKPim5AkonadiCalendar.so.*
%{_kf5_datadir}/qlogging-categories5/*%{base_name}.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_AkonadiCalendar.pri
%{_includedir}/KPim5/AkonadiCalendar/Akonadi/
%{_includedir}/KPim5/AkonadiCalendar/akonadi-calendar_version.h
%{_includedir}/KPim5/AkonadiCalendar/akonadi/
%{_kf5_libdir}/cmake/KF5AkonadiCalendar/
%{_kf5_libdir}/cmake/KPim5AkonadiCalendar/
%{_kf5_libdir}/libKPim5AkonadiCalendar.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
