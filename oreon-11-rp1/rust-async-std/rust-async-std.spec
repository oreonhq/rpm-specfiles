%global source0_hash 2c8e079a4ab67ae52b7403632e4618815d6db36d2a010cfe41b02c1b1578f93b
%bcond check 0
%global debug_package %{nil}
%global crate async-std
Name:           rust-async-std
Version:        1.13.2
Release:        1%{?dist}
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-std
Source0:        https://static.crates.io/crates/async-std/async-std-%{version}.crate
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
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+async-attributes-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+async-attributes-devel

This package contains library source intended for building other packages which
use the "async-attributes" feature of the "%{crate}" crate.

%package     -n %{name}+async-channel-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+async-channel-devel

This package contains library source intended for building other packages which
use the "async-channel" feature of the "%{crate}" crate.

%package     -n %{name}+async-lock-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+async-lock-devel

This package contains library source intended for building other packages which
use the "async-lock" feature of the "%{crate}" crate.

%package     -n %{name}+attributes-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+attributes-devel

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-utils-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+crossbeam-utils-devel

This package contains library source intended for building other packages which
use the "crossbeam-utils" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+io_safety-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+io_safety-devel

This package contains library source intended for building other packages which
use the "io_safety" feature of the "%{crate}" crate.

%package     -n %{name}+kv-log-macro-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+kv-log-macro-devel

This package contains library source intended for building other packages which
use the "kv-log-macro" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+pin-utils-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+pin-utils-devel

This package contains library source intended for building other packages which
use the "pin-utils" feature of the "%{crate}" crate.

%package     -n %{name}+slab-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+slab-devel

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+surf-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+surf-devel

This package contains library source intended for building other packages which
use the "surf" feature of the "%{crate}" crate.

%package     -n %{name}+tokio02-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+tokio02-devel

This package contains library source intended for building other packages which
use the "tokio02" feature of the "%{crate}" crate.

%package     -n %{name}+tokio03-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+tokio03-devel

This package contains library source intended for building other packages which
use the "tokio03" feature of the "%{crate}" crate.

%package     -n %{name}+tokio1-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+tokio1-devel

This package contains library source intended for building other packages which
use the "tokio1" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Deprecated in favor of `smol` - Async version of the Rust standard li...
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-async-std-devel -f %{oreon_filedir}/rust-async-std-devel.list

%changelog

%autochangelog
