%global source0_hash e90461bd78787fd5cf82f73ac4bc0cfccbc4f498f35dce59eb4d168a380d6ac0
%global catch_version 2.13.10
%global cli11_version 2.4.2
%global fmt_version 11.0.2
%global libosmium_version 2.20.0
%global protozero_version 1.7.1
Name:           osm2pgsql
Version:        2.3.1
Release:        1%{?dist}
Summary:        Import map data from OpenStreetMap to a PostgreSQL database
License:        GPL-2.0-or-later
URL:            https://osm2pgsql.org/
Source0:        https://github.com/osm2pgsql-dev/osm2pgsql/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  catch2-devel
BuildRequires:  catch2-static
BuildRequires:  cli11-devel
BuildRequires:  cli11-static
BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  libosmium-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  postgis
BuildRequires:  postgresql
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  proj-devel
BuildRequires:  protozero-devel
BuildRequires:  protozero-static
BuildRequires:  python3
BuildRequires:  python3-behave
BuildRequires:  python3-osmium
BuildRequires:  python3-psycopg2
BuildRequires:  zlib-devel
# /oreon:deps
%description
Provides a tool for loading OpenStreetMap data into a PostgreSQL / PostGIS
database suitable for applications like rendering into a map, geocoding with
Nominatim, or general analysis.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -rf contrib
mkdir -p contrib/catch2
ln -sf /usr/include/catch2 contrib/catch2/include

%build

%cmake \
  -DEXTERNAL_CLI11=ON \
  -DEXTERNAL_FMT=ON \
  -DEXTERNAL_LIBOSMIUM=ON \
  -DEXTERNAL_PROTOZERO=ON \
  -DBUILD_TESTS=ON \
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
echo "local all all trust" > datadir/pg_hba.conf
psql -c "SELECT pg_reload_conf()" postgres
mkdir tablespacetest
psql -c "CREATE TABLESPACE tablespacetest LOCATION '$PWD/tablespacetest'" postgres
LANG="C.UTF-8" %ctest -j1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
