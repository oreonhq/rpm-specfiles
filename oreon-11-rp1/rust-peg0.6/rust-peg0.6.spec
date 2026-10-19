%global source0_hash 9f76678828272f177ac33b7e2ac2e3e73cc6c1cd1e3e387928aa69562fa51367
%bcond check 0
%global debug_package %{nil}
%global crate peg
Name:           rust-peg0.6
Version:        0.6.3
Release:        1%{?dist}
Summary:        Simple Parsing Expression Grammar (PEG) parser generator
License:        MIT
URL:            https://crates.io/crates/peg
Source0:        https://static.crates.io/crates/peg/peg-%{version}.crate
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
Summary:        Simple Parsing Expression Grammar (PEG) parser generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        Simple Parsing Expression Grammar (PEG) parser generator
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/compile-fail/rust_action_type_error.{rs,stderr}
rm tests/compile-fail/rule_args_errors.{rs,stderr}
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
%files -n rust-peg0.6-devel -f %{oreon_filedir}/rust-peg0.6-devel.list

%changelog

%autochangelog
