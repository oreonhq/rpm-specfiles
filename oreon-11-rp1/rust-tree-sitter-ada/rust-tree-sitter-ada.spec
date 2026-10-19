%global source1_hash ad8425038de519f8c4e3e9339feebf99dfad8a6002dcf79227d91402780a32cc
%global source0_hash 8d9fcdd64359c98fcc99d72f6d3d6ca5d6d76ce325ac39430b1d283a0fb61ca1
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-ada
Name:           rust-tree-sitter-ada
Version:        0.1.0
Release:        1%{?dist}
Summary:        Ada grammar for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-ada
Source0:        https://static.crates.io/crates/tree-sitter-ada/tree-sitter-ada-%{version}.crate
Source1:        https://raw.githubusercontent.com/briot/tree-sitter-ada/ba7951a8f3fb08f9ea923625153e7670c89f30b4/LICENSE.txt
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
Summary:        Ada grammar for tree-sitter
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
cp -p LICENSE.txt %{buildroot}%{crate_instdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tree-sitter-ada-devel -f %{oreon_filedir}/rust-tree-sitter-ada-devel.list

%changelog

%autochangelog
