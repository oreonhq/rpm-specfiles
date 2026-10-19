%global source0_hash 9c07347b7c0301b9adba4350bdcf09c039d0e7160922050db0439b3c6723c8ab
%bcond check 1
%global debug_package %{nil}
%global crate spin_sleep
Name:           rust-spin_sleep
Version:        1.3.3
Release:        1%{?dist}
Summary:        Accurate sleeping
License:        Apache-2.0
URL:            https://crates.io/crates/spin_sleep
Source0:        https://static.crates.io/crates/spin_sleep/spin_sleep-%{version}.crate
Patch:          spin_sleep-fix-metadata-auto.diff
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
Summary:        Accurate sleeping
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nondeterministic_tests-devel
Summary:        Accurate sleeping
BuildArch:      noarch
%description -n %{name}+nondeterministic_tests-devel

This package contains library source intended for building other packages which
use the "nondeterministic_tests" feature of the "%{crate}" crate.

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
%files -n rust-spin_sleep-devel -f %{oreon_filedir}/rust-spin_sleep-devel.list

%changelog

%autochangelog
