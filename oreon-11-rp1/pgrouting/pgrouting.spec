%global source0_hash b8a5f0472934fdf7cda3fb4754d01945378d920cdaddc01f378617ddbb9c447f

Name:          pgrouting
Version:       3.8.0
Release:       3%{?dist}
Summary:       Provides routing functionality to PostGIS / PostgreSQL
License:       GPL-2.0-or-later AND BSL-1.0 AND MIT
URL:           https://pgrouting.org
Source:        https://github.com/pgRouting/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: perl-interpreter
BuildRequires: perl-File-Find
BuildRequires: perl-version
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: postgresql-server-devel
BuildRequires: boost-graph
BuildRequires: cmake

Requires:      postgresql-server
Requires:      postgis

%description
pgRouting extends the PostGIS / PostgreSQL geospatial database to provide
geospatial routing functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DPOSTGRESQL_PG_CONFIG=%{_bindir}/pg_server_config
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%license BOOST_LICENSE_1_0.txt
%license tools/licences/MIT_license.txt
%license tools/licences/GNU_license.txt
%license tools/licences/CCM_license.txt
%doc CODE_OF_CONDUCT.md NEWS README.md CONTRIBUTING.md
%{_libdir}/pgsql/libpgrouting-%{sub %version 1 3}.so
%{_datadir}/pgsql/extension/pgrouting--*--%{version}.sql
%{_datadir}/pgsql/extension/pgrouting--%{version}.sql
%{_datadir}/pgsql/extension/pgrouting.control

%changelog
%autochangelog
