%global source1_hash cc35bd4a973bf6067558e88b56d9a369e02c36e240b2b537aef8f751b7808fd7
%global source0_hash f8395b6a054e6264c67e1ef915f239c4f86575b7d7c69638bdbf3c336c58f128
%bcond check 1
%global debug_package %{nil}
%global crate tree-sitter-racket
Name:           rust-tree-sitter-racket
Version:        0.24.7
Release:        1%{?dist}
Summary:        Racket parser for tree-sitter
License:        MIT
URL:            https://crates.io/crates/tree-sitter-racket
Source0:        https://static.crates.io/crates/tree-sitter-racket/tree-sitter-racket-%{version}.crate
Source1:        https://raw.githubusercontent.com/6cdh/tree-sitter-racket/refs/tags/v%{version}/LICENSE
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
Summary:        Racket parser for tree-sitter
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
%files -n rust-tree-sitter-racket-devel -f %{oreon_filedir}/rust-tree-sitter-racket-devel.list

%changelog

%autochangelog
