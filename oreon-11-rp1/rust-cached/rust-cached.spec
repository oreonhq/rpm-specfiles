%global source0_hash c5a6cf8262820194a1488ece477f5fb5ba9256ef25229d525470e71d6e9a5835
%bcond check 1
%global debug_package %{nil}
%global crate cached
Name:           rust-cached
Version:        4.0.0
Release:        1%{?dist}
Summary:        Generic cache implementations and simplified function memoization
License:        MIT
URL:            https://crates.io/crates/cached
Source0:        https://static.crates.io/crates/cached/cached-%{version}.crate
Patch:          cached-fix-metadata.diff
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
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+async_tokio_rt_multi_thread-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+async_tokio_rt_multi_thread-devel

This package contains library source intended for building other packages which
use the "async_tokio_rt_multi_thread" feature of the "%{crate}" crate.

%package     -n %{name}+cached_proc_macro-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+cached_proc_macro-devel

This package contains library source intended for building other packages which
use the "cached_proc_macro" feature of the "%{crate}" crate.

%package     -n %{name}+cached_proc_macro_types-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+cached_proc_macro_types-devel

This package contains library source intended for building other packages which
use the "cached_proc_macro_types" feature of the "%{crate}" crate.

%package     -n %{name}+directories-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+directories-devel

This package contains library source intended for building other packages which
use the "directories" feature of the "%{crate}" crate.

%package     -n %{name}+disk_store-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+disk_store-devel

This package contains library source intended for building other packages which
use the "disk_store" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+proc_macro-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+proc_macro-devel

This package contains library source intended for building other packages which
use the "proc_macro" feature of the "%{crate}" crate.

%package     -n %{name}+r2d2-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+r2d2-devel

This package contains library source intended for building other packages which
use the "r2d2" feature of the "%{crate}" crate.

%package     -n %{name}+redis-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+redis-devel

This package contains library source intended for building other packages which
use the "redis" feature of the "%{crate}" crate.

%package     -n %{name}+redis_ahash-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+redis_ahash-devel

This package contains library source intended for building other packages which
use the "redis_ahash" feature of the "%{crate}" crate.

%package     -n %{name}+redis_async_std-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+redis_async_std-devel

This package contains library source intended for building other packages which
use the "redis_async_std" feature of the "%{crate}" crate.

%package     -n %{name}+redis_connection_manager-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+redis_connection_manager-devel

This package contains library source intended for building other packages which
use the "redis_connection_manager" feature of the "%{crate}" crate.

%package     -n %{name}+redis_store-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+redis_store-devel

This package contains library source intended for building other packages which
use the "redis_store" feature of the "%{crate}" crate.

%package     -n %{name}+redis_tokio-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+redis_tokio-devel

This package contains library source intended for building other packages which
use the "redis_tokio" feature of the "%{crate}" crate.

%package     -n %{name}+rmp-serde-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+rmp-serde-devel

This package contains library source intended for building other packages which
use the "rmp-serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sled-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+sled-devel

This package contains library source intended for building other packages which
use the "sled" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Generic cache implementations and simplified function memoization
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm examples/disk.rs
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
%files -n rust-cached-devel -f %{oreon_filedir}/rust-cached-devel.list

%changelog

%autochangelog
