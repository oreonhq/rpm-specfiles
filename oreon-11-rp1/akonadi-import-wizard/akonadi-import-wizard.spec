%global source0_hash 20d38918b47e8ddc78e08fae11e5fc70959c55ec80caf44c8204d34b943fed1f
%global framework importwizard
Name:    akonadi-import-wizard
Summary:        Akonadi Import Wizard
Version: 26.08.0
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Conflicts: kdepim-common < 16.12
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailImporterAkonadi)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MessageViewer)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6MailTransport)
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles akonadi-import-wizard-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.akonadiimportwizard.desktop
%files -f %{oreon_filedir}/main.list
%files -n akonadi-import-wizard-devel -f %{oreon_filedir}/akonadi-import-wizard-devel.list

%changelog

%autochangelog
