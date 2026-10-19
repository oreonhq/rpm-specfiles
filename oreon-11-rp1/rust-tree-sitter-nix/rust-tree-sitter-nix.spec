%global source1_hash c1b72e50266464ec5118d26200e17bf1f472d142e62ab637e1ffc23986657a78
%global source0_hash 3a8d4f8705d377d63242a075331d2d8c1dcc9828fd74aa13d7145185b3d9c004
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-nix
Name:           rust-tree-sitter-nix
Version:        0.0.2
Release:        1%{?dist}
Summary:        Nix grammar for the tree-sitter parsing library
License:        MIT
URL:            https://crates.io/crates/tree-sitter-nix
Source0:        https://static.crates.io/crates/tree-sitter-nix/tree-sitter-nix-%{version}.crate
Source1:        https://raw.githubusercontent.com/nix-community/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-nix-fix-metadata.diff
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
Summary:        Nix grammar for the tree-sitter parsing library
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
%files -n rust-tree-sitter-nix-devel -f %{oreon_filedir}/rust-tree-sitter-nix-devel.list

%changelog

%autochangelog
