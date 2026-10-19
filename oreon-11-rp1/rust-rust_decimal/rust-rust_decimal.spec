%global source0_hash 7653272e75dcac41dc199fbea6f5797633994fafd339943c06c9af16bf29cd3a
%bcond check 0
%global debug_package %{nil}
%global crate rust_decimal
Name:           rust-rust_decimal
Version:        1.43.0
Release:        1%{?dist}
Summary:        Decimal number implementation written in pure Rust suitable for finan...
License:        MIT
URL:            https://crates.io/crates/rust_decimal
Source0:        https://static.crates.io/crates/rust_decimal/rust_decimal-%{version}.crate
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
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+align16-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+align16-devel

This package contains library source intended for building other packages which
use the "align16" feature of the "%{crate}" crate.

%package     -n %{name}+borsh-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+borsh-devel

This package contains library source intended for building other packages which
use the "borsh" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+c-repr-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+c-repr-devel

This package contains library source intended for building other packages which
use the "c-repr" feature of the "%{crate}" crate.

%package     -n %{name}+db-diesel-mysql-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+db-diesel-mysql-devel

This package contains library source intended for building other packages which
use the "db-diesel-mysql" feature of the "%{crate}" crate.

%package     -n %{name}+db-diesel-postgres-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+db-diesel-postgres-devel

This package contains library source intended for building other packages which
use the "db-diesel-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+db-diesel2-mysql-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+db-diesel2-mysql-devel

This package contains library source intended for building other packages which
use the "db-diesel2-mysql" feature of the "%{crate}" crate.

%package     -n %{name}+db-diesel2-postgres-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+db-diesel2-postgres-devel

This package contains library source intended for building other packages which
use the "db-diesel2-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+db-postgres-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+db-postgres-devel

This package contains library source intended for building other packages which
use the "db-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+db-tokio-postgres-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+db-tokio-postgres-devel

This package contains library source intended for building other packages which
use the "db-tokio-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+diesel-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+diesel-devel

This package contains library source intended for building other packages which
use the "diesel" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-ops-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+legacy-ops-devel

This package contains library source intended for building other packages which
use the "legacy-ops" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+maths-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+maths-devel

This package contains library source intended for building other packages which
use the "maths" feature of the "%{crate}" crate.

%package     -n %{name}+maths-nopanic-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+maths-nopanic-devel

This package contains library source intended for building other packages which
use the "maths-nopanic" feature of the "%{crate}" crate.

%package     -n %{name}+ndarray-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+ndarray-devel

This package contains library source intended for building other packages which
use the "ndarray" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rand-0_9-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+rand-0_9-devel

This package contains library source intended for building other packages which
use the "rand-0_9" feature of the "%{crate}" crate.

%package     -n %{name}+rocket-traits-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+rocket-traits-devel

This package contains library source intended for building other packages which
use the "rocket-traits" feature of the "%{crate}" crate.

%package     -n %{name}+rust-fuzz-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+rust-fuzz-devel

This package contains library source intended for building other packages which
use the "rust-fuzz" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-arbitrary-precision-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-arbitrary-precision-devel

This package contains library source intended for building other packages which
use the "serde-arbitrary-precision" feature of the "%{crate}" crate.

%package     -n %{name}+serde-bincode-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-bincode-devel

This package contains library source intended for building other packages which
use the "serde-bincode" feature of the "%{crate}" crate.

%package     -n %{name}+serde-float-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-float-devel

This package contains library source intended for building other packages which
use the "serde-float" feature of the "%{crate}" crate.

%package     -n %{name}+serde-str-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-str-devel

This package contains library source intended for building other packages which
use the "serde-str" feature of the "%{crate}" crate.

%package     -n %{name}+serde-with-arbitrary-precision-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-with-arbitrary-precision-devel

This package contains library source intended for building other packages which
use the "serde-with-arbitrary-precision" feature of the "%{crate}" crate.

%package     -n %{name}+serde-with-float-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-with-float-devel

This package contains library source intended for building other packages which
use the "serde-with-float" feature of the "%{crate}" crate.

%package     -n %{name}+serde-with-str-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde-with-str-devel

This package contains library source intended for building other packages which
use the "serde-with-str" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-pg-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+tokio-pg-devel

This package contains library source intended for building other packages which
use the "tokio-pg" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-postgres-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+tokio-postgres-devel

This package contains library source intended for building other packages which
use the "tokio-postgres" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%package     -n %{name}+zmij-devel
Summary:        Decimal number implementation written in pure Rust suitable for finan...
BuildArch:      noarch
%description -n %{name}+zmij-devel

This package contains library source intended for building other packages which
use the "zmij" feature of the "%{crate}" crate.

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
%files -n rust-rust_decimal-devel -f %{oreon_filedir}/rust-rust_decimal-devel.list

%changelog

%autochangelog
