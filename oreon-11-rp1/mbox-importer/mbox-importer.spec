%global stable_kf6 stable
%global source0_hash 628238e028aeaa2a6395a78449abfe4344d69fcff7c7f4b70994a98fc194be95
Name:    mbox-importer
Summary:        MBox Importer
Version: 25.12.3
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Conflicts: kmail < 16.12
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailImporterAkonadi)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.mboximporter.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
