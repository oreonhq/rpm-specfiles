%global source0_hash 4d727acca406c0020cffc6cf35516764f36c8e3dc4408e5ebe2cb35a947ec471
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-json
Name:           rust-tree-sitter-json
Version:        0.24.8
Release:        1%{?dist}
Summary:        JSON grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-json
Source0:        https://static.crates.io/crates/tree-sitter-json/tree-sitter-json-%{version}.crate
Patch:          tree-sitter-json-fix-metadata.diff
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
Summary:        JSON grammar for tree-sitter
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
%files -n rust-tree-sitter-json-devel -f %{oreon_filedir}/rust-tree-sitter-json-devel.list

%changelog

%autochangelog
