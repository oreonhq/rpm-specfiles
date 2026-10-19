%global source1_hash f9352b63e87252b282b252bf27530027c8ca69829e0023f8b8b682a736f271fd
%global source0_hash f2db500a0948bf37c43febe2c3d67bfb9ad690b06aaa20780a5106da6f620b41
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-fsharp
Name:           rust-tree-sitter-fsharp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Fsharp grammar for the tree-sitter parsing library
License:        MIT
URL:            https://crates.io/crates/tree-sitter-fsharp
Source0:        https://static.crates.io/crates/tree-sitter-fsharp/tree-sitter-fsharp-%{version}.crate
Source1:        https://raw.githubusercontent.com/ionide/tree-sitter-fsharp/refs/tags/v%{version}/LICENSE
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
Summary:        Fsharp grammar for the tree-sitter parsing library
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
%files -n rust-tree-sitter-fsharp-devel -f %{oreon_filedir}/rust-tree-sitter-fsharp-devel.list

%changelog

%autochangelog
