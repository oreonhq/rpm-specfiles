%global stable_kf6 stable
%global source0_hash 0b3e9bdaf3a9f2766efb7007dff9bb1278d4753eaa05eca138f24231ac485de2
ExcludeArch: %{ix86}
Name:    kcron
Summary:        Cron KDE configuration module
Version: 25.12.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/system/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
Systemsettings module for the cron task scheduler.

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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
