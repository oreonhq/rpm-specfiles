%global source0_hash 4b067c0c11094aef6b7a801c1e34a26affafdf3d051dba08456b868789aaf9a4
%bcond check 0
%global debug_package %{nil}
%global crate wasm-bindgen
Name:           rust-wasm-bindgen
Version:        0.2.126
Release:        1%{?dist}
Summary:        Easy support for interacting between JS and Rust.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wasm-bindgen
Source0:        https://static.crates.io/crates/wasm-bindgen/wasm-bindgen-%{version}.crate
Patch:          wasm-bindgen-macro-no-default-feature.patch
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
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+enable-interning-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+enable-interning-devel

This package contains library source intended for building other packages which
use the "enable-interning" feature of the "%{crate}" crate.

%package     -n %{name}+gg-alloc-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+gg-alloc-devel

This package contains library source intended for building other packages which
use the "gg-alloc" feature of the "%{crate}" crate.

%package     -n %{name}+msrv-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+msrv-devel

This package contains library source intended for building other packages which
use the "msrv" feature of the "%{crate}" crate.

%package     -n %{name}+rustversion-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+rustversion-devel

This package contains library source intended for building other packages which
use the "rustversion" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-serialize-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+serde-serialize-devel

This package contains library source intended for building other packages which
use the "serde-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+spans-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+spans-devel

This package contains library source intended for building other packages which
use the "spans" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+strict-macro-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+strict-macro-devel

This package contains library source intended for building other packages which
use the "strict-macro" feature of the "%{crate}" crate.

%package     -n %{name}+xxx_debug_only_print_generated_code-devel
Summary:        Easy support for interacting between JS and Rust.
BuildArch:      noarch
%description -n %{name}+xxx_debug_only_print_generated_code-devel

This package contains library source intended for building other packages which
use the "xxx_debug_only_print_generated_code" feature of the "%{crate}" crate.

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
%files -n rust-wasm-bindgen-devel -f %{oreon_filedir}/rust-wasm-bindgen-devel.list

%changelog

%autochangelog
