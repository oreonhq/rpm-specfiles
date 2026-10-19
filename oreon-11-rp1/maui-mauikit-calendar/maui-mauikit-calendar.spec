%global source0_hash 0a9169250bab954fb1b7d07195e9e6322c183946b6268aa2983e080bf55095d0
Name:          maui-mauikit-calendar
Version:       4.0.0
Release:        1%{?dist}
License:       GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND GPL-3.0-or-later
Summary:        Calendar support components for Maui applications
URL:           https://invent.kde.org/maui/mauikit-calendar/
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Source0:        https://download.kde.org/stable/maui/mauikit-calendar/%{version}/mauikit-calendar-%{version}.tar.xz
Patch0:        24.08-fix.patch
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Required headers to build components based
on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mauikit-calendar-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang mauikitcalendar
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-calendar-devel -f %{oreon_filedir}/maui-mauikit-calendar-devel.list

%changelog

%autochangelog
