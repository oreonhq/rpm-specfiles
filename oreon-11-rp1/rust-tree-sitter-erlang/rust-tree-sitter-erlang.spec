%global source1_hash c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
%global source0_hash eb9265a444b04975b2ecc2e1a64114a03e009737e7fae19ce9078b962b8be1af
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-erlang
Name:           rust-tree-sitter-erlang
Version:        0.13.0
Release:        1%{?dist}
Summary:        Erlang grammar for the tree-sitter parsing library
License:        MIT
URL:            https://crates.io/crates/tree-sitter-erlang
Source0:        https://static.crates.io/crates/tree-sitter-erlang/tree-sitter-erlang-%{version}.crate
Source1:        https://raw.githubusercontent.com/WhatsApp/tree-sitter-erlang/364e323b32d098ad0e7b29e7adb4005c2bb5cf34/LICENSE
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
Summary:        Erlang grammar for the tree-sitter parsing library
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
%files -n rust-tree-sitter-erlang-devel -f %{oreon_filedir}/rust-tree-sitter-erlang-devel.list

%changelog

%autochangelog
