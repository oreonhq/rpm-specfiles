%global source0_hash cc1b3a65c60bd88b77a1ddd1574042d83cf7cc32b85fe9481c99613359eb7cfe
Name:		libcue
Version:	2.3.0
Release:        1%{?dist}
Summary:        Cue sheet parser library
License:	GPL-2.0-only AND BSD-2-Clause
URL:		https://github.com/lipnitsk/%{name}
VCS:		git:%{url}.git
Source0:        https://github.com/lipnitsk/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:		libcue-0001-Raise-minimum-CMake-version-up-to-3.5.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# /oreon:deps
%description
Libcue is intended for parsing a so-called cue sheet from a char string or a
file pointer. For handling of the parsed data a convenient API is available.

%package devel
Summary:	Development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build --target test
%files -f %{oreon_filedir}/main.list
%files -n libcue-devel -f %{oreon_filedir}/libcue-devel.list

%changelog

%autochangelog
