%global source0_hash b4c0cf476284b03eb6c10e78787b21c7abb7d7d43cb2f02532ba6b831ed892fa
%bcond check 0
%global debug_package %{nil}
%global crate cx448
Name:           rust-cx448
Version:        0.1.1
Release:        1%{?dist}
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
License:        BSD-3-Clause
URL:            https://crates.io/crates/cx448
Source0:        https://static.crates.io/crates/cx448/cx448-%{version}.crate
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
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+crypto_signature-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+crypto_signature-devel

This package contains library source intended for building other packages which
use the "crypto_signature" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serdect-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+serdect-devel

This package contains library source intended for building other packages which
use the "serdect" feature of the "%{crate}" crate.

%package     -n %{name}+signing-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+signing-devel

This package contains library source intended for building other packages which
use the "signing" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        A pure-Rust implementation of Ed448 and Curve448 and Decaf.
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
%files -n rust-cx448-devel -f %{oreon_filedir}/rust-cx448-devel.list

%changelog

%autochangelog
