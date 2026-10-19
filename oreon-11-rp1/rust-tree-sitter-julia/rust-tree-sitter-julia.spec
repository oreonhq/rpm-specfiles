%global source1_hash 74f800107f200f4e28da33e9c3f86230d37d8f4c0a4916f7111e800c395ee3a2
%global source0_hash 4144731a178812ee867619b1e98b3b91e54c1652304b26e5ebe3175b701de323
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-julia
Name:           rust-tree-sitter-julia
Version:        0.23.1
Release:        1%{?dist}
Summary:        Julia grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-julia
Source0:        https://static.crates.io/crates/tree-sitter-julia/tree-sitter-julia-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-julia-fix-metadata.diff
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
Summary:        Julia grammar for tree-sitter
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
%files -n rust-tree-sitter-julia-devel -f %{oreon_filedir}/rust-tree-sitter-julia-devel.list

%changelog

%autochangelog
