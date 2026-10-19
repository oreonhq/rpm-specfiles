%global source0_hash b8a94047bd9c3717c6ca3a145504c0e26b64a5e2d9eb9559b187748433fbc382
%bcond check 0
%global debug_package %{nil}
%global crate aws-nitro-enclaves-cose
Name:           rust-aws-nitro-enclaves-cose
Version:        0.5.2
Release:        1%{?dist}
Summary:        Safe Rust implementation of COSE, with COSE Sign1 currently implemented
License:        Apache-2.0
URL:            https://crates.io/crates/aws-nitro-enclaves-cose
Source0:        https://static.crates.io/crates/aws-nitro-enclaves-cose/aws-nitro-enclaves-cose-%{version}.crate
Patch:          aws-nitro-enclaves-cose-fix-metadata.diff
Patch:          aws-nitro-enclaves-cose-fix-errors.diff
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
Summary:        Safe Rust implementation of COSE, with COSE Sign1 currently implemented
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+key_openssl_pkey-devel
Summary:        Safe Rust implementation of COSE, with COSE Sign1 currently implemented
BuildArch:      noarch
%description -n %{name}+key_openssl_pkey-devel

This package contains library source intended for building other packages which
use the "key_openssl_pkey" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Safe Rust implementation of COSE, with COSE Sign1 currently implemented
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

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
%files -n rust-aws-nitro-enclaves-cose-devel -f %{oreon_filedir}/rust-aws-nitro-enclaves-cose-devel.list

%changelog

%autochangelog
