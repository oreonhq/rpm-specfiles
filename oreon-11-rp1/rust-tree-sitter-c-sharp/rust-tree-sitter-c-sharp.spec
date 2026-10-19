%global source0_hash 67f06accca7b45351758663b8215089e643d53bd9a660ce0349314263737fcb0
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-c-sharp
Name:           rust-tree-sitter-c-sharp
Version:        0.23.1
Release:        1%{?dist}
Summary:        C# grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-c-sharp
Source0:        https://static.crates.io/crates/tree-sitter-c-sharp/tree-sitter-c-sharp-%{version}.crate
Patch:          tree-sitter-c-sharp-fix-metadata.diff
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
Summary:        C# grammar for tree-sitter
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
%files -n rust-tree-sitter-c-sharp-devel -f %{oreon_filedir}/rust-tree-sitter-c-sharp-devel.list

%changelog

%autochangelog
