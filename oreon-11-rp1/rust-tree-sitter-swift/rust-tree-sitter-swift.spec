%global source1_hash 3533cec129bb4bba015c0d61d86dd7c3b7e82110e4d2ff7837a01eff5bad5ccc
%global source0_hash 4ef216011c3e3df4fa864736f347cb8d509b1066cf0c8549fb1fd81ac9832e59
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-swift
Name:           rust-tree-sitter-swift
Version:        0.7.1
Release:        1%{?dist}
Summary:        Swift grammar for the tree-sitter parsing library
License:        MIT
URL:            https://crates.io/crates/tree-sitter-swift
Source0:        https://static.crates.io/crates/tree-sitter-swift/tree-sitter-swift-%{version}.crate
Source1:        https://raw.githubusercontent.com/alex-pinkus/tree-sitter-swift/refs/tags/%{version}/LICENSE
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
Summary:        Swift grammar for the tree-sitter parsing library
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

%{cargo_test -- -- %{shrink:
    --skip tests::test_can_load_grammar
    --skip tests::test_can_parse_basic_file
    --skip bindings/rust/lib.rs
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-swift-devel -f %{oreon_filedir}/rust-tree-sitter-swift-devel.list

%changelog

%autochangelog
