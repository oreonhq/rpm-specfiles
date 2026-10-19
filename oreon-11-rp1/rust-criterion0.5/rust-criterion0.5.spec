%global source0_hash f2b12d017a929603d80db1831cd3a24082f8137ce19c69e6447f54f5fc8d692f
%bcond check 0
%global debug_package %{nil}
%global crate criterion
Name:           rust-criterion0.5
Version:        0.5.1
Release:        1%{?dist}
Summary:        Statistics-driven micro-benchmarking library
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/criterion
Source0:        https://static.crates.io/crates/criterion/criterion-%{version}.crate
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
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async_futures-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+async_futures-devel

This package contains library source intended for building other packages which
use the "async_futures" feature of the "%{crate}" crate.

%package     -n %{name}+async_smol-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+async_smol-devel

This package contains library source intended for building other packages which
use the "async_smol" feature of the "%{crate}" crate.

%package     -n %{name}+async_std-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+async_std-devel

This package contains library source intended for building other packages which
use the "async_std" feature of the "%{crate}" crate.

%package     -n %{name}+async_tokio-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+async_tokio-devel

This package contains library source intended for building other packages which
use the "async_tokio" feature of the "%{crate}" crate.

%package     -n %{name}+cargo_bench_support-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+cargo_bench_support-devel

This package contains library source intended for building other packages which
use the "cargo_bench_support" feature of the "%{crate}" crate.

%package     -n %{name}+csv-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+csv-devel

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%package     -n %{name}+csv_output-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+csv_output-devel

This package contains library source intended for building other packages which
use the "csv_output" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+html_reports-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+html_reports-devel

This package contains library source intended for building other packages which
use the "html_reports" feature of the "%{crate}" crate.

%package     -n %{name}+plotters-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+plotters-devel

This package contains library source intended for building other packages which
use the "plotters" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+real_blackbox-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+real_blackbox-devel

This package contains library source intended for building other packages which
use the "real_blackbox" feature of the "%{crate}" crate.

%package     -n %{name}+smol-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+smol-devel

This package contains library source intended for building other packages which
use the "smol" feature of the "%{crate}" crate.

%package     -n %{name}+stable-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+stable-devel

This package contains library source intended for building other packages which
use the "stable" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-criterion0.5-devel -f %{oreon_filedir}/rust-criterion0.5-devel.list

%changelog

%autochangelog
