%global source0_hash 670fdfda89751bc4a84ac13eaa63e205cf0fd22b4c9a5fbfa085b63c1f1d3a30
%bcond check 0
%global debug_package %{nil}
%global crate macro_rules_attribute-proc_macro
Name:           rust-macro_rules_attribute-proc_macro
Version:        0.2.2
Release:        1%{?dist}
Summary:        Use declarative macros as proc_macro attributes or derives
License:        Apache-2.0 OR MIT OR Zlib
URL:            https://crates.io/crates/macro_rules_attribute-proc_macro
Source0:        https://static.crates.io/crates/macro_rules_attribute-proc_macro/macro_rules_attribute-proc_macro-%{version}.crate
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

%package     -n %{name}+verbose-expansions-devel
Summary:        Use declarative macros as proc_macro attributes or derives
BuildArch:      noarch
%description -n %{name}+verbose-expansions-devel

This package contains library source intended for building other packages which
use the "verbose-expansions" feature of the "%{crate}" crate.

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
%files -n rust-macro_rules_attribute-proc_macro-devel -f %{oreon_filedir}/rust-macro_rules_attribute-proc_macro-devel.list

%changelog

%autochangelog
