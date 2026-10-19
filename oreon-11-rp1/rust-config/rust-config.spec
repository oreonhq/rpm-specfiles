%global source0_hash b85f248a4de22d204ceabc6299d89d2c70fbd7f09fea53c06c852369652d8139
%bcond check 0
%global debug_package %{nil}
%global crate config
Name:           rust-config
Version:        0.15.25
Release:        1%{?dist}
Summary:        Layered configuration system for Rust applications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/config
Source0:        https://static.crates.io/crates/config/config-%{version}.crate
Patch:          config-fix-metadata.diff
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
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+convert-case-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+convert-case-devel

This package contains library source intended for building other packages which
use the "convert-case" feature of the "%{crate}" crate.

%package     -n %{name}+convert_case-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+convert_case-devel

This package contains library source intended for building other packages which
use the "convert_case" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+ini-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+ini-devel

This package contains library source intended for building other packages which
use the "ini" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+json5-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+json5-devel

This package contains library source intended for building other packages which
use the "json5" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+ron-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+ron-devel

This package contains library source intended for building other packages which
use the "ron" feature of the "%{crate}" crate.

%package     -n %{name}+rust-ini-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+rust-ini-devel

This package contains library source intended for building other packages which
use the "rust-ini" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-rust2-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+yaml-rust2-devel

This package contains library source intended for building other packages which
use the "yaml-rust2" feature of the "%{crate}" crate.

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
%files -n rust-config-devel -f %{oreon_filedir}/rust-config-devel.list

%changelog

%autochangelog
