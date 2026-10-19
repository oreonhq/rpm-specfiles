%global source0_hash 3f1646788fe0afdbf8e191b5d0f558df7333d8857665a67053c532ec811e6086
%bcond check 1
%global debug_package %{nil}
%global crate tree-house-bindings
Name:           rust-tree-house-bindings
Version:        0.2.1
Release:        1%{?dist}
Summary:        Homey Rust bindings for the tree-sitter C library
License:        MPL-2.0 AND MIT AND Unicode-DFS-2016
URL:            https://crates.io/crates/tree-house-bindings
Source0:        https://static.crates.io/crates/tree-house-bindings/tree-house-bindings-%{version}.crate
Patch:          tree-house-bindings-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(tree-sitter) = 0.25.7
Provides:       bundled(icu) = 65.1
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Homey Rust bindings for the tree-sitter C library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ropey-devel
Summary:        Homey Rust bindings for the tree-sitter C library
BuildArch:      noarch
%description -n %{name}+ropey-devel

This package contains library source intended for building other packages which
use the "ropey" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-tree-house-bindings-devel -f %{oreon_filedir}/rust-tree-house-bindings-devel.list

%changelog

%autochangelog
