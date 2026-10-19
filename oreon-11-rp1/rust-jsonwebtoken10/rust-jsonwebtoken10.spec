%global source0_hash eba32bfb4ffdeaca3e34431072faf01745c9b26d25504aa7a6cf5684334fc4fc
%bcond check 0
%global debug_package %{nil}
%global crate jsonwebtoken
Name:           rust-jsonwebtoken10
Version:        10.4.0
Release:        1%{?dist}
Summary:        Create and decode JWTs in a strongly typed way
License:        MIT
URL:            https://crates.io/crates/jsonwebtoken
Source0:        https://static.crates.io/crates/jsonwebtoken/jsonwebtoken-%{version}.crate
Patch:          jsonwebtoken-fix-metadata-auto.diff
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
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+aws_lc_rs-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+aws_lc_rs-devel

This package contains library source intended for building other packages which
use the "aws_lc_rs" feature of the "%{crate}" crate.

%package     -n %{name}+ed25519-dalek-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+ed25519-dalek-devel

This package contains library source intended for building other packages which
use the "ed25519-dalek" feature of the "%{crate}" crate.

%package     -n %{name}+hmac-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+hmac-devel

This package contains library source intended for building other packages which
use the "hmac" feature of the "%{crate}" crate.

%package     -n %{name}+p256-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+p256-devel

This package contains library source intended for building other packages which
use the "p256" feature of the "%{crate}" crate.

%package     -n %{name}+p384-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+p384-devel

This package contains library source intended for building other packages which
use the "p384" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rsa-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+rsa-devel

This package contains library source intended for building other packages which
use the "rsa" feature of the "%{crate}" crate.

%package     -n %{name}+rust_crypto-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+rust_crypto-devel

This package contains library source intended for building other packages which
use the "rust_crypto" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+simple_asn1-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+simple_asn1-devel

This package contains library source intended for building other packages which
use the "simple_asn1" feature of the "%{crate}" crate.

%package     -n %{name}+use_pem-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+use_pem-devel

This package contains library source intended for building other packages which
use the "use_pem" feature of the "%{crate}" crate.

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
%files -n rust-jsonwebtoken10-devel -f %{oreon_filedir}/rust-jsonwebtoken10-devel.list

%changelog

%autochangelog
