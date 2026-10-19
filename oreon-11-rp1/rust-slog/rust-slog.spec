%global source0_hash 9b3b8565691b22d2bdfc066426ed48f837fc0c5f2c8cad8d9718f7f99d6995c1
%bcond check 0
%global debug_package %{nil}
%global crate slog
Name:           rust-slog
Version:        2.8.2
Release:        1%{?dist}
Summary:        Structured, extensible, composable logging for Rust
License:        MPL-2.0 OR MIT OR Apache-2.0
URL:            https://crates.io/crates/slog
Source0:        https://static.crates.io/crates/slog/slog-%{version}.crate
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
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+anyhow-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+anyhow-devel

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic-keys-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+dynamic-keys-devel

This package contains library source intended for building other packages which
use the "dynamic-keys" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_debug-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+max_level_debug-devel

This package contains library source intended for building other packages which
use the "max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_error-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+max_level_error-devel

This package contains library source intended for building other packages which
use the "max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_info-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+max_level_info-devel

This package contains library source intended for building other packages which
use the "max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_off-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+max_level_off-devel

This package contains library source intended for building other packages which
use the "max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_trace-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+max_level_trace-devel

This package contains library source intended for building other packages which
use the "max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_warn-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+max_level_warn-devel

This package contains library source intended for building other packages which
use the "max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+nested-values-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+nested-values-devel

This package contains library source intended for building other packages which
use the "nested-values" feature of the "%{crate}" crate.

%package     -n %{name}+nothreads-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+nothreads-devel

This package contains library source intended for building other packages which
use the "nothreads" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot_0_12-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+parking_lot_0_12-devel

This package contains library source intended for building other packages which
use the "parking_lot_0_12" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_debug-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_debug-devel

This package contains library source intended for building other packages which
use the "release_max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_error-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_error-devel

This package contains library source intended for building other packages which
use the "release_max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_info-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_info-devel

This package contains library source intended for building other packages which
use the "release_max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_off-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_off-devel

This package contains library source intended for building other packages which
use the "release_max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_trace-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_trace-devel

This package contains library source intended for building other packages which
use the "release_max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_warn-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_warn-devel

This package contains library source intended for building other packages which
use the "release_max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Structured, extensible, composable logging for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-slog-devel -f %{oreon_filedir}/rust-slog-devel.list

%changelog

%autochangelog
