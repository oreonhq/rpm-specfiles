%global source0_hash 3be2444ab6ea0042a640e8f3282c7931e2570cd8d41af80ba583a14d8088b84b
Name:		libsysstat
Version:	1.1.0
Release:        1%{?dist}
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Library used to query system info and statistics
Url:		http://www.lxde.org
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(Qt6Core)
# /oreon:deps
%description
Library used to query system info and statistics

%package devel
Summary:	Devel files for libsysstat
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description devel
Sysstat libraries for development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libsysstat-devel -f %{oreon_filedir}/libsysstat-devel.list

%changelog

%autochangelog
