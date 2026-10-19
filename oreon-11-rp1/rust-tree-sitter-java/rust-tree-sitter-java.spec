%global source0_hash 0aa6cbcdc8c679b214e616fd3300da67da0e492e066df01bcf5a5921a71e90d6
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-java
Name:           rust-tree-sitter-java
Version:        0.23.5
Release:        1%{?dist}
Summary:        Java grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-java
Source0:        https://static.crates.io/crates/tree-sitter-java/tree-sitter-java-%{version}.crate
Patch:          tree-sitter-java-fix-metadata.diff
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
Summary:        Java grammar for tree-sitter
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
%files -n rust-tree-sitter-java-devel -f %{oreon_filedir}/rust-tree-sitter-java-devel.list

%changelog

%autochangelog
