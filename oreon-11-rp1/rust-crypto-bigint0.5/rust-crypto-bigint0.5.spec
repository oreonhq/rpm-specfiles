%global source0_hash 0dc92fb57ca44df6db8059111ab3af99a63d5d0f8375d9972e319a379c6bab76
%bcond check 1
%global debug_package %{nil}
%global crate crypto-bigint
Name:           rust-crypto-bigint0.5
Version:        0.5.5
Release:        1%{?dist}
Summary:        Pure Rust bigint implementation for use in cryptographic applications
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/crypto-bigint
Source0:        https://static.crates.io/crates/crypto-bigint/crypto-bigint-%{version}.crate
Patch:          crypto-bigint-fix-metadata.diff
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
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+der-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+der-devel

This package contains library source intended for building other packages which
use the "der" feature of the "%{crate}" crate.

%package     -n %{name}+extra-sizes-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+extra-sizes-devel

This package contains library source intended for building other packages which
use the "extra-sizes" feature of the "%{crate}" crate.

%package     -n %{name}+generic-array-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+generic-array-devel

This package contains library source intended for building other packages which
use the "generic-array" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust bigint implementation for use in cryptographic applications
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-crypto-bigint0.5-devel -f %{oreon_filedir}/rust-crypto-bigint0.5-devel.list

%changelog

%autochangelog
