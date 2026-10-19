%global source0_hash a0228a564470f81724e30996bbc2b171713b37b15254a6440c7e2d5449b95691
%bcond check 0
%global debug_package %{nil}
%global crate simd-json
Name:           rust-simd-json
Version:        0.13.11
Release:        1%{?dist}
Summary:        High performance JSON parser based on a port of simdjson
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/simd-json
Source0:        https://static.crates.io/crates/simd-json/simd-json-%{version}.crate
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
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+128bit-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+128bit-devel

This package contains library source intended for building other packages which
use the "128bit" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+alloc_counter-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+alloc_counter-devel

This package contains library source intended for building other packages which
use the "alloc_counter" feature of the "%{crate}" crate.

%package     -n %{name}+approx-number-parsing-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+approx-number-parsing-devel

This package contains library source intended for building other packages which
use the "approx-number-parsing" feature of the "%{crate}" crate.

%package     -n %{name}+arraybackend-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+arraybackend-devel

This package contains library source intended for building other packages which
use the "arraybackend" feature of the "%{crate}" crate.

%package     -n %{name}+beef-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+beef-devel

This package contains library source intended for building other packages which
use the "beef" feature of the "%{crate}" crate.

%package     -n %{name}+bench-all-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-all-devel

This package contains library source intended for building other packages which
use the "bench-all" feature of the "%{crate}" crate.

%package     -n %{name}+bench-apache_builds-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-apache_builds-devel

This package contains library source intended for building other packages which
use the "bench-apache_builds" feature of the "%{crate}" crate.

%package     -n %{name}+bench-canada-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-canada-devel

This package contains library source intended for building other packages which
use the "bench-canada" feature of the "%{crate}" crate.

%package     -n %{name}+bench-citm_catalog-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-citm_catalog-devel

This package contains library source intended for building other packages which
use the "bench-citm_catalog" feature of the "%{crate}" crate.

%package     -n %{name}+bench-event_stacktrace_10kb-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-event_stacktrace_10kb-devel

This package contains library source intended for building other packages which
use the "bench-event_stacktrace_10kb" feature of the "%{crate}" crate.

%package     -n %{name}+bench-github_events-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-github_events-devel

This package contains library source intended for building other packages which
use the "bench-github_events" feature of the "%{crate}" crate.

%package     -n %{name}+bench-log-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-log-devel

This package contains library source intended for building other packages which
use the "bench-log" feature of the "%{crate}" crate.

%package     -n %{name}+bench-serde-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-serde-devel

This package contains library source intended for building other packages which
use the "bench-serde" feature of the "%{crate}" crate.

%package     -n %{name}+bench-twitter-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+bench-twitter-devel

This package contains library source intended for building other packages which
use the "bench-twitter" feature of the "%{crate}" crate.

%package     -n %{name}+big-int-as-float-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+big-int-as-float-devel

This package contains library source intended for building other packages which
use the "big-int-as-float" feature of the "%{crate}" crate.

%package     -n %{name}+colored-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+colored-devel

This package contains library source intended for building other packages which
use the "colored" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+getopts-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+getopts-devel

This package contains library source intended for building other packages which
use the "getopts" feature of the "%{crate}" crate.

%package     -n %{name}+hints-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+hints-devel

This package contains library source intended for building other packages which
use the "hints" feature of the "%{crate}" crate.

%package     -n %{name}+jemallocator-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+jemallocator-devel

This package contains library source intended for building other packages which
use the "jemallocator" feature of the "%{crate}" crate.

%package     -n %{name}+known-key-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+known-key-devel

This package contains library source intended for building other packages which
use the "known-key" feature of the "%{crate}" crate.

%package     -n %{name}+no-inline-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+no-inline-devel

This package contains library source intended for building other packages which
use the "no-inline" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+perf-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+perf-devel

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%package     -n %{name}+perfcnt-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+perfcnt-devel

This package contains library source intended for building other packages which
use the "perfcnt" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-detection-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+runtime-detection-devel

This package contains library source intended for building other packages which
use the "runtime-detection" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_impl-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+serde_impl-devel

This package contains library source intended for building other packages which
use the "serde_impl" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+swar-number-parsing-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+swar-number-parsing-devel

This package contains library source intended for building other packages which
use the "swar-number-parsing" feature of the "%{crate}" crate.

%package     -n %{name}+value-no-dup-keys-devel
Summary:        High performance JSON parser based on a port of simdjson
BuildArch:      noarch
%description -n %{name}+value-no-dup-keys-devel

This package contains library source intended for building other packages which
use the "value-no-dup-keys" feature of the "%{crate}" crate.

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
%files -n rust-simd-json-devel -f %{oreon_filedir}/rust-simd-json-devel.list

%changelog

%autochangelog
