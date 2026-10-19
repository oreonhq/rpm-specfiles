%global source1_hash 8d2ff8d1e308828099436c43dc8bfbb8b6f368ad2a012ab9802a80ca22b03b53
%global source0_hash d4e7e0360395852f1f6ff5b7b82c72dc6557d181073188df1d60ec469ea69c66
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-verilog
Name:           rust-tree-sitter-verilog
Version:        1.0.3
Release:        1%{?dist}
Summary:        Verilog grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-verilog
Source0:        https://static.crates.io/crates/tree-sitter-verilog/tree-sitter-verilog-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/tree-sitter-verilog/refs/tags/v%{version}/LICENSE
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
Summary:        Verilog grammar for tree-sitter
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
%files -n rust-tree-sitter-verilog-devel -f %{oreon_filedir}/rust-tree-sitter-verilog-devel.list

%changelog

%autochangelog
