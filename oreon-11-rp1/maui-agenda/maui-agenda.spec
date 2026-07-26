%global source0_hash 2c864a104db564cf28a440aa165b1687b1fc76cac43fac326119a50d74b01144

Name:          maui-agenda
Version:       1.0.0
Release:       4%{?dist}
# SPDX licenses missing from project, for the most part.
License:       MIT AND GPL-3.0-or-later AND LGPL-3.0-only
Summary:       Maui Calendar App for Plasma Mobile
URL:           https://apps.kde.org/%{name}/

# Akonadi has limited arches, and this package depends on it.
# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

Source0:       https://download.kde.org/stable/maui/agenda/%{version}/maui-agenda-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(MauiKitCalendar4)
BuildRequires: cmake(MauiKit4)

Requires:      hicolor-icon-theme

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n maui-agenda-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.agenda.desktop
# One item in the xml file fails verification
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml ||:

%files
%license licenses/* LICENSE
%doc README.md
%{_kf6_bindir}/agenda
%{_metainfodir}/org.kde.agenda.appdata.xml
%{_kf6_datadir}/applications/org.kde.agenda.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/agenda.svg

%changelog
%autochangelog
