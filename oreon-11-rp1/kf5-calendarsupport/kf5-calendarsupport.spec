%global source0_hash 65fa5ca77e19515dad579cf96e7cf16025d64a6a9a39c63772691a6bc16f3ef3

%global framework      calendarsupport

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: KDE PIM library for calendar and even handling

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# available only where kf5-pimcommon is
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

%global kf5_ver 5.71.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)

BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5PimCommon)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-calendar-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
BuildRequires:  kf5-kcalendarutils-devel >= %{majmin_ver}
BuildRequires:  kf5-kholidays-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

Obsoletes:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Mime)
Requires:       cmake(KF5IdentityManagement)
Requires:       cmake(KF5AkonadiCalendar)
Requires:       kf5-akonadi-calendar-devel >= %{majmin_ver}
Requires:       kf5-kidentitymanagement-devel >= %{majmin_ver}
Requires:       kf5-kmime-devel >= %{majmin_ver}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} calendarsupport5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/calendarsupport/calendarsupport5/" src/CMakeLists.txt
sed -i "s/calendarsupport/calendarsupport5/" src/Messages.sh

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
%{_kf5_libdir}/libKPim5CalendarSupport.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_CalendarSupport.pri
%{_includedir}/KPim5/CalendarSupport/
%{_kf5_libdir}/cmake/KF5CalendarSupport/
%{_kf5_libdir}/cmake/KPim5CalendarSupport/
%{_kf5_libdir}/libKPim5CalendarSupport.so

%changelog
%autochangelog
