%global source0_hash b128ace80c3dcc172dcc6b4c6b0e368e9430b4470eb4947b794df807b96c706a
%global gitcommit c5b97e4020be23e431d53fb3642accc55d36f1c7
%global gitdate 20240409.165252
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
Name:          notae
Version:       0.1~%{gitdate}.%{shortcommit}
Release:        1%{?dist}
License:       CC0-1.0 AND BSD-2-Clause AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
Summary:        A simple note taking application that automatically saves your work
URL:           https://apps.kde.org/notae/
Source0:        https://invent.kde.org/utilities/%{name}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
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

%autosetup -p1 -n %{name}-%{gitcommit}

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.notae.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
