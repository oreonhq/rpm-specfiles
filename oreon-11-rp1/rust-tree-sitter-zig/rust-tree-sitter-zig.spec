%global source1_hash 0eea8dc45e89deeb03c7799bbbc7b4688f365fb274562f4540ecfebdea82e727
%global source0_hash ab11fc124851b0db4dd5e55983bbd9631192e93238389dcd44521715e5d53e28
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-zig
Name:           rust-tree-sitter-zig
Version:        1.1.2
Release:        1%{?dist}
Summary:        Zig grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-zig
Source0:        https://static.crates.io/crates/tree-sitter-zig/tree-sitter-zig-%{version}.crate
Source1:        https://raw.githubusercontent.com/michel-slm/tree-sitter-zig/b71affffdb4222ff2d2dea6e164f76603b0be6bc/LICENSE
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
Summary:        Zig grammar for tree-sitter
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
%files -n rust-tree-sitter-zig-devel -f %{oreon_filedir}/rust-tree-sitter-zig-devel.list

%changelog

%autochangelog
