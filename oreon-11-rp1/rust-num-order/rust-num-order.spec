%global source0_hash 537b596b97c40fcf8056d153049eb22f481c17ebce72a513ec9286e4986d1bb6
%bcond check 1
%global debug_package %{nil}
%global crate num-order
Name:           rust-num-order
Version:        1.2.0
Release:        1%{?dist}
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
License:        Apache-2.0
URL:            https://crates.io/crates/num-order
Source0:        https://static.crates.io/crates/num-order/num-order-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+num-complex-devel
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
BuildArch:      noarch
%description -n %{name}+num-complex-devel

This package contains library source intended for building other packages which
use the "num-complex" feature of the "%{crate}" crate.

%package     -n %{name}+num-rational-devel
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
BuildArch:      noarch
%description -n %{name}+num-rational-devel

This package contains library source intended for building other packages which
use the "num-rational" feature of the "%{crate}" crate.

%package     -n %{name}+num-traits-devel
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
BuildArch:      noarch
%description -n %{name}+num-traits-devel

This package contains library source intended for building other packages which
use the "num-traits" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Numerically consistent Eq, Ord and Hash implementations for various num types
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -exec dos2unix --keepdate '{}' +
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
%files -n rust-num-order-devel -f %{oreon_filedir}/rust-num-order-devel.list

%changelog

%autochangelog
