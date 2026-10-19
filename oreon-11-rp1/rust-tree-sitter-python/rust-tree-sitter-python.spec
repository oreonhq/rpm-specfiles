%global source1_hash d724405ce238a22c0d35769c5a36b386ad5958192efe8bbb304fb2896254575f
%global source0_hash 3d065aaa27f3aaceaf60c1f0e0ac09e1cb9eb8ed28e7bcdaa52129cffc7f4b04
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-python
Name:           rust-tree-sitter-python
Version:        0.23.6
Release:        1%{?dist}
Summary:        Python grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-python
Source0:        https://static.crates.io/crates/tree-sitter-python/tree-sitter-python-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-python-fix-metadata.diff
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
Summary:        Python grammar for tree-sitter
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
%files -n rust-tree-sitter-python-devel -f %{oreon_filedir}/rust-tree-sitter-python-devel.list

%changelog

%autochangelog
