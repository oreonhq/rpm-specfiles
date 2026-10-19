%global source0_hash 4b7af2be944280cc6be397b76fad3d6588ac93e771fdb19a485b358b21a50326
%global core_name timescale
Name:           %{core_name}db
Version:        2.30.1
Release:        1%{?dist}
Summary:        Open-source time-series database powered by PostgreSQL
License:        Apache-2.0
URL:            http://www.%{core_name}.com
Source0:        https://github.com/%{core_name}/%{name}/archive/refs/tags/%{version}.tar.gz
Requires(pre): postgresql-server
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  postgresql-server-devel
# /oreon:deps
%description
TimescaleDB is an open-source database designed to make SQL scalable for
time-series data.  It is engineered up from PostgreSQL, providing automatic
partitioning across time and space (partitioning key), as well as full SQL
support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
# Remove tsl directory containing sources licensed under Timescale license
rm -rf tsl

%build

%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_config
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
