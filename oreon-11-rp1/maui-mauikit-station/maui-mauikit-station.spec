%global source0_hash 8834adb7474e924ac1a4dd0981c237fd5cc4e2902c2c94268314e9c24c5285e0
Name:          maui-mauikit-station
Version:       4.0.0
Release:        1%{?dist}
License:       MIT AND GPL-3.0-or-later
Summary:        Convergent terminal emulator written using Maui
URL:           https://mauikit.org/apps/station/
Source0:        https://download.kde.org/stable/maui/station/%{version}/maui-station-%{version}.tar.xz
Patch0:        8.patch
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitTerminal4)
BuildRequires:  cmake(Qt6DBus)
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
%global oreon_srcdir maui-station-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang station --with-man --with-qt --all-name
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.station.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
