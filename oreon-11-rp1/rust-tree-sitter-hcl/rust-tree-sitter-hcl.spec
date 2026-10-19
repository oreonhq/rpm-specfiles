%global source0_hash 5a7b2cc3d7121553b84309fab9d11b3ff3d420403eef9ae50f9fd1cd9d9cf012
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-hcl
Name:           rust-tree-sitter-hcl
Version:        1.1.0
Release:        1%{?dist}
Summary:        HCL and terraform grammar for tree-sitter
License:        Apache-2.0
URL:            https://crates.io/crates/tree-sitter-hcl
Source0:        https://static.crates.io/crates/tree-sitter-hcl/tree-sitter-hcl-%{version}.crate
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
Summary:        HCL and terraform grammar for tree-sitter
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
%files -n rust-tree-sitter-hcl-devel -f %{oreon_filedir}/rust-tree-sitter-hcl-devel.list

%changelog

%autochangelog
