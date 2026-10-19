%global source2_hash 2d181298822a124f6d106118dcc69c8d4d26ac668559be29682c452e712b0947
%global source0_hash d0c99f2b92b677f1a18b6b232fa9329afb5758118238a7d0b29cae324ef50d5e
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-yaml
Name:           rust-tree-sitter-yaml
Version:        0.7.0
Release:        1%{?dist}
Summary:        YAML grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-yaml
Source0:        https://static.crates.io/crates/tree-sitter-yaml/tree-sitter-yaml-%{version}.crate
Source2:        https://raw.githubusercontent.com/tree-sitter-grammars/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-yaml-fix-metadata.diff
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
Summary:        YAML grammar for tree-sitter
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE2} .
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
%files -n rust-tree-sitter-yaml-devel -f %{oreon_filedir}/rust-tree-sitter-yaml-devel.list

%changelog

%autochangelog
