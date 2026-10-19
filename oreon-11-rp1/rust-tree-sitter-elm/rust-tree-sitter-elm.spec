%global source1_hash 26f7bf09693dd895ea64777316bad0133b131a8478a660b4785d4b9d1322f9a1
%global source0_hash 807f387a83c88d894b978edeff024f26a2935505de83237f57c77f9aa2de4ee7
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-elm
Name:           rust-tree-sitter-elm
Version:        5.9.4
Release:        1%{?dist}
Summary:        Elm grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-elm
Source0:        https://static.crates.io/crates/tree-sitter-elm/tree-sitter-elm-%{version}.crate
Source1:        https://raw.githubusercontent.com/elm-tooling/tree-sitter-elm/refs/tags/v%{version}/LICENSE.md
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
Summary:        Elm grammar for tree-sitter
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
cp -p LICENSE.md %{buildroot}%{crate_instdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-elm-devel -f %{oreon_filedir}/rust-tree-sitter-elm-devel.list

%changelog

%autochangelog
