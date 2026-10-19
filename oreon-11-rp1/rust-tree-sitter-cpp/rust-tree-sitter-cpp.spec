%global source0_hash df2196ea9d47b4ab4a31b9297eaa5a5d19a0b121dceb9f118f6790ad0ab94743
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-cpp
Name:           rust-tree-sitter-cpp
Version:        0.23.4
Release:        1%{?dist}
Summary:        C++ grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-cpp
Source0:        https://static.crates.io/crates/tree-sitter-cpp/tree-sitter-cpp-%{version}.crate
Patch:          tree-sitter-cpp-fix-metadata.diff
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
Summary:        C++ grammar for tree-sitter
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
%files -n rust-tree-sitter-cpp-devel -f %{oreon_filedir}/rust-tree-sitter-cpp-devel.list

%changelog

%autochangelog
