%global source0_hash 4eacf8875b70879f0cb670c60b233ad0b68752d9e1474e6c3ef168eea8a90b25
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-solidity
Name:           rust-tree-sitter-solidity
Version:        1.2.13
Release:        1%{?dist}
Summary:        Solidity grammar for the tree-sitter parsing library
License:        MIT
URL:            https://crates.io/crates/tree-sitter-solidity
Source0:        https://static.crates.io/crates/tree-sitter-solidity/tree-sitter-solidity-%{version}.crate
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
Summary:        Solidity grammar for the tree-sitter parsing library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-tree-sitter-solidity-devel -f %{oreon_filedir}/rust-tree-sitter-solidity-devel.list

%changelog

%autochangelog
