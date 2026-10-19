%global source0_hash 9d65aa39b3a5c1c9c1b745c9a019234bb7a21b77abcb4f4d266d706e2d577d65
%bcond check 0
%global debug_package %{nil}
%global crate elliptic-curve
Name:           rust-elliptic-curve
Version:        0.14.1
Release:        1%{?dist}
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/elliptic-curve
Source0:        https://static.crates.io/crates/elliptic-curve/elliptic-curve-%{version}.crate
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
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arithmetic-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+arithmetic-devel

This package contains library source intended for building other packages which
use the "arithmetic" feature of the "%{crate}" crate.

%package     -n %{name}+dev-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+dev-devel

This package contains library source intended for building other packages which
use the "dev" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+ecdh-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+ecdh-devel

This package contains library source intended for building other packages which
use the "ecdh" feature of the "%{crate}" crate.

%package     -n %{name}+ff-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+ff-devel

This package contains library source intended for building other packages which
use the "ff" feature of the "%{crate}" crate.

%package     -n %{name}+group-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+group-devel

This package contains library source intended for building other packages which
use the "group" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+sec1-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+sec1-devel

This package contains library source intended for building other packages which
use the "sec1" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including...
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
%files -n rust-elliptic-curve-devel -f %{oreon_filedir}/rust-elliptic-curve-devel.list

%changelog

%autochangelog
