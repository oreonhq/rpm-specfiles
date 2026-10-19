%global source0_hash 4232611db32fcf3976e1ee0d7f6c0c4321ea688cc322dadeefd7914ddd2dd6c2
ExcludeArch: %{ix86}
Name:    kmail-account-wizard
Summary:        KMail Account Wizard
Version: 26.08.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Conflicts: kdepim-common < 16.12
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6LdapCore)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(shared-mime-info)
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.accountwizard.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
