%global source0_hash b5e6043086bf7973472e0c7dff2142ea0b680d30e18d9cc40f267efbf222bd47
%bcond check 1
%global debug_package %{nil}
%global crate elliptic-curve
Name:           rust-elliptic-curve0.13
Version:        0.13.8
Release:        1%{?dist}
Summary:        General purpose Elliptic Curve Cryptography
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/elliptic-curve
Source0:        https://static.crates.io/crates/elliptic-curve/elliptic-curve-%{version}.crate
Patch:          elliptic-curve-fix-metadata.diff
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
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arithmetic-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+arithmetic-devel

This package contains library source intended for building other packages which
use the "arithmetic" feature of the "%{crate}" crate.

%package     -n %{name}+bits-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+bits-devel

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+ecdh-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+ecdh-devel

This package contains library source intended for building other packages which
use the "ecdh" feature of the "%{crate}" crate.

%package     -n %{name}+ff-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+ff-devel

This package contains library source intended for building other packages which
use the "ff" feature of the "%{crate}" crate.

%package     -n %{name}+group-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+group-devel

This package contains library source intended for building other packages which
use the "group" feature of the "%{crate}" crate.

%package     -n %{name}+hash2curve-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+hash2curve-devel

This package contains library source intended for building other packages which
use the "hash2curve" feature of the "%{crate}" crate.

%package     -n %{name}+hazmat-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+jwk-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+jwk-devel

This package contains library source intended for building other packages which
use the "jwk" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+sec1-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+sec1-devel

This package contains library source intended for building other packages which
use the "sec1" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        General purpose Elliptic Curve Cryptography
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+voprf-devel
Summary:        General purpose Elliptic Curve Cryptography
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
%files -n rust-elliptic-curve0.13-devel -f %{oreon_filedir}/rust-elliptic-curve0.13-devel.list

%changelog

%autochangelog
