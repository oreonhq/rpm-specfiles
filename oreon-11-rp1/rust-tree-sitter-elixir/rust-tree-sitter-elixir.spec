%global source1_hash a6cba85bc92e0cff7a450b1d873c0eaa2e9fc96bf472df0247a26bec77bf3ff9
%global source0_hash e45d444647b4fd53d8fd32474c1b8bedc1baa22669ce3a78d083e365fa9a2d3f
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-elixir
Name:           rust-tree-sitter-elixir
Version:        0.3.4
Release:        1%{?dist}
Summary:        Elixir grammar for the tree-sitter parsing library
License:        Apache-2.0
URL:            https://crates.io/crates/tree-sitter-elixir
Source0:        https://static.crates.io/crates/tree-sitter-elixir/tree-sitter-elixir-%{version}.crate
Source1:        https://raw.githubusercontent.com/elixir-lang/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-elixir-fix-metadata.diff
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
Summary:        Elixir grammar for the tree-sitter parsing library
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-elixir-devel -f %{oreon_filedir}/rust-tree-sitter-elixir-devel.list

%changelog

%autochangelog
