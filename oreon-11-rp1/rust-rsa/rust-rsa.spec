%global source0_hash b8573f03f5883dcaebdfcf4725caa1ecb9c15b2ef50c43a07b816e06799bb12d
%bcond check 0
%global debug_package %{nil}
%global crate rsa
Name:           rust-rsa
Version:        0.9.10
Release:        1%{?dist}
Summary:        Pure Rust RSA implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rsa
Source0:        https://static.crates.io/crates/rsa/rsa-%{version}.crate
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
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+hazmat-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs5-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+pkcs5-devel

This package contains library source intended for building other packages which
use the "pkcs5" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+u64_digit-devel
Summary:        Pure Rust RSA implementation
BuildArch:      noarch
%description -n %{name}+u64_digit-devel

This package contains library source intended for building other packages which
use the "u64_digit" feature of the "%{crate}" crate.

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
%files -n rust-rsa-devel -f %{oreon_filedir}/rust-rsa-devel.list

%changelog

%autochangelog
