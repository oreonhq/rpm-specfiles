%global source1_hash 099c44248f8cf353123211318680e93465587c005a4b3730ce8cb5334de043d6
%global source0_hash 9ca8bb556423fc176f0535e79d525f783a6684d3c9da81bf9d905303c129e1d2
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-objc
Name:           rust-tree-sitter-objc
Version:        3.0.2
Release:        1%{?dist}
Summary:        Objective-C grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-objc
Source0:        https://static.crates.io/crates/tree-sitter-objc/tree-sitter-objc-%{version}.crate
Source1:        https://raw.githubusercontent.com/tree-sitter-grammars/%{crate}/refs/tags/v%{version}/LICENSE
Patch:          tree-sitter-objc-fix-metadata.diff
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
Summary:        Objective-C grammar for tree-sitter
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
%files -n rust-tree-sitter-objc-devel -f %{oreon_filedir}/rust-tree-sitter-objc-devel.list

%changelog

%autochangelog
