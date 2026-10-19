%global source0_hash cd8aa5b2ab86a2cefa406d889139c162cbb230092f7d1d7cbc1716405d852a3b
%bcond check 1
%global debug_package %{nil}
%global crate tikv-jemalloc-sys
%global crate_version 0.6.1+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-tikv-jemalloc-sys
Version:        0.6.1
Release:        1%{?dist}
Summary:        Rust FFI bindings to jemalloc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tikv-jemalloc-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          tikv-jemalloc-sys-fix-metadata-auto.diff
Patch10:        0001-Downstream-only-always-use-the-system-jemalloc.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(jemalloc)
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
use the "background_threads_runtime_support" feature of the
"%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+override_allocator_on_supported_platforms-devel
Summary:        Rust FFI bindings to jemalloc
BuildArch:      noarch
%description -n %{name}+override_allocator_on_supported_platforms-devel

This package contains library source intended for building other packages which
use the "override_allocator_on_supported_platforms" feature of the
"%{crate}" crate.

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
use the "unprefixed_malloc_on_supported_platforms" feature of the
"%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
rm -rv jemalloc
rm -rv configure
tomcli set Cargo.toml append features.default \
unprefixed_malloc_on_supported_platforms
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
%files -n rust-tikv-jemalloc-sys-devel -f %{oreon_filedir}/rust-tikv-jemalloc-sys-devel.list

%changelog

%autochangelog
