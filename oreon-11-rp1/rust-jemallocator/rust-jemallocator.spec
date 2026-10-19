%global source0_hash a0de374a9f8e63150e6f5e8a60cc14c668226d7a347d8aee1a45766e3c4dd3bc
%bcond check 0
%global debug_package %{nil}
%global crate jemallocator
Name:           rust-jemallocator
Version:        0.5.4
Release:        1%{?dist}
Summary:        A Rust allocator backed by jemalloc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jemallocator
Source0:        https://static.crates.io/crates/jemallocator/jemallocator-%{version}.crate
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
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc_trait-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+alloc_trait-devel

This package contains library source intended for building other packages which
use the "alloc_trait" feature of the "%{crate}" crate.

%package     -n %{name}+background_threads-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+background_threads-devel

This package contains library source intended for building other packages which
use the "background_threads" feature of the "%{crate}" crate.

%package     -n %{name}+background_threads_runtime_support-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+background_threads_runtime_support-devel

This package contains library source intended for building other packages which
use the "background_threads_runtime_support" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+disable_initial_exec_tls-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+disable_initial_exec_tls-devel

This package contains library source intended for building other packages which
use the "disable_initial_exec_tls" feature of the "%{crate}" crate.

%package     -n %{name}+profiling-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+profiling-devel

This package contains library source intended for building other packages which
use the "profiling" feature of the "%{crate}" crate.

%package     -n %{name}+stats-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+stats-devel

This package contains library source intended for building other packages which
use the "stats" feature of the "%{crate}" crate.

%package     -n %{name}+unprefixed_malloc_on_supported_platforms-devel
Summary:        A Rust allocator backed by jemalloc
BuildArch:      noarch
%description -n %{name}+unprefixed_malloc_on_supported_platforms-devel

This package contains library source intended for building other packages which
use the "unprefixed_malloc_on_supported_platforms" feature of the "%{crate}" crate.

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
%files -n rust-jemallocator-devel -f %{oreon_filedir}/rust-jemallocator-devel.list

%changelog

%autochangelog
