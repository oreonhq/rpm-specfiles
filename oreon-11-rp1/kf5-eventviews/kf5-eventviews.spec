%global framework eventviews

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: KDE PIM library for displaying events and calendars

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# available only where kf5-calendarsupport is
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules >= 5.23.0
BuildRequires:  kf5-rpm-macros >= 5.23.0

BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  cmake(KGantt)

BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KF5TextEditTextToSpeech)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-calendar-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-calendarsupport-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarutils-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}

Obsoletes:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiCalendar)
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5CalendarSupport)
Requires:       cmake(KPim5CalendarUtils)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libeventviews5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libeventviews/libeventviews5/" src/CMakeLists.txt
sed -i "s/libeventviews/libeventviews5/" src/Messages.sh


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5EventViews.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_EventViews.pri
%{_includedir}/KPim5/EventViews/
%{_kf5_libdir}/cmake/KPim5EventViews/
%{_kf5_libdir}/libKPim5EventViews.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
