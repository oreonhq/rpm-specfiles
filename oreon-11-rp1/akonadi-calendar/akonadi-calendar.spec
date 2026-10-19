%global source0_hash 6c2c21d3932c4c4905ecd6fb0b21b265ba9dc45fd35e538e2795f3b09aae2c5f
ExcludeArch: %{ix86}
Name:    akonadi-calendar
Version: 26.08.0
Release:        1%{?dist}
Summary:        The Akonadi Calendar Library
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Obsoletes:      kf5-akonadi-calendar < 24.01.80-1
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6AkonadiContactCore)
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KPim6IdentityManagementCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libakonadi-calendar5.po -execdir mv {} libakonadi-calendar6.po \;
find ./po -type f -name libakonadi-calendar5-serializer.po -execdir mv {} libakonadi-calendar6-serializer.po \;

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles akonadi-calendar-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles akonadi-calendar-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n akonadi-calendar-devel -f %{oreon_filedir}/akonadi-calendar-devel.list
%files -n akonadi-calendar-doc -f %{oreon_filedir}/akonadi-calendar-doc.list

%changelog

%autochangelog
