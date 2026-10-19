%global source2_hash c5cfb43042b6b72045f4ba997834d0a7786d2793d91680868b5815b39f14fc78
%global source0_hash 9832e5d5867f05cbcf038cfa6001643efd3c270aa24605b2f90b91590eaf5b0d
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-config
Name:           rust-tree-sitter-config
Version:        0.27.0
Release:        1%{?dist}
Summary:        User configuration of tree-sitter's command line programs
License:        MIT
URL:            https://crates.io/crates/tree-sitter-config
Source0:        https://static.crates.io/crates/tree-sitter-config/tree-sitter-config-%{version}.crate
Source2:        https://github.com/tree-sitter/tree-sitter/raw/v%{version}/LICENSE#/LICENSE.upstream
Patch:          tree-sitter-config-fix-metadata.diff
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
Summary:        User configuration of tree-sitter's command line programs
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
%files -n rust-tree-sitter-config-devel -f %{oreon_filedir}/rust-tree-sitter-config-devel.list

%changelog

%autochangelog
