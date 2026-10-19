%global source2_hash 31d5b6f4243d5c7c6e1c4ebbbb9f6407bd1457a08bcc4f706521710341acba36
%global source0_hash a4d64d449ca63e683c562c7743946a646671ca23947b9c925c0cfbe65051a4af
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-rust
Name:           rust-tree-sitter-rust
Version:        0.23.2
Release:        1%{?dist}
Summary:        Rust grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-rust
Source0:        https://static.crates.io/crates/tree-sitter-rust/tree-sitter-rust-%{version}.crate
Source2:        https://raw.githubusercontent.com/tree-sitter/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-rust-fix-metadata.diff
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
Summary:        Rust grammar for tree-sitter
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE2} .
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
%files -n rust-tree-sitter-rust-devel -f %{oreon_filedir}/rust-tree-sitter-rust-devel.list

%changelog

%autochangelog
