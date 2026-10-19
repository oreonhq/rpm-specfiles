%global source0_hash 0c13d25dfb29edf328c7eb4ebb24838ade355272d685ba0402b8751567c3dde2
%bcond check 1
%global debug_package %{nil}
%global crate domain
%global forgeurl0 https://github.com/NLnetLabs/domain
Name:           rust-domain
Version:        0.12.2
Release:        1%{?dist}
Summary:        DNS library for Rust
License:        BSD-3-Clause
URL:            https://crates.io/crates/domain
VCS:            git:%{forgeurl0}
Source0:        https://static.crates.io/crates/domain/domain-%{version}.crate
Patch:          domain-fix-metadata.diff
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
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-swap-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+arc-swap-devel

This package contains library source intended for building other packages which
use the "arc-swap" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-util-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+futures-util-devel

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+moka-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+moka-devel

This package contains library source intended for building other packages which
use the "moka" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro2-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+proc-macro2-devel

This package contains library source intended for building other packages which
use the "proc-macro2" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+resolv-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+resolv-devel

This package contains library source intended for building other packages which
use the "resolv" feature of the "%{crate}" crate.

%package     -n %{name}+resolv-sync-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+resolv-sync-devel

This package contains library source intended for building other packages which
use the "resolv-sync" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sign-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+sign-devel

This package contains library source intended for building other packages which
use the "sign" feature of the "%{crate}" crate.

%package     -n %{name}+siphasher-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+siphasher-devel

This package contains library source intended for building other packages which
use the "siphasher" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-subscriber-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+tracing-subscriber-devel

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

%package     -n %{name}+tsig-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+tsig-devel

This package contains library source intended for building other packages which
use the "tsig" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-client-transport-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+unstable-client-transport-devel

This package contains library source intended for building other packages which
use the "unstable-client-transport" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-server-transport-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+unstable-server-transport-devel

This package contains library source intended for building other packages which
use the "unstable-server-transport" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-stelline-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+unstable-stelline-devel

This package contains library source intended for building other packages which
use the "unstable-stelline" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-zonetree-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+unstable-zonetree-devel

This package contains library source intended for building other packages which
use the "unstable-zonetree" feature of the "%{crate}" crate.

%package     -n %{name}+validate-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+validate-devel

This package contains library source intended for building other packages which
use the "validate" feature of the "%{crate}" crate.

%package     -n %{name}+zonefile-devel
Summary:        DNS library for Rust
BuildArch:      noarch
%description -n %{name}+zonefile-devel

This package contains library source intended for building other packages which
use the "zonefile" feature of the "%{crate}" crate.

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
%files -n rust-domain-devel -f %{oreon_filedir}/rust-domain-devel.list

%changelog

%autochangelog
