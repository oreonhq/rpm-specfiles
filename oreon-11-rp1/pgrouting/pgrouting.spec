%global source0_hash 2faf31b178db969637c1f392ba3ba18fba8d5aed15bdc73fbb4a53a72c5d0f71
Name:          pgrouting
Version:       4.0.2
Release:        1%{?dist}
Summary:        Provides routing functionality to PostGIS / PostgreSQL
License:       GPL-2.0-or-later AND BSL-1.0 AND MIT
URL:           https://pgrouting.org
Source0:        https://github.com/pgRouting/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:      postgresql-server
Requires:      postgis
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  boost-graph
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl-File-Find
BuildRequires:  perl-interpreter
BuildRequires:  perl-version
BuildRequires:  postgresql-server-devel
# /oreon:deps
%description
pgRouting extends the PostGIS / PostgreSQL geospatial database to provide
geospatial routing functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DPOSTGRESQL_PG_CONFIG=%{_bindir}/pg_server_config
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
