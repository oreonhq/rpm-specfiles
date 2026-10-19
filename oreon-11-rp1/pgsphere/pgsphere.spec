%global source0_hash 40c1422d252c070c7a9d4d488491c3619ad2ffded6c17353faaa6da4ed14d588
Summary:        Spherical data types, functions, and operators for PostgreSQL
Name: pgsphere
Version: 1.4.1
Release:        1%{?dist}
License: BSD-3-Clause
Source0:        https://github.com/postgrespro/%{name}/archive/refs/tags/%{version}.tar.gz
URL: https://github.com/postgrespro/pgsphere/
Requires(pre):	postgresql-server
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  healpix-c++-devel
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  postgresql-server-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
pgSphere is a server side module for PostgreSQL. It contains methods for 
working with spherical coordinates and objects. It also supports indexing of 
spherical objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build 
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
