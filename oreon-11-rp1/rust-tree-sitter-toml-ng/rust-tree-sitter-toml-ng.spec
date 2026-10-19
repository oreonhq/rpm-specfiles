%global source1_hash b727eee929bee836e8102cecf749a795b199f291b58c885bcd81cae727ac5a46
%global source0_hash e9adc2c898ae49730e857d75be403da3f92bb81d8e37a2f918a08dd10de5ebb1
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-toml-ng
Name:           rust-tree-sitter-toml-ng
Version:        0.7.0
Release:        1%{?dist}
Summary:        TOML grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-toml-ng
Source0:        https://static.crates.io/crates/tree-sitter-toml-ng/tree-sitter-toml-ng-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter-grammars/tree-sitter-toml/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-toml-ng-fix-metadata.diff
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
Summary:        TOML grammar for tree-sitter
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
%files -n rust-tree-sitter-toml-ng-devel -f %{oreon_filedir}/rust-tree-sitter-toml-ng-devel.list

%changelog

%autochangelog
