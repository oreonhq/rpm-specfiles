%global source2_hash 28eecdb75b6de2d9020603531461444bf54db827ee2fb345a8fcf4dbee7c2ad1
%global source0_hash c5998dc7cbcbdab19fae8aefef982bf2d6544513d8d2e69cc44aec4c63810104
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-make
Name:           rust-tree-sitter-make
Version:        1.1.1
Release:        1%{?dist}
Summary:        Makefile grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-make
Source0:        https://static.crates.io/crates/tree-sitter-make/tree-sitter-make-%{version}.crate
Source2:        https://raw.githubusercontent.com/tree-sitter-grammars/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-make-fix-metadata.diff
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
Summary:        Makefile grammar for tree-sitter
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
%files -n rust-tree-sitter-make-devel -f %{oreon_filedir}/rust-tree-sitter-make-devel.list

%changelog

%autochangelog
