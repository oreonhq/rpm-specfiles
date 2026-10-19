%global source1_hash 2e0110e07abef7c2548b26ec9d6969775617ca539a0dc8dbeeb14d6452c711d1
%global source0_hash 977c51e504548cba13fc27cb5a2edab2124cf6716a1934915d07ab99523b05a4
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-haskell
Name:           rust-tree-sitter-haskell
Version:        0.23.1
Release:        1%{?dist}
Summary:        Haskell grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-haskell
Source0:        https://static.crates.io/crates/tree-sitter-haskell/tree-sitter-haskell-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-haskell-fix-metadata.diff
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
Summary:        Haskell grammar for tree-sitter
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
%files -n rust-tree-sitter-haskell-devel -f %{oreon_filedir}/rust-tree-sitter-haskell-devel.list

%changelog

%autochangelog
