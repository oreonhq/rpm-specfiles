%global source0_hash 01d5d551c6fe2e86edc37ef465d331a9682795b49d58a3b7a3ffb1ee1edce736
Name: tuned-switcher
Version: 1.1.2
Release:        1%{?dist}
License: GPL-3.0-or-later AND Apache-2.0
Summary:        Simple utility to manipulate the Tuned service
URL: https://github.com/xvitaly/%{name}
Source0:        https://github.com/xvitaly/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires: hicolor-icon-theme
Requires: tuned
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pandoc
# /oreon:deps
%description
Tuned Switcher is a simple utility for managing performance profiles using
the Tuned service.

Tuned is a daemon for monitoring and adaptive tuning of system devices.
In order to use this program, a daemon must be installed on your system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON
%cmake_build
%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
