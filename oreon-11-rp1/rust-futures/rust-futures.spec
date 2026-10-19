%global source0_hash 9a31d2a3fbaaeb2af2368bbdd904aa8e812d3c04a1ee10d3171f52d556e5d0a3
%bcond check 1
%global debug_package %{nil}
%global crate futures
Name:           rust-futures
Version:        0.3.34
Release:        1%{?dist}
Summary:        Implementation of futures and streams
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures
Source0:        https://static.crates.io/crates/futures/futures-%{version}.crate
Patch:          futures-fix-metadata.diff
Patch10:        0001-Fix-compiling-tests-with-compat-and-io-compat-featur.patch
%if %{with check}
%endif
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
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+async-await-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+async-await-devel

This package contains library source intended for building other packages which
use the "async-await" feature of the "%{crate}" crate.

%package     -n %{name}+bilock-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+bilock-devel

This package contains library source intended for building other packages which
use the "bilock" feature of the "%{crate}" crate.

%package     -n %{name}+cfg-target-has-atomic-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+cfg-target-has-atomic-devel

This package contains library source intended for building other packages which
use the "cfg-target-has-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+executor-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+executor-devel

This package contains library source intended for building other packages which
use the "executor" feature of the "%{crate}" crate.

%package     -n %{name}+futures-executor-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+futures-executor-devel

This package contains library source intended for building other packages which
use the "futures-executor" feature of the "%{crate}" crate.

%package     -n %{name}+spin-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+spin-devel

This package contains library source intended for building other packages which
use the "spin" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thread-pool-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+thread-pool-devel

This package contains library source intended for building other packages which
use the "thread-pool" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+write-all-vectored-devel
Summary:        Implementation of futures and streams
BuildArch:      noarch
%description -n %{name}+write-all-vectored-devel

This package contains library source intended for building other packages which
use the "write-all-vectored" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/compat.rs
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -f default,thread-pool -- -- %{shrink:
    --skip stream_select
    --skip many_threads
    --skip join_size
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-futures-devel -f %{oreon_filedir}/rust-futures-devel.list

%changelog

%autochangelog
