%global source0_hash b281d307588d634de920874890732659e2e7672f72b5e10e81badc1a8a83621e
%bcond check 0
%global debug_package %{nil}
%global crate aws-lc-rs
Name:           rust-aws-lc-rs
Version:        1.18.1
Release:        1%{?dist}
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
License:        ISC AND (Apache-2.0 OR ISC)
URL:            https://crates.io/crates/aws-lc-rs
Source0:        https://static.crates.io/crates/aws-lc-rs/aws-lc-rs-%{version}.crate
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
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+asan-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+asan-devel

This package contains library source intended for building other packages which
use the "asan" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-sys-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+aws-lc-sys-devel

This package contains library source intended for building other packages which
use the "aws-lc-sys" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+dev-tests-only-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+dev-tests-only-devel

This package contains library source intended for building other packages which
use the "dev-tests-only" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-des-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+legacy-des-devel

This package contains library source intended for building other packages which
use the "legacy-des" feature of the "%{crate}" crate.

%package     -n %{name}+non-fips-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+non-fips-devel

This package contains library source intended for building other packages which
use the "non-fips" feature of the "%{crate}" crate.

%package     -n %{name}+prebuilt-nasm-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+prebuilt-nasm-devel

This package contains library source intended for building other packages which
use the "prebuilt-nasm" feature of the "%{crate}" crate.

%package     -n %{name}+ring-io-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+ring-io-devel

This package contains library source intended for building other packages which
use the "ring-io" feature of the "%{crate}" crate.

%package     -n %{name}+ring-sig-verify-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+ring-sig-verify-devel

This package contains library source intended for building other packages which
use the "ring-sig-verify" feature of the "%{crate}" crate.

%package     -n %{name}+test_logging-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
BuildArch:      noarch
%description -n %{name}+test_logging-devel

This package contains library source intended for building other packages which
use the "test_logging" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Aws-lc-rs is a cryptographic library using AWS-LC for its cryptographic operations
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
%files -n rust-aws-lc-rs-devel -f %{oreon_filedir}/rust-aws-lc-rs-devel.list

%changelog

%autochangelog
