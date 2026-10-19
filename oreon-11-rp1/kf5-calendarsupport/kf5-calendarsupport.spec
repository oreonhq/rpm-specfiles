%global source0_hash 65fa5ca77e19515dad579cf96e7cf16025d64a6a9a39c63772691a6bc16f3ef3
%global framework      calendarsupport
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        KDE PIM library for calendar and even handling
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global kf5_ver 5.71.0
%global majmin_ver %{version}
Obsoletes:      kdepim-libs < 7:16.04.0
# oreon:deps
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5PimCommon)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-calendar-devel
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcalendarutils-devel
BuildRequires:  kf5-kholidays-devel
BuildRequires:  kf5-kidentitymanagement-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-pimcommon-devel
BuildRequires:  kf5-rpm-macros
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-calendarsupport-devel -f %{oreon_filedir}/kf5-calendarsupport-devel.list

%changelog

%autochangelog
