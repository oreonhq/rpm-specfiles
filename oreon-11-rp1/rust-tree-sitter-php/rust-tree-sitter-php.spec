%global source1_hash 664764fabf40c0b318e06324a5a12379092a2df25b8cbf2415f71bc0bb352346
%global source0_hash f066e94e9272cfe4f1dcb07a1c50c66097eca648f2d7233d299c8ae9ed8c130c
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-php
Name:           rust-tree-sitter-php
Version:        0.23.11
Release:        1%{?dist}
Summary:        PHP grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-php
Source0:        https://static.crates.io/crates/tree-sitter-php/tree-sitter-php-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-php-fix-metadata.diff
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
Summary:        PHP grammar for tree-sitter
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
%files -n rust-tree-sitter-php-devel -f %{oreon_filedir}/rust-tree-sitter-php-devel.list

%changelog

%autochangelog
