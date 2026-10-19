%global source10_hash e9306dd6396046f8e887952447e1a1276ba198d65351590d85d641a7181bdf48
%global source0_hash bea0f369eddde45219969406b7cc591b113c0373907c293f3e05f8a1d23d13c7
%bcond check 1
%global debug_package %{nil}
%global crate matrixcompare-mock
Name:           rust-matrixcompare-mock
Version:        0.1.0
Release:        1%{?dist}
Summary:        Internal mock data structures for testing of matrixcompare
License:        MIT
URL:            https://crates.io/crates/matrixcompare-mock
Source0:        https://static.crates.io/crates/matrixcompare-mock/matrixcompare-mock-%{version}.crate
Source10:       https://github.com/Andlon/matrixcompare/raw/57a66bd/LICENSE
Patch:          matrixcompare-mock-fix-metadata.diff
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
Summary:        Internal mock data structures for testing of matrixcompare
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE10} .
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
%files -n rust-matrixcompare-mock-devel -f %{oreon_filedir}/rust-matrixcompare-mock-devel.list

%changelog

%autochangelog
