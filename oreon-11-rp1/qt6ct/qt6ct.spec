%global source0_hash b16b65771d195f2ee983d11e188e9257b242b3625d65d150ee6c7932e9415c2e
%global forgename gitlab
%global forgeurl https://www.opencode.net/trialuser/qt6ct
%global commit 23a985f45cf793ce7ce05811411d2374b4f979c4
%forgemeta
Name:    qt6ct
Version: 0.11
Release:        1%{?dist}
Summary:        Qt6 - Configuration Tool
License: BSD-2-Clause
URL:     %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
Patch0:  qt6ct-kde.patch
Patch1:  0001-build-refactor-CMake-build-rules.patch
Patch2:  0002-Wrap-forward-declaration-within-QT_NAMESPACE.patch
Patch3:  0003-Revert-Use-KDE-s-QtQuick-QtWidgets-style-bridge.patch
Patch4:  qt6ct-fix-build-against-qt-6-10.patch
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
This program allows users to configure Qt6 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake -DQT6CT_IN_TREE=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
