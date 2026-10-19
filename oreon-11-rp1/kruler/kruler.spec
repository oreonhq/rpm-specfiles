%global stable_kf6 stable
%global source0_hash c211bec09a71bda55b1ab86223729603ec7c3206296466bc8ae98dcb76cb7084
ExcludeArch: %{ix86}
Name:    kruler
Summary:        A screen ruler and color measurement tool
Version: 25.12.3
Release:        1%{?dist}
License: GFDL-1.2-or-later AND GPL-2.0-or-later
URL:     https://www.kde.org/applications/graphics/kruler/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Conflicts: kdegraphics < 7:4.6.95-10
Conflicts: kde-l10n < 17.03
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
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
%find_lang %{name} --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
