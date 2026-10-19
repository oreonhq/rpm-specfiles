%global source0_hash 29a9359940e6ba775c9e1dccfd9eb7de68b799ef4182f4eaf7ba3baffaaf1c1b
%global framework eventviews
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        KDE PIM library for displaying events and calendars
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global majmin_ver %{version}
Obsoletes:      kdepim-libs < 7:16.04.0
# oreon:deps
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KGantt)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-calendar-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-calendarsupport-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcalendarutils-devel
BuildRequires:  kf5-kidentitymanagement-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-libkdepim-devel
BuildRequires:  kf5-rpm-macros
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-eventviews-devel -f %{oreon_filedir}/kf5-eventviews-devel.list

%changelog

%autochangelog
