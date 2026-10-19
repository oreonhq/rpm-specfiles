%global source0_hash f6962483bc78fc183d8d47cb753bfc0ccfe1f4159e9bbd122ae78aeb402f63ec
%global commit 3e21584b0524a7998dcc20424329d1886ceb0a12
%global shortcommit %(c=%{commit}; echo ${c:0:8})
Name:           kolorfill
Version:        0^20250825.%{shortcommit}
Release:        2%{?dist}
Summary:        Simple flood fill game
License:        MIT
URL:            https://apps.kde.org/kolorfill
Source0:        https://invent.kde.org/games/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Requires:      kf6-kirigami%{?_isa}
# oreon:deps
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  qt6-rpm-macros
# /oreon:deps
%description
Given a board initially filled with randomly colored blocks,
on each turn choose a color to expand the uniform color surrounding
the top left most block by so that at the end, the board is filled
with one color.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
