%global source0_hash 4cd191f9397d57d581cddd31014772520aa448f65ef991055d7f61582c65165f
%bcond check 0
%global debug_package %{nil}
%global crate schemars
Name:           rust-schemars0.9
Version:        0.9.0
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

%package     -n %{name}+_ui_test-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+_ui_test-devel

This package contains library source intended for building other packages which
use the "_ui_test" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec07-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+arrayvec07-devel

This package contains library source intended for building other packages which
use the "arrayvec07" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal04-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+bigdecimal04-devel

This package contains library source intended for building other packages which
use the "bigdecimal04" feature of the "%{crate}" crate.

%package     -n %{name}+bytes1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+bytes1-devel

This package contains library source intended for building other packages which
use the "bytes1" feature of the "%{crate}" crate.

%package     -n %{name}+chrono04-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+chrono04-devel

This package contains library source intended for building other packages which
use the "chrono04" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+either1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+either1-devel

This package contains library source intended for building other packages which
use the "either1" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap2-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+indexmap2-devel

This package contains library source intended for building other packages which
use the "indexmap2" feature of the "%{crate}" crate.

%package     -n %{name}+jiff02-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+jiff02-devel

This package contains library source intended for building other packages which
use the "jiff02" feature of the "%{crate}" crate.

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

%package     -n %{name}+rust_decimal1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+rust_decimal1-devel

This package contains library source intended for building other packages which
use the "rust_decimal1" feature of the "%{crate}" crate.

%package     -n %{name}+schemars_derive-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+schemars_derive-devel

This package contains library source intended for building other packages which
use the "schemars_derive" feature of the "%{crate}" crate.

%package     -n %{name}+semver1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+semver1-devel

This package contains library source intended for building other packages which
use the "semver1" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec1-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+smallvec1-devel

This package contains library source intended for building other packages which
use the "smallvec1" feature of the "%{crate}" crate.

%package     -n %{name}+smol_str02-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+smol_str02-devel

This package contains library source intended for building other packages which
use the "smol_str02" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+url2-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+url2-devel

This package contains library source intended for building other packages which
use the "url2" feature of the "%{crate}" crate.

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
%files -n rust-schemars0.9-devel -f %{oreon_filedir}/rust-schemars0.9-devel.list

%changelog

%autochangelog
