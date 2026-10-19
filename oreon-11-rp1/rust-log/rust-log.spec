%global source0_hash f9f8bd3e56ce4dfc153cf470fffbfa98c7620958b312ca5c3a4b8d5181fd13c6
%bcond check 1
%global debug_package %{nil}
%global crate log
Name:           rust-log
Version:        0.4.34
Release:        1%{?dist}
Summary:        Lightweight logging facade for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/log
Source0:        https://static.crates.io/crates/log/log-%{version}.crate
Patch:          log-fix-metadata.diff
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
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+kv-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+kv-devel

This package contains library source intended for building other packages which
use the "kv" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_debug-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_debug-devel

This package contains library source intended for building other packages which
use the "max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_error-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_error-devel

This package contains library source intended for building other packages which
use the "max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_info-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_info-devel

This package contains library source intended for building other packages which
use the "max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_off-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_off-devel

This package contains library source intended for building other packages which
use the "max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_trace-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_trace-devel

This package contains library source intended for building other packages which
use the "max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+max_level_warn-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+max_level_warn-devel

This package contains library source intended for building other packages which
use the "max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_debug-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_debug-devel

This package contains library source intended for building other packages which
use the "release_max_level_debug" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_error-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_error-devel

This package contains library source intended for building other packages which
use the "release_max_level_error" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_info-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_info-devel

This package contains library source intended for building other packages which
use the "release_max_level_info" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_off-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_off-devel

This package contains library source intended for building other packages which
use the "release_max_level_off" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_trace-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_trace-devel

This package contains library source intended for building other packages which
use the "release_max_level_trace" feature of the "%{crate}" crate.

%package     -n %{name}+release_max_level_warn-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+release_max_level_warn-devel

This package contains library source intended for building other packages which
use the "release_max_level_warn" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_core-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+serde_core-devel

This package contains library source intended for building other packages which
use the "serde_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Lightweight logging facade for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%files -n rust-log-devel -f %{oreon_filedir}/rust-log-devel.list

%changelog

%autochangelog
