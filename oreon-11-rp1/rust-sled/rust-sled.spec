%global source0_hash 7f96b4737c2ce5987354855aed3797279def4ebf734436c6aa4552cf8e169935
%bcond check 0
%global debug_package %{nil}
%global crate sled
Name:           rust-sled
Version:        0.34.7
Release:        1%{?dist}
Summary:        Lightweight high-performance pure-rust transactional embedded database
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sled
Source0:        https://static.crates.io/crates/sled/sled-%{version}.crate
Patch:          sled-fix-metadata.diff
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
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+event_log-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+event_log-devel

This package contains library source intended for building other packages which
use the "event_log" feature of the "%{crate}" crate.

%package     -n %{name}+failpoints-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+failpoints-devel

This package contains library source intended for building other packages which
use the "failpoints" feature of the "%{crate}" crate.

%package     -n %{name}+io_uring-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+io_uring-devel

This package contains library source intended for building other packages which
use the "io_uring" feature of the "%{crate}" crate.

%package     -n %{name}+lock_free_delays-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+lock_free_delays-devel

This package contains library source intended for building other packages which
use the "lock_free_delays" feature of the "%{crate}" crate.

%package     -n %{name}+measure_allocs-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+measure_allocs-devel

This package contains library source intended for building other packages which
use the "measure_allocs" feature of the "%{crate}" crate.

%package     -n %{name}+miri_optimizations-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+miri_optimizations-devel

This package contains library source intended for building other packages which
use the "miri_optimizations" feature of the "%{crate}" crate.

%package     -n %{name}+mutex-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+mutex-devel

This package contains library source intended for building other packages which
use the "mutex" feature of the "%{crate}" crate.

%package     -n %{name}+no_inline-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+no_inline-devel

This package contains library source intended for building other packages which
use the "no_inline" feature of the "%{crate}" crate.

%package     -n %{name}+no_logs-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+no_logs-devel

This package contains library source intended for building other packages which
use the "no_logs" feature of the "%{crate}" crate.

%package     -n %{name}+no_metrics-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+no_metrics-devel

This package contains library source intended for building other packages which
use the "no_metrics" feature of the "%{crate}" crate.

%package     -n %{name}+rio-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+rio-devel

This package contains library source intended for building other packages which
use the "rio" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Lightweight high-performance pure-rust transactional embedded database
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f testing
%install
%cargo_install -f testing
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

rm -r tests/{tree/,test_tree.rs}
%cargo_test -f testing
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sled-devel -f %{oreon_filedir}/rust-sled-devel.list

%changelog

%autochangelog
