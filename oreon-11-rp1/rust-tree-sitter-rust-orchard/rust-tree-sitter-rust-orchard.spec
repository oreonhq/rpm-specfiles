%global source0_hash 42e06f00ca89feba4d7455e95b61b9019a979a380527297fab0c461e2e13c264
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-rust-orchard
Name:           rust-tree-sitter-rust-orchard
Version:        0.13.0
Release:        1%{?dist}
Summary:        Grammar for Rust that aims to be closer to the actual AST
License:        MIT
URL:            https://crates.io/crates/tree-sitter-rust-orchard
Source0:        https://static.crates.io/crates/tree-sitter-rust-orchard/tree-sitter-rust-orchard-%{version}.crate
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
Summary:        Grammar for Rust that aims to be closer to the actual AST
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-tree-sitter-rust-orchard-devel -f %{oreon_filedir}/rust-tree-sitter-rust-orchard-devel.list

%changelog

%autochangelog
