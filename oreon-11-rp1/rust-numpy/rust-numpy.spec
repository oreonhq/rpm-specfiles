%global source0_hash 7aac2e6a6e4468ffa092ad43c39b81c79196c2bb773b8db4085f695efe3bba17
%bcond check 1
%global debug_package %{nil}
%global crate numpy
Name:           rust-numpy
Version:        0.27.1
Release:        1%{?dist}
Summary:        PyO3-based Rust bindings of the NumPy C-API
License:        BSD-2-Clause
URL:            https://crates.io/crates/numpy
Source0:        https://static.crates.io/crates/numpy/numpy-%{version}.crate
Patch2:         https://patch-diff.githubusercontent.com/raw/PyO3/rust-numpy/pull/524.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  python3dist(numpy)
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
Summary:        PyO3-based Rust bindings of the NumPy C-API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+half-devel
Summary:        PyO3-based Rust bindings of the NumPy C-API
BuildArch:      noarch
%description -n %{name}+half-devel

This package contains library source intended for building other packages which
use the "half" feature of the "%{crate}" crate.

%package     -n %{name}+nalgebra-devel
Summary:        PyO3-based Rust bindings of the NumPy C-API
BuildArch:      noarch
%description -n %{name}+nalgebra-devel

This package contains library source intended for building other packages which
use the "nalgebra" feature of the "%{crate}" crate.

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

%if 0%{?__isa_bits} == 32
%cargo_test -- -- --skip dtype::tests::test_dtype_methods_
%else
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-numpy-devel -f %{oreon_filedir}/rust-numpy-devel.list

%changelog

%autochangelog
