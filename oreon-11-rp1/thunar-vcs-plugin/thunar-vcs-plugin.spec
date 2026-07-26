%global source0_hash 0e4170e099c9ffedfcbb1290f1fc42c00560cf6108e25fe90685315f18c8d6cc

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=529465

%global minor_version 0.4
%global thunar_version 4.20.0

Name:           thunar-vcs-plugin
Version:        0.4.0
Release:        36%{?dist}
Summary:        Version Contol System plugin for the Thunar filemanager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  subversion-devel >= 1.5
BuildRequires:  apr-devel >= 0.9.7
BuildRequires:  e2fsprogs-devel
BuildRequires:  uuid-devel
BuildRequires:  libuuid-devel
BuildRequires:  meson
BuildRequires:  libxfce4ui-devel

Requires:       Thunar >= %{thunar_version}
Requires:       subversion
Requires:       git
# Obsolete thunar-svn-plugin for smooth upgrades
Provides:       thunar-svn-plugin = %{version}-%{release}
Obsoletes:      thunar-svn-plugin < 0.0.4-1

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

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/thunarx-*/%{name}.so
%{_libexecdir}/tvp-svn-helper
%{_libexecdir}/tvp-git-helper
%{_datadir}/icons/hicolor/*/apps/subversion.png
%{_datadir}/icons/hicolor/*/apps/git.png

%changelog
%autochangelog
