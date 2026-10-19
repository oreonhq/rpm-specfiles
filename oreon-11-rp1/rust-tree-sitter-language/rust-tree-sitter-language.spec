%global source2_hash 5f9cf9fb6acb1972b35ae29119ce563bb60ec097656bc4b69b9bac2d04c7a147
%global source0_hash c4013970217383f67b18aef68f6fb2e8d409bc5755227092d32efb0422ba24b8
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-language
Name:           rust-tree-sitter-language
Version:        0.1.5
Release:        1%{?dist}
Summary:        Tree-sitter Language type, used by the library and by language implementations
License:        MIT
URL:            https://crates.io/crates/tree-sitter-language
Source0:        https://static.crates.io/crates/tree-sitter-language/tree-sitter-language-%{version}.crate
Source2:        https://github.com/tree-sitter/tree-sitter/raw/v0.23.2/LICENSE#/LICENSE.upstream
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
Summary:        Tree-sitter Language type, used by the library and by language implementations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} LICENSE
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
%files -n rust-tree-sitter-language-devel -f %{oreon_filedir}/rust-tree-sitter-language-devel.list

%changelog

%autochangelog
