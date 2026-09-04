%global source0_hash 1effdb62375b66435de8b75cfe1429eeda5facc546d9b192e8a8affeea216bba

Name:    akonadiconsole
Summary: Akonadi developer tool
Version: 26.08.0
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/akonadiconsole/

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: perl-generators

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6TextTemplate)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6CalendarSupport)
BuildRequires: cmake(KPim6MessageViewer)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: xapian-core-devel
BuildRequires: cmake(QGpgmeQt6)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

# upgrade path, previously included here
Requires: akonadi-calendar-tools

%description
Akonadi Console is a tool for Akonadi developers that provides means of direct
interaction with the Akonadi storage, SQL debugging, protocol debugger and
other tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_bindir}/akonadiconsole
%{_kf6_datadir}/applications/org.kde.akonadiconsole.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/akonadiconsole.*
%{_kf6_libdir}/libakonadiconsole.so.*

%changelog
* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

%autochangelog
