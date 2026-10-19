%global source0_hash 3b86f5297f0f04d08cabaa0f6bff7cb6aec4d9c3b49d87990d63da9d9156a8c3
%bcond check 1
%global debug_package %{nil}
%global crate ssh-key
Name:           rust-ssh-key
Version:        0.6.7
Release:        1%{?dist}
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ssh-key
Source0:        https://static.crates.io/crates/ssh-key/ssh-key-%{version}.crate
Patch:          ssh-key-fix-metadata.diff
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
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+crypto-devel

This package contains library source intended for building other packages which
use the "crypto" feature of the "%{crate}" crate.

%package     -n %{name}+dsa-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+dsa-devel

This package contains library source intended for building other packages which
use the "dsa" feature of the "%{crate}" crate.

%package     -n %{name}+ecdsa-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+ecdsa-devel

This package contains library source intended for building other packages which
use the "ecdsa" feature of the "%{crate}" crate.

%package     -n %{name}+ed25519-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+ed25519-devel

This package contains library source intended for building other packages which
use the "ed25519" feature of the "%{crate}" crate.

%package     -n %{name}+encryption-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+encryption-devel

This package contains library source intended for building other packages which
use the "encryption" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+p256-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+p256-devel

This package contains library source intended for building other packages which
use the "p256" feature of the "%{crate}" crate.

%package     -n %{name}+p384-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+p384-devel

This package contains library source intended for building other packages which
use the "p384" feature of the "%{crate}" crate.

%package     -n %{name}+p521-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+p521-devel

This package contains library source intended for building other packages which
use the "p521" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+rsa-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+rsa-devel

This package contains library source intended for building other packages which
use the "rsa" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tdes-devel
Summary:        Pure Rust implementation of SSH key file format decoders/encoders
BuildArch:      noarch
%description -n %{name}+tdes-devel

This package contains library source intended for building other packages which
use the "tdes" feature of the "%{crate}" crate.

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
%files -n rust-ssh-key-devel -f %{oreon_filedir}/rust-ssh-key-devel.list

%changelog

%autochangelog
