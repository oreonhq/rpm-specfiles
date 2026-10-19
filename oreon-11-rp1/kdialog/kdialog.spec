%global source0_hash e7142c812d2b4b202abd12bea054f8368fdba9bb0552a9f46d3a7d7283339c72
%global stable_kf6 stable
Name:    kdialog
Summary:        Nice dialog boxes from shell scripts
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
KDialog can be used to show nice dialog boxes from shell scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html --with-man
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
