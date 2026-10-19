%global source0_hash 3fbf2ae1b8bc8e02df939598064d22402220cd5bbcca1c76f7d6a310974d5615
%bcond check 0
%global debug_package %{nil}
%global crate schemars
Name:           rust-schemars0.8
Version:        0.8.22
Release:        1%{?dist}
Summary:        Generate JSON Schemas from Rust code
License:        MIT
URL:            https://crates.io/crates/schemars
Source0:        https://static.crates.io/crates/schemars/schemars-%{version}.crate
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
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec05-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+arrayvec05-devel

This package contains library source intended for building other packages which
use the "arrayvec05" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec07-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+arrayvec07-devel

This package contains library source intended for building other packages which
use the "arrayvec07" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal03-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+bigdecimal03-devel

This package contains library source intended for building other packages which
use the "bigdecimal03" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal04-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+bigdecimal04-devel

This package contains library source intended for building other packages which
use the "bigdecimal04" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+derive_json_schema-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+derive_json_schema-devel

This package contains library source intended for building other packages which
use the "derive_json_schema" feature of the "%{crate}" crate.

%package     -n %{name}+either-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+enumset-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+enumset-devel

This package contains library source intended for building other packages which
use the "enumset" feature of the "%{crate}" crate.

%package     -n %{name}+impl_json_schema-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+impl_json_schema-devel

This package contains library source intended for building other packages which
use the "impl_json_schema" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+indexmap1-devel

This package contains library source intended for building other packages which
use the "indexmap1" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap2-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+indexmap2-devel

This package contains library source intended for building other packages which
use the "indexmap2" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+raw_value-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+raw_value-devel

This package contains library source intended for building other packages which
use the "raw_value" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+schemars_derive-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+schemars_derive-devel

This package contains library source intended for building other packages which
use the "schemars_derive" feature of the "%{crate}" crate.

%package     -n %{name}+semver-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+semver-devel

This package contains library source intended for building other packages which
use the "semver" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+smol_str-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+smol_str-devel

This package contains library source intended for building other packages which
use the "smol_str" feature of the "%{crate}" crate.

%package     -n %{name}+ui_test-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+ui_test-devel

This package contains library source intended for building other packages which
use the "ui_test" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+uuid08-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+uuid08-devel

This package contains library source intended for building other packages which
use the "uuid08" feature of the "%{crate}" crate.

%package     -n %{name}+uuid1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+uuid1-devel

This package contains library source intended for building other packages which
use the "uuid1" feature of the "%{crate}" crate.

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
%files -n rust-schemars0.8-devel -f %{oreon_filedir}/rust-schemars0.8-devel.list

%changelog

%autochangelog
