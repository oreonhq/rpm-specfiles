%global source0_hash 2654ddd64ab243e1424d44b8f293daec1eab442809dd85b763ce70a58aa641e4
Summary:        Gamerzilla Integration Library
Name: libgamerzilla
Version: 0.1.3
Release:        1%{?dist}
License: zlib
URL: https://github.com/dulsi/libgamerzilla
Source0:        http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jansson-devel
BuildRequires:  libcurl-devel
# /oreon:deps
%description
Gamerzilla is trophy/achievement system for games. It integrates with a
hubzilla plugin to display your results online. Games can either connect
directly to hubzilla or connect to a game launcher with using this
library.

%package devel
Summary: Libraries and includes for Gamerzilla development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains libraries and header files for
developing applications that use gamerzilla.

%package server
Summary: Simple Gamerzilla server to relay information to Hubzilla
%description server
The gamerzillaserver listens for trophies awarded by games. It logs into
the user's Hubzilla server and passes on the awards.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libgamerzilla-devel -f %{oreon_filedir}/libgamerzilla-devel.list
%files -n libgamerzilla-server -f %{oreon_filedir}/libgamerzilla-server.list

%changelog

%autochangelog
