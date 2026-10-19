%global source0_hash bd8e500409e6cd603b03e477c26a6caecdc27ac58979a53e881c75eafc079f44
%bcond check 1
%global debug_package %{nil}
%global crate num-modular
Name:           rust-num-modular
Version:        0.6.5
Release:        1%{?dist}
Summary:        A generic implementation of integer division and modular arithmetics
License:        Apache-2.0
URL:            https://crates.io/crates/num-modular
Source0:        https://static.crates.io/crates/num-modular/num-modular-%{version}.crate
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
Summary:        A generic implementation of integer division and modular arithmetics
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        A generic implementation of integer division and modular arithmetics
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+num-traits-devel
Summary:        A generic implementation of integer division and modular arithmetics
BuildArch:      noarch
%description -n %{name}+num-traits-devel

This package contains library source intended for building other packages which
use the "num-traits" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A generic implementation of integer division and modular arithmetics
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

%cargo_test -- -- --exact --skip reduced::tests::test_against_prim stdout
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-num-modular-devel -f %{oreon_filedir}/rust-num-modular-devel.list

%changelog

%autochangelog
