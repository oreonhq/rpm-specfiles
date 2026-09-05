%global source0_hash 0a41268e6b153700c4c815da1baa40637efa61943f4e387f66cf5599d8e8d502

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kmail-account-wizard
Summary: KMail Account Wizard
Version: 26.08.0
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: cmake
BuildRequires: perl-generators

BuildRequires: pkgconfig(shared-mime-info)

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Keychain)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6LdapCore)
BuildRequires: cmake(KPim6Libkleo)
BuildRequires: cmake(QGpgmeQt6)
BuildRequires: cmake(KPim6IMAP)

# when split out
Conflicts: kdepim-common < 16.12

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.accountwizard.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/accountwizard
%{_kf6_datadir}/applications/org.kde.accountwizard.desktop
%{_metainfodir}/org.kde.accountwizard.appdata.xml

%changelog
%autochangelog
