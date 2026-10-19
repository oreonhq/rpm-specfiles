%global source0_hash 378620ccc25c62c89d8be1c819e76a88d59bdcc3304733330788948e619bfd71
%bcond check 1
%global debug_package %{nil}
%global crate sqlx
Name:           rust-sqlx
Version:        0.9.0
Release:        1%{?dist}
Summary:        🧰 The Rust SQL Toolkit
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx
Source0:        https://static.crates.io/crates/sqlx/sqlx-%{version}.crate
Patch:          sqlx-fix-metadata-auto.diff
Patch:          sqlx-fix-metadata.diff
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
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_rt-async-std-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+_rt-async-std-devel

This package contains library source intended for building other packages which
use the "_rt-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+_rt-tokio-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+_rt-tokio-devel

This package contains library source intended for building other packages which
use the "_rt-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+_sqlite-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+_sqlite-devel

This package contains library source intended for building other packages which
use the "_sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+_unstable-all-types-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+_unstable-all-types-devel

This package contains library source intended for building other packages which
use the "_unstable-all-types" feature of the "%{crate}" crate.

%package     -n %{name}+all-databases-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+all-databases-devel

This package contains library source intended for building other packages which
use the "all-databases" feature of the "%{crate}" crate.

%package     -n %{name}+any-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+any-devel

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+bit-vec-devel

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%package     -n %{name}+bstr-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+bstr-devel

This package contains library source intended for building other packages which
use the "bstr" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+ipnet-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+ipnet-devel

This package contains library source intended for building other packages which
use the "ipnet" feature of the "%{crate}" crate.

%package     -n %{name}+ipnetwork-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+ipnetwork-devel

This package contains library source intended for building other packages which
use the "ipnetwork" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+mac_address-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+mac_address-devel

This package contains library source intended for building other packages which
use the "mac_address" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+migrate-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+migrate-devel

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%package     -n %{name}+mysql-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+mysql-devel

This package contains library source intended for building other packages which
use the "mysql" feature of the "%{crate}" crate.

%package     -n %{name}+postgres-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+postgres-devel

This package contains library source intended for building other packages which
use the "postgres" feature of the "%{crate}" crate.

%package     -n %{name}+regexp-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+regexp-devel

This package contains library source intended for building other packages which
use the "regexp" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-async-std-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+runtime-async-std-devel

This package contains library source intended for building other packages which
use the "runtime-async-std" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-async-std-native-tls-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+runtime-async-std-native-tls-devel

This package contains library source intended for building other packages which
use the "runtime-async-std-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-async-std-rustls-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+runtime-async-std-rustls-devel

This package contains library source intended for building other packages which
use the "runtime-async-std-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-tokio-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+runtime-tokio-devel

This package contains library source intended for building other packages which
use the "runtime-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-tokio-native-tls-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+runtime-tokio-native-tls-devel

This package contains library source intended for building other packages which
use the "runtime-tokio-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-tokio-rustls-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+runtime-tokio-rustls-devel

This package contains library source intended for building other packages which
use the "runtime-tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlite-devel

This package contains library source intended for building other packages which
use the "sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-preupdate-hook-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlite-preupdate-hook-devel

This package contains library source intended for building other packages which
use the "sqlite-preupdate-hook" feature of the "%{crate}" crate.

%package     -n %{name}+sqlite-unbundled-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlite-unbundled-devel

This package contains library source intended for building other packages which
use the "sqlite-unbundled" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-macros-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-macros-devel

This package contains library source intended for building other packages which
use the "sqlx-macros" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-mysql-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-mysql-devel

This package contains library source intended for building other packages which
use the "sqlx-mysql" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-postgres-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-postgres-devel

This package contains library source intended for building other packages which
use the "sqlx-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+sqlx-sqlite-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+sqlx-sqlite-devel

This package contains library source intended for building other packages which
use the "sqlx-sqlite" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tls-native-tls-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+tls-native-tls-devel

This package contains library source intended for building other packages which
use the "tls-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-none-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+tls-none-devel

This package contains library source intended for building other packages which
use the "tls-none" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+tls-rustls-devel

This package contains library source intended for building other packages which
use the "tls-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-ring-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+tls-rustls-ring-devel

This package contains library source intended for building other packages which
use the "tls-rustls-ring" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-ring-native-roots-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+tls-rustls-ring-native-roots-devel

This package contains library source intended for building other packages which
use the "tls-rustls-ring-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+tls-rustls-ring-webpki-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+tls-rustls-ring-webpki-devel

This package contains library source intended for building other packages which
use the "tls-rustls-ring-webpki" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        🧰 The Rust SQL Toolkit
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rf contrib gen-changelog.sh rust-toolchain.toml
rm -rf examples
rm -rf tests
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --doc
%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sqlx-devel -f %{oreon_filedir}/rust-sqlx-devel.list

%changelog

%autochangelog
