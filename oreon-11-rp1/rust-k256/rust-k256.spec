%global source0_hash 93f50113171a713f4a4231ef82eb26703607139b35dcb56241f0ceab2ae1f7d8
%bcond check 1
%global debug_package %{nil}
%global crate k256
Name:           rust-k256
Version:        0.14.0
Release:        1%{?dist}
Summary:        Secp256k1 elliptic curve library written in pure Rust
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/k256
Source0:        https://static.crates.io/crates/k256/k256-%{version}.crate
Patch:          k256-fix-metadata.diff
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
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arithmetic-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+arithmetic-devel

This package contains library source intended for building other packages which
use the "arithmetic" feature of the "%{crate}" crate.

%package     -n %{name}+bits-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+bits-devel

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

%package     -n %{name}+critical-section-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+critical-section-devel

This package contains library source intended for building other packages which
use the "critical-section" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+ecdh-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+ecdh-devel

This package contains library source intended for building other packages which
use the "ecdh" feature of the "%{crate}" crate.

%package     -n %{name}+ecdsa-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+ecdsa-devel

This package contains library source intended for building other packages which
use the "ecdsa" feature of the "%{crate}" crate.

%package     -n %{name}+ecdsa-core-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+ecdsa-core-devel

This package contains library source intended for building other packages which
use the "ecdsa-core" feature of the "%{crate}" crate.

%package     -n %{name}+expose-field-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+expose-field-devel

This package contains library source intended for building other packages which
use the "expose-field" feature of the "%{crate}" crate.

%package     -n %{name}+hash2curve-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+hash2curve-devel

This package contains library source intended for building other packages which
use the "hash2curve" feature of the "%{crate}" crate.

%package     -n %{name}+hex-literal-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+hex-literal-devel

This package contains library source intended for building other packages which
use the "hex-literal" feature of the "%{crate}" crate.

%package     -n %{name}+jwk-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+jwk-devel

This package contains library source intended for building other packages which
use the "jwk" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+precomputed-tables-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+precomputed-tables-devel

This package contains library source intended for building other packages which
use the "precomputed-tables" feature of the "%{crate}" crate.

%package     -n %{name}+schnorr-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+schnorr-devel

This package contains library source intended for building other packages which
use the "schnorr" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serdect-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+serdect-devel

This package contains library source intended for building other packages which
use the "serdect" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

%package     -n %{name}+signature-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+signature-devel

This package contains library source intended for building other packages which
use the "signature" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test-vectors-devel
Summary:        Secp256k1 elliptic curve library written in pure Rust
BuildArch:      noarch
%description -n %{name}+test-vectors-devel

This package contains library source intended for building other packages which
use the "test-vectors" feature of the "%{crate}" crate.

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
%files -n rust-k256-devel -f %{oreon_filedir}/rust-k256-devel.list

%changelog

%autochangelog
