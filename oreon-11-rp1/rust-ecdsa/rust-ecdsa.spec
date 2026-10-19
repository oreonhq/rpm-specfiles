%global source0_hash c0681a4fc24c767085329728d8dfba959af91228aa4610cca4f8ce317ba46ae0
%bcond check 0
%global debug_package %{nil}
%global crate ecdsa
Name:           rust-ecdsa
Version:        0.17.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ecdsa
Source0:        https://static.crates.io/crates/ecdsa/ecdsa-%{version}.crate
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
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+der-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+der-devel

This package contains library source intended for building other packages which
use the "der" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+spki-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+spki-devel

This package contains library source intended for building other packages which
use the "spki" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algo...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ecdsa-devel -f %{oreon_filedir}/rust-ecdsa-devel.list

%changelog

%autochangelog
