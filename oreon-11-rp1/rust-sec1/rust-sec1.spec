%global source0_hash d3e97a565f76233a6003f9f5c54be1d9c5bdfa3eccfb189469f11ec4901c47dc
%bcond check 0
%global debug_package %{nil}
%global crate sec1
Name:           rust-sec1
Version:        0.7.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sec1
Source0:        https://static.crates.io/crates/sec1/sec1-%{version}.crate
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
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+base16ct-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+base16ct-devel

This package contains library source intended for building other packages which
use the "base16ct" feature of the "%{crate}" crate.

%package     -n %{name}+der-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+der-devel

This package contains library source intended for building other packages which
use the "der" feature of the "%{crate}" crate.

%package     -n %{name}+generic-array-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+generic-array-devel

This package contains library source intended for building other packages which
use the "generic-array" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+point-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+point-devel

This package contains library source intended for building other packages which
use the "point" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serdect-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+serdect-devel

This package contains library source intended for building other packages which
use the "serdect" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+subtle-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
BuildArch:      noarch
%description -n %{name}+subtle-devel

This package contains library source intended for building other packages which
use the "subtle" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encodin...
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
%files -n rust-sec1-devel -f %{oreon_filedir}/rust-sec1-devel.list

%changelog

%autochangelog
