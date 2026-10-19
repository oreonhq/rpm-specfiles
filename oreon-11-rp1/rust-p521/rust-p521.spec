%global source0_hash 0fc9e2161f1f215afdfce23677034ae137bbd45016a880c2eb3ba8eb95f085b2
%bcond check 0
%global debug_package %{nil}
%global crate p521
Name:           rust-p521
Version:        0.13.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/p521
Source0:        https://static.crates.io/crates/p521/p521-%{version}.crate
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
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arithmetic-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+arithmetic-devel

This package contains library source intended for building other packages which
use the "arithmetic" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+ecdh-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+ecdh-devel

This package contains library source intended for building other packages which
use the "ecdh" feature of the "%{crate}" crate.

%package     -n %{name}+ecdsa-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+ecdsa-devel

This package contains library source intended for building other packages which
use the "ecdsa" feature of the "%{crate}" crate.

%package     -n %{name}+ecdsa-core-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+ecdsa-core-devel

This package contains library source intended for building other packages which
use the "ecdsa-core" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+hash2curve-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+hash2curve-devel

This package contains library source intended for building other packages which
use the "hash2curve" feature of the "%{crate}" crate.

%package     -n %{name}+hex-literal-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+hex-literal-devel

This package contains library source intended for building other packages which
use the "hex-literal" feature of the "%{crate}" crate.

%package     -n %{name}+jwk-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+jwk-devel

This package contains library source intended for building other packages which
use the "jwk" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+primeorder-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+primeorder-devel

This package contains library source intended for building other packages which
use the "primeorder" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serdect-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+serdect-devel

This package contains library source intended for building other packages which
use the "serdect" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+sha512-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+sha512-devel

This package contains library source intended for building other packages which
use the "sha512" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test-vectors-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+test-vectors-devel

This package contains library source intended for building other packages which
use the "test-vectors" feature of the "%{crate}" crate.

%package     -n %{name}+voprf-devel
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a. secp521r1) ellipti...
BuildArch:      noarch
%description -n %{name}+voprf-devel

This package contains library source intended for building other packages which
use the "voprf" feature of the "%{crate}" crate.

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
%files -n rust-p521-devel -f %{oreon_filedir}/rust-p521-devel.list

%changelog

%autochangelog
