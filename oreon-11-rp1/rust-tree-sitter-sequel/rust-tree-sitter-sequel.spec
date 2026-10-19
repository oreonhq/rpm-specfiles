%global source1_hash 3b3e4e4252d5d7d1c18e1257005f23242bf0580ad619204fd093c99b8c56748d
%global source0_hash 9d198ad3c319c02e43c21efa1ec796b837afcb96ffaef1a40c1978fbdcec7d17
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-sequel
Name:           rust-tree-sitter-sequel
Version:        0.3.11
Release:        1%{?dist}
Summary:        Tree-sitter Grammar for SQL
License:        MIT
URL:            https://crates.io/crates/tree-sitter-sequel
Source0:        https://static.crates.io/crates/tree-sitter-sequel/tree-sitter-sequel-%{version}.crate
Source1:        https://raw.githubusercontent.com/DerekStride/tree-sitter-sql/refs/tags/v%{version}/LICENSE
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
Summary:        Tree-sitter Grammar for SQL
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
cp -p LICENSE %{buildroot}%{crate_instdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-sequel-devel -f %{oreon_filedir}/rust-tree-sitter-sequel-devel.list

%changelog

%autochangelog
