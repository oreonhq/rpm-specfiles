%global source0_hash 0a05013b252b77f47c16ba1878e6d4a5f05dcc0a82cb98d7024f308ad8b5a349
Name:    akonadi-contacts
Version: 26.08.0
Release:        1%{?dist}
Summary:        The Akonadi Contacts Library
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Obsoletes:      kf5-akonadi-contacts < 24.01.80-1
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  cmake(KPim6Akonadi)
Requires:  cmake(KF6Contacts)
Requires:  cmake(KPim6GrantleeTheme)
Recommends:  cmake(KF6CalendarCore)
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
find ./po -type f -name akonadicontact5.po -execdir mv {} akonadicontact6.po \;
find ./po -type f -name akonadicontact5-serializer.po -execdir mv {} akonadicontact6-serializer.po \;

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles akonadi-contacts-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles akonadi-contacts-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n akonadi-contacts-devel -f %{oreon_filedir}/akonadi-contacts-devel.list
%files -n akonadi-contacts-doc -f %{oreon_filedir}/akonadi-contacts-doc.list

%changelog

%autochangelog
