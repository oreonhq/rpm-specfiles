%global source0_hash ac6c1946e1cea1788cbfde01c993b52a10e2da07f4bac608228d1bed20bfebf2
%bcond check 0
%global debug_package %{nil}
%global crate jemalloc-sys
%global crate_version 0.5.4+5.3.0-patched
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-jemalloc-sys
Version:        0.5.4
Release:        1%{?dist}
Summary:        Rust FFI bindings to jemalloc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jemalloc-sys
Source0:        https://static.crates.io/crates/jemalloc-sys/jemalloc-sys-%{version}.crate
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
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+background_threads-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+background_threads-devel

This package contains library source intended for building other packages which
use the "background_threads" feature of the "%{crate}" crate.

%package     -n %{name}+background_threads_runtime_support-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+background_threads_runtime_support-devel

This package contains library source intended for building other packages which
use the "background_threads_runtime_support" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+disable_cache_oblivious-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+disable_cache_oblivious-devel

This package contains library source intended for building other packages which
use the "disable_cache_oblivious" feature of the "%{crate}" crate.

%package     -n %{name}+disable_initial_exec_tls-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+disable_initial_exec_tls-devel

This package contains library source intended for building other packages which
use the "disable_initial_exec_tls" feature of the "%{crate}" crate.

%package     -n %{name}+profiling-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+profiling-devel

This package contains library source intended for building other packages which
use the "profiling" feature of the "%{crate}" crate.

%package     -n %{name}+stats-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+stats-devel

This package contains library source intended for building other packages which
use the "stats" feature of the "%{crate}" crate.

%package     -n %{name}+unprefixed_malloc_on_supported_platforms-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+unprefixed_malloc_on_supported_platforms-devel

This package contains library source intended for building other packages which
use the "unprefixed_malloc_on_supported_platforms" feature of the "%{crate}" crate.

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
%files -n rust-jemalloc-sys-devel -f %{oreon_filedir}/rust-jemalloc-sys-devel.list

%changelog

%autochangelog
