%global source0_hash bf40bf599e0416c16c125c3cec10ee5ddc7d1bb8b0c60fa5c4de249ad34dc1b1
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-javascript
Name:           rust-tree-sitter-javascript
Version:        0.23.1
Release:        1%{?dist}
Summary:        JavaScript grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-javascript
Source0:        https://static.crates.io/crates/tree-sitter-javascript/tree-sitter-javascript-%{version}.crate
Patch:          tree-sitter-javascript-fix-metadata.diff
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
Summary:        JavaScript grammar for tree-sitter
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
%files -n rust-tree-sitter-javascript-devel -f %{oreon_filedir}/rust-tree-sitter-javascript-devel.list

%changelog

%autochangelog
