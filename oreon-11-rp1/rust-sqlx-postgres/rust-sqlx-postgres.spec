%global source0_hash db58fcd5a53cf07c184b154801ff91347e4c30d17a3562a635ff028ad5deda46
%bcond check 0
%global debug_package %{nil}
%global crate sqlx-postgres
Name:           rust-sqlx-postgres
Version:        0.8.6
Release:        1%{?dist}
Summary:        PostgreSQL driver implementation for SQLx
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-postgres
Source0:        https://static.crates.io/crates/sqlx-postgres/sqlx-postgres-%{version}.crate
Patch:          sqlx-postgres-fix-metadata-auto.diff
Patch:          sqlx-postgres-fix-metadata.diff
Patch10:        sqlx-postgres-0.8.6-whoami2.patch
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
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+any-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+any-devel

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+ipnet-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+ipnet-devel

This package contains library source intended for building other packages which
use the "ipnet" feature of the "%{crate}" crate.

%package     -n %{name}+ipnetwork-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+ipnetwork-devel

This package contains library source intended for building other packages which
use the "ipnetwork" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+mac_address-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+mac_address-devel

This package contains library source intended for building other packages which
use the "mac_address" feature of the "%{crate}" crate.

%package     -n %{name}+migrate-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+migrate-devel

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%package     -n %{name}+offline-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+offline-devel

This package contains library source intended for building other packages which
use the "offline" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        PostgreSQL driver implementation for SQLx
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sqlx-postgres-devel -f %{oreon_filedir}/rust-sqlx-postgres-devel.list

%changelog

%autochangelog
