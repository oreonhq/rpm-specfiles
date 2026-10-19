%global source0_hash 19a9c1841124ac5a61741f96e1d9e2ec77424bf323962dd894bdb93f37d5219b
%bcond check 1
%global debug_package %{nil}
%global crate sqlx-macros-core
Name:           rust-sqlx-macros-core
Version:        0.8.6
Release:        1%{?dist}
Summary:        Macro support core for SQLx, the Rust SQL toolkit
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-macros-core
Source0:        https://static.crates.io/crates/sqlx-macros-core/sqlx-macros-core-%{version}.crate
Patch:          sqlx-macros-core-fix-metadata.diff
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
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_rt-async-std-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+_rt-async-std-devel

This package contains library source intended for building other packages which
use the "_rt-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+_rt-tokio-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+_rt-tokio-devel

This package contains library source intended for building other packages which
use the "_rt-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+_sqlite-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+_sqlite-devel

This package contains library source intended for building other packages which
use the "_sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-native-tls-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+_tls-native-tls-devel

This package contains library source intended for building other packages which
use the "_tls-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-rustls-ring-native-roots-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+_tls-rustls-ring-native-roots-devel

This package contains library source intended for building other packages which
use the "_tls-rustls-ring-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+_tls-rustls-ring-webpki-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+_tls-rustls-ring-webpki-devel

This package contains library source intended for building other packages which
use the "_tls-rustls-ring-webpki" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+ipnet-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+ipnet-devel

This package contains library source intended for building other packages which
use the "ipnet" feature of the "%{crate}" crate.

%package     -n %{name}+ipnetwork-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+ipnetwork-devel

This package contains library source intended for building other packages which
use the "ipnetwork" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+mac_address-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+mac_address-devel

This package contains library source intended for building other packages which
use the "mac_address" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+migrate-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+migrate-devel

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%package     -n %{name}+mysql-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+mysql-devel

This package contains library source intended for building other packages which
use the "mysql" feature of the "%{crate}" crate.

%package     -n %{name}+postgres-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+postgres-devel

This package contains library source intended for building other packages which
use the "postgres" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-unbundled-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+sqlite-unbundled-devel

This package contains library source intended for building other packages which
use the "sqlite-unbundled" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-mysql-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-mysql-devel

This package contains library source intended for building other packages which
use the "sqlx-mysql" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-postgres-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-postgres-devel

This package contains library source intended for building other packages which
use the "sqlx-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-sqlite-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-sqlite-devel

This package contains library source intended for building other packages which
use the "sqlx-sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Macro support core for SQLx, the Rust SQL toolkit
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

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
%files -n rust-sqlx-macros-core-devel -f %{oreon_filedir}/rust-sqlx-macros-core-devel.list

%changelog

%autochangelog
