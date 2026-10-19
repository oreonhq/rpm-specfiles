%global source0_hash 2c864a104db564cf28a440aa165b1687b1fc76cac43fac326119a50d74b01144
Name:          maui-agenda
Version:       1.0.0
Release:        1%{?dist}
License:       MIT AND GPL-3.0-or-later AND LGPL-3.0-only
Summary:        Maui Calendar App for Plasma Mobile
URL:           https://apps.kde.org/%{name}/
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Source0:        https://download.kde.org/stable/maui/agenda/%{version}/maui-agenda-%{version}.tar.xz
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiKitCalendar4)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir maui-agenda-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.agenda.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
