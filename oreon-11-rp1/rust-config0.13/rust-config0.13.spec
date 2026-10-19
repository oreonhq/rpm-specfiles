%global source0_hash 23738e11972c7643e4ec947840fc463b6a571afcd3e735bdfce7d03c7a784aca
%bcond check 0
%global debug_package %{nil}
%global crate config
Name:           rust-config0.13
Version:        0.13.4
Release:        1%{?dist}
Summary:        Layered configuration system for Rust applications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/config
Source0:        https://static.crates.io/crates/config/config-%{version}.crate
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

%package     -n %{name}+json5_rs-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+json5_rs-devel

This package contains library source intended for building other packages which
use the "json5_rs" feature of the "%{crate}" crate.

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

%package     -n %{name}+yaml-rust-devel
Summary:        Layered configuration system for Rust applications
BuildArch:      noarch
%description -n %{name}+yaml-rust-devel

This package contains library source intended for building other packages which
use the "yaml-rust" feature of the "%{crate}" crate.

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
%files -n rust-config0.13-devel -f %{oreon_filedir}/rust-config0.13-devel.list

%changelog

%autochangelog
