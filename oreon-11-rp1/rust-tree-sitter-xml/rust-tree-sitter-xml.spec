%global source0_hash e670041f591d994f54d597ddcd8f4ebc930e282c4c76a42268743b71f0c8b6b3
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-xml
Name:           rust-tree-sitter-xml
Version:        0.7.0
Release:        1%{?dist}
Summary:        XML & DTD grammars for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-xml
Source0:        https://static.crates.io/crates/tree-sitter-xml/tree-sitter-xml-%{version}.crate
Patch:          tree-sitter-xml-fix-metadata.diff
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
Summary:        XML & DTD grammars for tree-sitter
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
%files -n rust-tree-sitter-xml-devel -f %{oreon_filedir}/rust-tree-sitter-xml-devel.list

%changelog

%autochangelog
