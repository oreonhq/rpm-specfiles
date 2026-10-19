%global source0_hash 0e4170e099c9ffedfcbb1290f1fc42c00560cf6108e25fe90685315f18c8d6cc
%global minor_version 0.4
%global thunar_version 4.20.0
Name:           thunar-vcs-plugin
Version:        0.4.0
Release:        1%{?dist}
Summary:        Version Contol System plugin for the Thunar filemanager
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz
Requires:       Thunar >= %{thunar_version}
Requires:       subversion
Requires:       git
Provides:       thunar-svn-plugin = %{version}-%{release}
Obsoletes:      thunar-svn-plugin < 0.0.4-1
# oreon:deps
BuildRequires:  Thunar-devel
BuildRequires:  apr-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  subversion-devel
BuildRequires:  uuid-devel
# /oreon:deps
%description
The Thunar VCS Plugin adds Subversion and GIT actions to the context menu of 
Thunar. This gives a VCS integration to Thunar. The current features are:
* Most of the SVN actions: add, blame, checkout, cleanup, commit, copy, 
  delete, export, import, lock, log, move, properties, relocate, resolved, 
  revert, status, switch, unlock and update
* Subversion info in file properties dialog
* Basic GIT actions: add, blame, branch, clean, clone, log, move, reset, stash 
  and status

This project was formerly known as Thunar SVN Plugin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
