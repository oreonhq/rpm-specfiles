%global source1_hash 9a32b02e4c917b1ce6b5e79d8ea81e25cefd7f27d89c7235f2afb262c06cf32e
%global source0_hash 5cdb9adf0965fec58e7660cbb3a059dbb12ebeec9459e6dcbae3db004739641e
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-lua
Name:           rust-tree-sitter-lua
Version:        0.2.0
Release:        1%{?dist}
Summary:        Lua grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-lua
Source0:        https://static.crates.io/crates/tree-sitter-lua/tree-sitter-lua-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter-grammars/%{crate}/refs/tags/v%{version}/LICENSE.md
Patch:          tree-sitter-lua-fix-metadata.diff
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
Summary:        Lua grammar for tree-sitter
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
%files -n rust-tree-sitter-lua-devel -f %{oreon_filedir}/rust-tree-sitter-lua-devel.list

%changelog

%autochangelog
