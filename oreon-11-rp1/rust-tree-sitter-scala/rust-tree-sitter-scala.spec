%global source1_hash 1f95ed26e1f4074074c9c7083e61c0a9e4c3b9f435745044995f3beb4ed28575
%global source0_hash efde5e68b4736e9eac17bfa296c6f104a26bffab363b365eb898c40a63c15d2f
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-scala
Name:           rust-tree-sitter-scala
Version:        0.23.4
Release:        1%{?dist}
Summary:        Scala grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-scala
Source0:        https://static.crates.io/crates/tree-sitter-scala/tree-sitter-scala-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-scala-fix-metadata.diff
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
Summary:        Scala grammar for tree-sitter
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
%files -n rust-tree-sitter-scala-devel -f %{oreon_filedir}/rust-tree-sitter-scala-devel.list

%changelog

%autochangelog
