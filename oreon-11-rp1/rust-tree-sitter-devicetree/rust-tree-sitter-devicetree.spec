%global source1_hash b539c1b4ccd868c8d4fc89651c8133a1678823f5057e2e1a81455a3df4f4c0b8
%global source0_hash b1e6874b59d8252cbaf9750f7152166e17ed162921a5f6d4e8bd2a2bc2aed46b
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-devicetree
Name:           rust-tree-sitter-devicetree
Version:        0.14.1
Release:        1%{?dist}
Summary:        Tree-sitter parser for Devicetree files with Zephyr extended syntax
License:        MIT
URL:            https://crates.io/crates/tree-sitter-devicetree
Source0:        https://static.crates.io/crates/tree-sitter-devicetree/tree-sitter-devicetree-%{version}.crate
Source1:        https://raw.githubusercontent.com/joelspadin/tree-sitter-devicetree/refs/tags/v%{version}/LICENSE
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
Summary:        Tree-sitter parser for Devicetree files with Zephyr extended syntax
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE1} .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
cp -p LICENSE %{buildroot}%{crate_instdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-devicetree-devel -f %{oreon_filedir}/rust-tree-sitter-devicetree-devel.list

%changelog

%autochangelog
