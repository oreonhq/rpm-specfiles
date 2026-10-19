%global source0_hash 039012bf56beb31c297c5191daf6c1afa3d31b77560631e2a14e9dd7a44effcc
Name:           deepin-shortcut-viewer
Version:        5.5.6
Release:        1%{?dist}
Summary:        Deepin Shortcut Viewer
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-shortcut-viewer
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
# /oreon:deps
%description
The program displays a shortcut key window when a JSON data is passed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
