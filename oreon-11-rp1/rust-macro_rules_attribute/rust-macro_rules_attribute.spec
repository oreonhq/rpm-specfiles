%global source0_hash 65049d7923698040cd0b1ddcced9b0eb14dd22c5f86ae59c3740eab64a676520
%bcond check 0
%global debug_package %{nil}
%global crate macro_rules_attribute
Name:           rust-macro_rules_attribute
Version:        0.2.2
Release:        1%{?dist}
Summary:        Use declarative macros in attribute or derive position
License:        Apache-2.0 OR MIT OR Zlib
URL:            https://crates.io/crates/macro_rules_attribute
Source0:        https://static.crates.io/crates/macro_rules_attribute/macro_rules_attribute-%{version}.crate
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
Summary:        Use declarative macros in attribute or derive position
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+better-docs-devel
Summary:        Use declarative macros in attribute or derive position
BuildArch:      noarch
%description -n %{name}+better-docs-devel

This package contains library source intended for building other packages which
use the "better-docs" feature of the "%{crate}" crate.

%package     -n %{name}+verbose-expansions-devel
Summary:        Use declarative macros in attribute or derive position
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
%files -n rust-macro_rules_attribute-devel -f %{oreon_filedir}/rust-macro_rules_attribute-devel.list

%changelog

%autochangelog
