%global source0_hash c68c12c3d62f2e3c46d277d2558c20e31d3826b84e15a8594d1084874a1ea9a4

%global core_name timescale

Name:           %{core_name}db
Version:        2.16.0
Release:        2%{?dist}
Summary:        Open-source time-series database powered by PostgreSQL

License:        Apache-2.0
URL:            http://www.%{core_name}.com
Source0:        https://github.com/%{core_name}/%{name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake gcc openssl-devel postgresql-server-devel

Requires(pre): postgresql-server

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
%if 0%{?fedora} >= 30 || 0%{?epel} >= 8
%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_server_config
%else
%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_config
%endif
%cmake_build

%install
%cmake_install

%files
%license LICENSE-APACHE
%doc README.md
%{_libdir}/pgsql/%{name}-%{version}.so
%{_libdir}/pgsql/%{name}.so
%{_datadir}/pgsql/extension/%{name}--*%{version}.sql
%{_datadir}/pgsql/extension/%{name}.control

%changelog
%autochangelog
