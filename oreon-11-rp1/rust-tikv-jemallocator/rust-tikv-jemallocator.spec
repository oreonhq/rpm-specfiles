%global source0_hash 249f09e49ab1609436f34c776e84231bead18d6a955f119f939bdc1d847561bd
%bcond check 1
%global debug_package %{nil}
%global crate tikv-jemallocator
Name:           rust-tikv-jemallocator
Version:        0.7.0
Release:        1%{?dist}
Summary:        Rust allocator backed by jemalloc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tikv-jemallocator
Source0:        https://static.crates.io/crates/tikv-jemallocator/tikv-jemallocator-%{version}.crate
Patch:          tikv-jemallocator-fix-metadata.diff
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
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc_trait-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+alloc_trait-devel

This package contains library source intended for building other packages which
use the "alloc_trait" feature of the "%{crate}" crate.

%package     -n %{name}+background_threads-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+background_threads-devel

This package contains library source intended for building other packages which
use the "background_threads" feature of the "%{crate}" crate.

%package     -n %{name}+background_threads_runtime_support-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+background_threads_runtime_support-devel

This package contains library source intended for building other packages which
use the "background_threads_runtime_support" feature of the
"%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+override_allocator_on_supported_platforms-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+override_allocator_on_supported_platforms-devel

This package contains library source intended for building other packages which
use the "override_allocator_on_supported_platforms" feature of the
"%{crate}" crate.

%package     -n %{name}+profiling-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+profiling-devel

This package contains library source intended for building other packages which
use the "profiling" feature of the "%{crate}" crate.

%package     -n %{name}+stats-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+stats-devel

This package contains library source intended for building other packages which
use the "stats" feature of the "%{crate}" crate.

%package     -n %{name}+unprefixed_malloc_on_supported_platforms-devel
Summary:        Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+unprefixed_malloc_on_supported_platforms-devel

This package contains library source intended for building other packages which
use the "unprefixed_malloc_on_supported_platforms" feature of the
"%{crate}" crate.

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
%files -n rust-tikv-jemallocator-devel -f %{oreon_filedir}/rust-tikv-jemallocator-devel.list

%changelog

%autochangelog
