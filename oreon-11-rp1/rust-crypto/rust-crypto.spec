%global source0_hash bf1e6e5492f8f0830c37f301f6349e0dac8b2466e4fe89eef90e9eef906cd046
%bcond check 1
%global debug_package %{nil}
%global crate crypto
Name:           rust-crypto
Version:        0.5.1
Release:        1%{?dist}
Summary:        Facade crate for all of the RustCrypto traits
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/crypto
Source0:        https://static.crates.io/crates/crypto/crypto-%{version}.crate
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
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aead-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+aead-devel

This package contains library source intended for building other packages which
use the "aead" feature of the "%{crate}" crate.

%package     -n %{name}+cipher-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+cipher-devel

This package contains library source intended for building other packages which
use the "cipher" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+elliptic-curve-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+elliptic-curve-devel

This package contains library source intended for building other packages which
use the "elliptic-curve" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+password-hash-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+password-hash-devel

This package contains library source intended for building other packages which
use the "password-hash" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+signature-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+signature-devel

This package contains library source intended for building other packages which
use the "signature" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+universal-hash-devel
Summary:        Facade crate for all of the RustCrypto traits
BuildArch:      noarch
%description -n %{name}+universal-hash-devel

This package contains library source intended for building other packages which
use the "universal-hash" feature of the "%{crate}" crate.

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
%files -n rust-crypto-devel -f %{oreon_filedir}/rust-crypto-devel.list

%changelog

%autochangelog
