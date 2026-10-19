%global source0_hash 37195f01a7464b2bc99ba33c5b2b61929bb294632bce96987f88e2ade8e29a07
%bcond check 0
%global debug_package %{nil}
%global crate effective-limits
Name:           rust-effective-limits
Version:        0.5.5
Release:        1%{?dist}
Summary:        Estimate effective resource limits for a process
License:        Apache-2.0
URL:            https://crates.io/crates/effective-limits
Source0:        https://static.crates.io/crates/effective-limits/effective-limits-%{version}.crate
Patch:          effective-limits-fix-metadata-auto.diff
Patch:          effective-limits-fix-metadata.diff
Patch:          0001-fix-compilation-of-tests-on-32-bit-architectures.patch
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
Summary:        Estimate effective resource limits for a process
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip tests::test_no_ulimit --skip tests::test_ulimit
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-effective-limits-devel -f %{oreon_filedir}/rust-effective-limits-devel.list

%changelog

%autochangelog
