%global source1_hash e666c20d89b91beb44bc17b156136cf417c775c7b4dbe67e689c884847f0058f
%global source0_hash 6590fefad29e37be7d51ed89e9dbaf67884ae0a3fed14f8d58ac1352c0c0503d
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    kde-gtk-config
Summary:        Configure the appearance of GTK apps in KDE
Version:        6.7.5
Release:        1%{?dist}
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/kde-gtk-config-%{version}.tar.xz.sig
Requires:       breeze-gtk-common
Requires:       kde-cli-tools
Recommends:     xsettingsd
# oreon:deps
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  sassc
BuildRequires:  xsettingsd
# /oreon:deps
%description
This is a System Settings configuration module for configuring the
appearance of GTK apps in KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
