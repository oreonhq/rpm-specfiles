%global source0_hash 21d12c6b38b04ea19320afe97907986a9a432a9cf6cff33afe015dc1aa6404b6

%global framework importwizard

Name:    akonadi-import-wizard
Summary: Akonadi Import Wizard
Version: 26.08.0
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Gui)

BuildRequires: extra-cmake-modules
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6MailCommon)
BuildRequires: cmake(KPim6MailImporterAkonadi)
BuildRequires: cmake(KPim6MessageViewer)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(QGpgmeQt6)
BuildRequires: cmake(KF6IconThemes)

# when split out
Conflicts: kdepim-common < 16.12

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

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.akonadiimportwizard.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_bindir}/akonadiimportwizard
%{_kf6_datadir}/applications/org.kde.akonadiimportwizard.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kontact-import-wizard.*
%{_kf6_datadir}/importwizard/
%{_kf6_libdir}/libKPim6ImportWizard.so.*
%{_kf6_qtplugindir}/pim6/importwizard/

%files devel
%{_kf6_libdir}/libKPim6ImportWizard.so
%{_kf6_libdir}/cmake/KPim6ImportWizard/
%dir %{_includedir}/KPim6/
%{_includedir}/KPim6/ImportWizard/

%changelog
%autochangelog
