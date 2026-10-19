%global source0_hash 08c5785bcf2ade84e16242b1a8d1f574334ddd26032c15a5d9bcc012e013f4e1
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-newick
Name:           rust-tree-sitter-newick
Version:        1.1.0
Release:        1%{?dist}
Summary:        Parser for (extended) Newick files (nh, nwk, nhx)
License:        CECILL-C
URL:            https://crates.io/crates/tree-sitter-newick
Source0:        https://static.crates.io/crates/tree-sitter-newick/tree-sitter-newick-%{version}.crate
Patch:          tree-sitter-newick-fix-metadata.diff
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
Summary:        Parser for (extended) Newick files (nh, nwk, nhx)
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
%files -n rust-tree-sitter-newick-devel -f %{oreon_filedir}/rust-tree-sitter-newick-devel.list

%changelog

%autochangelog
