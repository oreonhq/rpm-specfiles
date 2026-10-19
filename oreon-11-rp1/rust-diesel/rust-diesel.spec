%global source0_hash e3b934ddbdcb2abb9f9fc9c30bd47bcc5618b615eea1d334cda5fdf8ff9b072a
%bcond check 0
%global debug_package %{nil}
%global crate diesel
Name:           rust-diesel
Version:        2.3.13
Release:        1%{?dist}
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/diesel
Source0:        https://static.crates.io/crates/diesel/diesel-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+128-column-tables-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+128-column-tables-devel

This package contains library source intended for building other packages which
use the "128-column-tables" feature of the "%{crate}" crate.

%package     -n %{name}+32-column-tables-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+32-column-tables-devel

This package contains library source intended for building other packages which
use the "32-column-tables" feature of the "%{crate}" crate.

%package     -n %{name}+64-column-tables-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+64-column-tables-devel

This package contains library source intended for building other packages which
use the "64-column-tables" feature of the "%{crate}" crate.

%package     -n %{name}+__with_asan_tests-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+__with_asan_tests-devel

This package contains library source intended for building other packages which
use the "__with_asan_tests" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+extras-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+extras-devel

This package contains library source intended for building other packages which
use the "extras" feature of the "%{crate}" crate.

%package     -n %{name}+huge-tables-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+huge-tables-devel

This package contains library source intended for building other packages which
use the "huge-tables" feature of the "%{crate}" crate.

%package     -n %{name}+i-implement-a-third-party-backend-and-opt-into-breaking-changes-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+i-implement-a-third-party-backend-and-opt-into-breaking-changes-devel

This package contains library source intended for building other packages which
use the "i-implement-a-third-party-backend-and-opt-into-breaking-changes" feature of the "%{crate}" crate.

%package     -n %{name}+ipnet-address-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+ipnet-address-devel

This package contains library source intended for building other packages which
use the "ipnet-address" feature of the "%{crate}" crate.

%package     -n %{name}+large-tables-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+large-tables-devel

This package contains library source intended for building other packages which
use the "large-tables" feature of the "%{crate}" crate.

%package     -n %{name}+mysql-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+mysql-devel

This package contains library source intended for building other packages which
use the "mysql" feature of the "%{crate}" crate.

%package     -n %{name}+mysql_backend-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+mysql_backend-devel

This package contains library source intended for building other packages which
use the "mysql_backend" feature of the "%{crate}" crate.

%package     -n %{name}+mysqlclient-src-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+mysqlclient-src-devel

This package contains library source intended for building other packages which
use the "mysqlclient-src" feature of the "%{crate}" crate.

%package     -n %{name}+network-address-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+network-address-devel

This package contains library source intended for building other packages which
use the "network-address" feature of the "%{crate}" crate.

%package     -n %{name}+numeric-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+numeric-devel

This package contains library source intended for building other packages which
use the "numeric" feature of the "%{crate}" crate.

%package     -n %{name}+postgres-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+postgres-devel

This package contains library source intended for building other packages which
use the "postgres" feature of the "%{crate}" crate.

%package     -n %{name}+postgres_backend-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+postgres_backend-devel

This package contains library source intended for building other packages which
use the "postgres_backend" feature of the "%{crate}" crate.

%package     -n %{name}+pq-src-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+pq-src-devel

This package contains library source intended for building other packages which
use the "pq-src" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+r2d2-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+r2d2-devel

This package contains library source intended for building other packages which
use the "r2d2" feature of the "%{crate}" crate.

%package     -n %{name}+returning_clauses_for_sqlite_3_35-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+returning_clauses_for_sqlite_3_35-devel

This package contains library source intended for building other packages which
use the "returning_clauses_for_sqlite_3_35" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+with-deprecated-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+with-deprecated-devel

This package contains library source intended for building other packages which
use the "with-deprecated" feature of the "%{crate}" crate.

%package     -n %{name}+without-deprecated-devel
Summary:        A safe, extensible ORM and Query Builder for PostgreSQL, SQLite, and...
BuildArch:      noarch
%description -n %{name}+without-deprecated-devel

This package contains library source intended for building other packages which
use the "without-deprecated" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-diesel-devel -f %{oreon_filedir}/rust-diesel-devel.list

%changelog

%autochangelog
