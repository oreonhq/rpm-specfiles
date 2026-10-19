%global source0_hash c9df48d132e0790b6c6fa20ad94df61ab9621bb1e63db91d9075e6dbcfedf10a
%bcond check 0
%global debug_package %{nil}
%global crate primal-slowsieve
Name:           rust-primal-slowsieve
Version:        0.3.2
Release:        1%{?dist}
Summary:        Simple sieve of Eratosthenes designed for testing faster sieves
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/primal-slowsieve
Source0:        https://static.crates.io/crates/primal-slowsieve/primal-slowsieve-%{version}.crate
Patch:          primal-slowsieve-fix-metadata.diff
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
Summary:        Simple sieve of Eratosthenes designed for testing faster sieves
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+slow_tests-devel
Summary:        Simple sieve of Eratosthenes designed for testing faster sieves
BuildArch:      noarch
%description -n %{name}+slow_tests-devel

This package contains library source intended for building other packages which
use the "slow_tests" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Simple sieve of Eratosthenes designed for testing faster sieves
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-primal-slowsieve-devel -f %{oreon_filedir}/rust-primal-slowsieve-devel.list

%changelog

%autochangelog
