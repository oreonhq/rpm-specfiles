%global source0_hash cf92845e79fc2e2def6a5d828f0801e29a2f8acc037becc5ab08595c7d5e9863
%bcond check 0
%global debug_package %{nil}
%global crate toml
%global crate_version 0.9.12+spec-1.1.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-toml0.9
Version:        0.9.12
Release:        1%{?dist}
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml
Source0:        https://static.crates.io/crates/toml/toml-%{version}.crate
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
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+anstream-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+anstream-devel

This package contains library source intended for building other packages which
use the "anstream" feature of the "%{crate}" crate.

%package     -n %{name}+anstyle-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+anstyle-devel

This package contains library source intended for building other packages which
use the "anstyle" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+fast_hash-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+fast_hash-devel

This package contains library source intended for building other packages which
use the "fast_hash" feature of the "%{crate}" crate.

%package     -n %{name}+foldhash-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+foldhash-devel

This package contains library source intended for building other packages which
use the "foldhash" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_core-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+serde_core-devel

This package contains library source intended for building other packages which
use the "serde_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+toml_parser-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+toml_parser-devel

This package contains library source intended for building other packages which
use the "toml_parser" feature of the "%{crate}" crate.

%package     -n %{name}+toml_writer-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+toml_writer-devel

This package contains library source intended for building other packages which
use the "toml_writer" feature of the "%{crate}" crate.

%package     -n %{name}+unbounded-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+unbounded-devel

This package contains library source intended for building other packages which
use the "unbounded" feature of the "%{crate}" crate.

%package     -n %{name}+winnow-devel
Summary:        A native Rust encoder and decoder of TOML-formatted files and streams...
BuildArch:      noarch
%description -n %{name}+winnow-devel

This package contains library source intended for building other packages which
use the "winnow" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-toml0.9-devel -f %{oreon_filedir}/rust-toml0.9-devel.list

%changelog

%autochangelog
