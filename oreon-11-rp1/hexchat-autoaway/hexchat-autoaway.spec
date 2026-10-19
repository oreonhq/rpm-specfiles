%global source0_hash 608ba6b934869a5fe5d7402a178e2a24101d71eda2cb9b4b19e09058023eb8dc
%{?!_vpath_builddir:%define _vpath_builddir %{_target_platform}}
%if %{?cmake_build:1}%{?!cmake_build:0}
%global old_build 0
%else
%global old_build 1
%endif
Name:           hexchat-autoaway
Version:        2.0
Release:        1%{?dist}
Summary:        HexChat plugin that automatically mark you away
License:        GPL-3.0-or-later
URL:            https://github.com/andreyv/hexchat-autoaway
Source0:        https://github.com/andreyv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/andreyv/hexchat-autoaway/pull/3.patch#/0001-append-away-suffix-to-nickname.patch
Requires: gtk2 >= 2.14
Requires: hexchat
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gtk2-devel
BuildRequires:  hexchat-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  make
# /oreon:deps
%description
This HexChat plugin will automatically mark you away when your
computer is idle. It works on systems that use the GTK+ X11
backend, such as GNU/Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %old_build
mkdir -p %_vpath_builddir
cd %_vpath_builddir && %cmake3 -DCMAKE_BUILD_TYPE=Release ..
%make_build
cd -
%else
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%endif
%install
%if %old_build
%make_install -C %_vpath_builddir
%else
%cmake_install
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
