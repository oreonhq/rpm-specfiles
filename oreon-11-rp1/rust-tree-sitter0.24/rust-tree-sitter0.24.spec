%global source2_hash 5f9cf9fb6acb1972b35ae29119ce563bb60ec097656bc4b69b9bac2d04c7a147
%global source0_hash a5387dffa7ffc7d2dae12b50c6f7aab8ff79d6210147c6613561fc3d474c6f75
%bcond check 0
%global debug_package %{nil}
%global crate tree-sitter
Name:           rust-tree-sitter0.24
Version:        0.24.7
Release:        1%{?dist}
Summary:        Rust bindings to the Tree-sitter parsing library
License:        MIT AND Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://crates.io/crates/tree-sitter
Source0:        https://static.crates.io/crates/tree-sitter/tree-sitter-%{version}.crate
Source2:        https://github.com/tree-sitter/tree-sitter/raw/v%{version}/LICENSE#/LICENSE.upstream
Patch:          tree-sitter-fix-metadata.diff
Patch2:         tree-sitter-build-bindings-unconditionally.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(tree-sitter) = %{version}
Provides:       bundled(icu) = 65.1
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust bindings to the Tree-sitter parsing library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust bindings to the Tree-sitter parsing library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -f binding_rust/bindings.rs
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
install -D -m 0644 -pv %{SOURCE2} %{buildroot}%{crate_instdir}/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter0.24-devel -f %{oreon_filedir}/rust-tree-sitter0.24-devel.list

%changelog

%autochangelog
