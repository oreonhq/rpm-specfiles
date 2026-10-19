%global source1_hash 1cc17f880ff4fa68079a72b98b89d42e8ce16b1bdbb1ec7b6f33465241e41003
%global source0_hash 9c93b6f1ed20de442e900eb636f2176af6063953dfaa9f76bf168dd3b490a3a1
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-proto
Name:           rust-tree-sitter-proto
Version:        0.6.0
Release:        1%{?dist}
Summary:        Parser for proto2 and proto3 files
License:        MIT
URL:            https://crates.io/crates/tree-sitter-proto
Source0:        https://static.crates.io/crates/tree-sitter-proto/tree-sitter-proto-%{version}.crate
Source1:        https://raw.githubusercontent.com/michel-slm/tree-sitter-proto/refs/heads/include-license/LICENSE
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
Summary:        Parser for proto2 and proto3 files
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
cp -p LICENSE %{buildroot}%{crate_instdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-proto-devel -f %{oreon_filedir}/rust-tree-sitter-proto-devel.list

%changelog

%autochangelog
