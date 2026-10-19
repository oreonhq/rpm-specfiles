%global source0_hash ebe5ef63511595f1344e2d5cfa636d973292adc0eec1f0ad45fae9f0851ab1d4
%bcond check 0
%global debug_package %{nil}
%global crate tower
Name:           rust-tower
Version:        0.5.3
Release:        1%{?dist}
Summary:        Tower is a library of modular and reusable components for building ro...
License:        MIT
URL:            https://crates.io/crates/tower
Source0:        https://static.crates.io/crates/tower/tower-%{version}.crate
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

%package     -n %{name}+balance-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+balance-devel

This package contains library source intended for building other packages which
use the "balance" feature of the "%{crate}" crate.

%package     -n %{name}+buffer-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+buffer-devel

This package contains library source intended for building other packages which
use the "buffer" feature of the "%{crate}" crate.

%package     -n %{name}+discover-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+discover-devel

This package contains library source intended for building other packages which
use the "discover" feature of the "%{crate}" crate.

%package     -n %{name}+filter-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+filter-devel

This package contains library source intended for building other packages which
use the "filter" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+hdrhistogram-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+hdrhistogram-devel

This package contains library source intended for building other packages which
use the "hdrhistogram" feature of the "%{crate}" crate.

%package     -n %{name}+hedge-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+hedge-devel

This package contains library source intended for building other packages which
use the "hedge" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+limit-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+limit-devel

This package contains library source intended for building other packages which
use the "limit" feature of the "%{crate}" crate.

%package     -n %{name}+load-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+load-devel

This package contains library source intended for building other packages which
use the "load" feature of the "%{crate}" crate.

%package     -n %{name}+load-shed-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+load-shed-devel

This package contains library source intended for building other packages which
use the "load-shed" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+make-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+make-devel

This package contains library source intended for building other packages which
use the "make" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+ready-cache-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+ready-cache-devel

This package contains library source intended for building other packages which
use the "ready-cache" feature of the "%{crate}" crate.

%package     -n %{name}+reconnect-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+reconnect-devel

This package contains library source intended for building other packages which
use the "reconnect" feature of the "%{crate}" crate.

%package     -n %{name}+retry-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+retry-devel

This package contains library source intended for building other packages which
use the "retry" feature of the "%{crate}" crate.

%package     -n %{name}+slab-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+slab-devel

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

%package     -n %{name}+spawn-ready-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+spawn-ready-devel

This package contains library source intended for building other packages which
use the "spawn-ready" feature of the "%{crate}" crate.

%package     -n %{name}+steer-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+steer-devel

This package contains library source intended for building other packages which
use the "steer" feature of the "%{crate}" crate.

%package     -n %{name}+sync_wrapper-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+sync_wrapper-devel

This package contains library source intended for building other packages which
use the "sync_wrapper" feature of the "%{crate}" crate.

%package     -n %{name}+timeout-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+timeout-devel

This package contains library source intended for building other packages which
use the "timeout" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-stream-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+tokio-stream-devel

This package contains library source intended for building other packages which
use the "tokio-stream" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+tokio-util-devel

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+util-devel
Summary:        Tower is a library of modular and reusable components for building ro...
BuildArch:      noarch
%description -n %{name}+util-devel

This package contains library source intended for building other packages which
use the "util" feature of the "%{crate}" crate.

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
%files -n rust-tower-devel -f %{oreon_filedir}/rust-tower-devel.list

%changelog

%autochangelog
