%global source0_hash b8f352fe688cca9dd5712238f44a8fc57878709bf280adee4ab38a3f9de1f54d
Name:    akonadiconsole
Summary:        Akonadi developer tool
Version: 26.08.0
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/akonadiconsole/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Requires: akonadi-calendar-tools
# oreon:deps
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6AkonadiSearch)
BuildRequires:  cmake(KPim6CalendarSupport)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6MessageViewer)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  perl-generators
BuildRequires:  xapian-core-devel
# /oreon:deps
%description
Akonadi Console is a tool for Akonadi developers that provides means of direct
interaction with the Akonadi storage, SQL debugging, protocol debugger and
other tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
