%global source0_hash 851ca9db4932932d69f3ea811b1abe63087a0f740a47692619dd40d4899b68be
%bcond check 0
%global debug_package %{nil}
%global crate postgres-types
Name:           rust-postgres-types
Version:        0.2.14
Release:        1%{?dist}
Summary:        Conversions between Rust and Postgres values
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postgres-types
Source0:        https://static.crates.io/crates/postgres-types/postgres-types-%{version}.crate
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

%package     -n %{name}+array-impls-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+array-impls-devel

This package contains library source intended for building other packages which
use the "array-impls" feature of the "%{crate}" crate.

%package     -n %{name}+array-init-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+array-init-devel

This package contains library source intended for building other packages which
use the "array-init" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-06-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+bit-vec-06-devel

This package contains library source intended for building other packages which
use the "bit-vec-06" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-07-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+bit-vec-07-devel

This package contains library source intended for building other packages which
use the "bit-vec-07" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-08-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+bit-vec-08-devel

This package contains library source intended for building other packages which
use the "bit-vec-08" feature of the "%{crate}" crate.

%package     -n %{name}+bit-vec-09-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+bit-vec-09-devel

This package contains library source intended for building other packages which
use the "bit-vec-09" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-04-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+chrono-04-devel

This package contains library source intended for building other packages which
use the "chrono-04" feature of the "%{crate}" crate.

%package     -n %{name}+cidr-02-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+cidr-02-devel

This package contains library source intended for building other packages which
use the "cidr-02" feature of the "%{crate}" crate.

%package     -n %{name}+cidr-03-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+cidr-03-devel

This package contains library source intended for building other packages which
use the "cidr-03" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+eui48-04-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+eui48-04-devel

This package contains library source intended for building other packages which
use the "eui48-04" feature of the "%{crate}" crate.

%package     -n %{name}+eui48-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+eui48-1-devel

This package contains library source intended for building other packages which
use the "eui48-1" feature of the "%{crate}" crate.

%package     -n %{name}+geo-types-06-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+geo-types-06-devel

This package contains library source intended for building other packages which
use the "geo-types-06" feature of the "%{crate}" crate.

%package     -n %{name}+geo-types-0_7-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+geo-types-0_7-devel

This package contains library source intended for building other packages which
use the "geo-types-0_7" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-01-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+jiff-01-devel

This package contains library source intended for building other packages which
use the "jiff-01" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-02-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+jiff-02-devel

This package contains library source intended for building other packages which
use the "jiff-02" feature of the "%{crate}" crate.

%package     -n %{name}+js-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+js-devel

This package contains library source intended for building other packages which
use the "js" feature of the "%{crate}" crate.

%package     -n %{name}+postgres-derive-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+postgres-derive-devel

This package contains library source intended for building other packages which
use the "postgres-derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+serde-1-devel

This package contains library source intended for building other packages which
use the "serde-1" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+serde_json-1-devel

This package contains library source intended for building other packages which
use the "serde_json-1" feature of the "%{crate}" crate.

%package     -n %{name}+smol_str-01-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+smol_str-01-devel

This package contains library source intended for building other packages which
use the "smol_str-01" feature of the "%{crate}" crate.

%package     -n %{name}+time-02-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+time-02-devel

This package contains library source intended for building other packages which
use the "time-02" feature of the "%{crate}" crate.

%package     -n %{name}+time-03-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+time-03-devel

This package contains library source intended for building other packages which
use the "time-03" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-08-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+uuid-08-devel

This package contains library source intended for building other packages which
use the "uuid-08" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+uuid-1-devel

This package contains library source intended for building other packages which
use the "uuid-1" feature of the "%{crate}" crate.

%package     -n %{name}+with-bit-vec-0_6-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-bit-vec-0_6-devel

This package contains library source intended for building other packages which
use the "with-bit-vec-0_6" feature of the "%{crate}" crate.

%package     -n %{name}+with-bit-vec-0_7-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-bit-vec-0_7-devel

This package contains library source intended for building other packages which
use the "with-bit-vec-0_7" feature of the "%{crate}" crate.

%package     -n %{name}+with-bit-vec-0_8-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-bit-vec-0_8-devel

This package contains library source intended for building other packages which
use the "with-bit-vec-0_8" feature of the "%{crate}" crate.

%package     -n %{name}+with-bit-vec-0_9-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-bit-vec-0_9-devel

This package contains library source intended for building other packages which
use the "with-bit-vec-0_9" feature of the "%{crate}" crate.

%package     -n %{name}+with-chrono-0_4-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-chrono-0_4-devel

This package contains library source intended for building other packages which
use the "with-chrono-0_4" feature of the "%{crate}" crate.

%package     -n %{name}+with-cidr-0_2-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-cidr-0_2-devel

This package contains library source intended for building other packages which
use the "with-cidr-0_2" feature of the "%{crate}" crate.

%package     -n %{name}+with-cidr-0_3-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-cidr-0_3-devel

This package contains library source intended for building other packages which
use the "with-cidr-0_3" feature of the "%{crate}" crate.

%package     -n %{name}+with-eui48-0_4-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-eui48-0_4-devel

This package contains library source intended for building other packages which
use the "with-eui48-0_4" feature of the "%{crate}" crate.

%package     -n %{name}+with-eui48-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-eui48-1-devel

This package contains library source intended for building other packages which
use the "with-eui48-1" feature of the "%{crate}" crate.

%package     -n %{name}+with-geo-types-0_6-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-geo-types-0_6-devel

This package contains library source intended for building other packages which
use the "with-geo-types-0_6" feature of the "%{crate}" crate.

%package     -n %{name}+with-geo-types-0_7-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-geo-types-0_7-devel

This package contains library source intended for building other packages which
use the "with-geo-types-0_7" feature of the "%{crate}" crate.

%package     -n %{name}+with-jiff-0_1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-jiff-0_1-devel

This package contains library source intended for building other packages which
use the "with-jiff-0_1" feature of the "%{crate}" crate.

%package     -n %{name}+with-jiff-0_2-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-jiff-0_2-devel

This package contains library source intended for building other packages which
use the "with-jiff-0_2" feature of the "%{crate}" crate.

%package     -n %{name}+with-serde_json-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-serde_json-1-devel

This package contains library source intended for building other packages which
use the "with-serde_json-1" feature of the "%{crate}" crate.

%package     -n %{name}+with-smol_str-01-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-smol_str-01-devel

This package contains library source intended for building other packages which
use the "with-smol_str-01" feature of the "%{crate}" crate.

%package     -n %{name}+with-time-0_2-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-time-0_2-devel

This package contains library source intended for building other packages which
use the "with-time-0_2" feature of the "%{crate}" crate.

%package     -n %{name}+with-time-0_3-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-time-0_3-devel

This package contains library source intended for building other packages which
use the "with-time-0_3" feature of the "%{crate}" crate.

%package     -n %{name}+with-uuid-0_8-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-uuid-0_8-devel

This package contains library source intended for building other packages which
use the "with-uuid-0_8" feature of the "%{crate}" crate.

%package     -n %{name}+with-uuid-1-devel
Summary:        Conversions between Rust and Postgres values
BuildArch:      noarch
%description -n %{name}+with-uuid-1-devel

This package contains library source intended for building other packages which
use the "with-uuid-1" feature of the "%{crate}" crate.

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
%files -n rust-postgres-types-devel -f %{oreon_filedir}/rust-postgres-types-devel.list

%changelog

%autochangelog
