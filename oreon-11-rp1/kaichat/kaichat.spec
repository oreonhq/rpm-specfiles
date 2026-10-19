%global stable_kf6 stable
%global source0_hash 545980cd4889fced1889e53cf742ac8d538e3aaeb0d7e7bfcb8115b66e0d83a7
Name:           kaichat
Version:        0.5.1
Release:        1%{?dist}
Summary:        Chat interface for AI models such as ollama
License:        CC0-1.0 AND LGPL-2.0-or-later AND MIT AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/kaichat/
Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextAutoGenerateText)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
%summary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kaichat --all-name --with-html
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.kaichat.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
