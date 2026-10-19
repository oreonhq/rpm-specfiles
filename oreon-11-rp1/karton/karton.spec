%global source0_hash 8c87421647e2f3e8e6752b41f311917c1267d4afe0ac3604daf105bb60281fe7
%global gitcommit 07520e06f5a66e9cfe33a298a11e5482a2395aa0
%global gitdate 20251110.023853
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
Name:           karton
Version:        0.1^%{gitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        A Libvirt-based Virtual Machine Manager for KDE
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-3.0-or-later
URL:            https://invent.kde.org/sitter/%{name}
Source0:        https://invent.kde.org/sitter/%{name}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
Requires:       kf6-kirigami
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libosinfo-1.0)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(spice-client-glib-2.0)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitcommit} -p1

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.karton.desktop ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
