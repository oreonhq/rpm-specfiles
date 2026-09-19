%global source0_hash 2f5d2519ee3bb75e176c85087004a2e1fb993b644518afbcf3fe91a93b87d6f7

Name:    akonadi-calendar-tools
Summary: Akonadi Calendar Tools
Version: 26.08.0
Release: 1%{?dist}

# code (generally) GPLv2, docs GFDL
# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://userbase.kde.org/Akonadi/

Source0: https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext

BuildRequires: cmake(Qt6Widgets)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6AkonadiCalendar)
BuildRequires: cmake(KPim6CalendarSupport)

# when split out
Conflicts: akonadiconsole < 16.12

Provides: konsolekalendar = %{version}-%{release}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/konsolekalendar.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*console.*
%{_kf6_bindir}/calendarjanitor
%{_kf6_bindir}/konsolekalendar
%{_kf6_datadir}/applications/konsolekalendar.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/konsolekalendar.*

%changelog
%autochangelog
