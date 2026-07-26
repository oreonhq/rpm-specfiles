%global source0_hash 40c1422d252c070c7a9d4d488491c3619ad2ffded6c17353faaa6da4ed14d588

Summary: Spherical data types, functions, and operators for PostgreSQL
Name: pgsphere
Version: 1.4.1
Release: 8%{?dist}
License: BSD-3-Clause

Source0: https://github.com/postgrespro/%{name}/archive/refs/tags/%{version}.tar.gz
URL: https://github.com/postgrespro/pgsphere/

BuildRequires: make
BuildRequires: gcc
BuildRequires: postgresql-server-devel
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: healpix-c++-devel
BuildRequires: zlib-devel
Requires(pre):	postgresql-server

%description
pgSphere is a server side module for PostgreSQL. It contains methods for 
working with spherical coordinates and objects. It also supports indexing of 
spherical objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%make_build 

%install
%make_install

%files
%doc %{_datadir}/doc/pgsql/extension/README.pg_sphere
%license %{_datadir}/doc/pgsql/extension/COPYRIGHT.pg_sphere
%{_libdir}/pgsql/pg_sphere*
%{_datadir}/pgsql/extension/pg_sphere*

%changelog
%autochangelog
