%global source1_hash f977a20805dd6e275f14bc090a5f8e638401dad4df366841c1060f12c75b74ae
%global source0_hash 43adb10fcccbcbbce0f4adc9dab7cd55f0a5eafc2d71bd4c03fcc5d6767066e0
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-ocaml
Name:           rust-tree-sitter-ocaml
Version:        0.26.0
Release:        1%{?dist}
Summary:        OCaml grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-ocaml
Source0:        https://static.crates.io/crates/tree-sitter-ocaml/tree-sitter-ocaml-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-ocaml-fix-metadata.diff
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
Summary:        OCaml grammar for tree-sitter
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
%files -n rust-tree-sitter-ocaml-devel -f %{oreon_filedir}/rust-tree-sitter-ocaml-devel.list

%changelog

%autochangelog
