%global source0_hash 2d76fac0a007075fa8d38a6ec08df340bea2035cc0a6e9b0f6594bff1627692b
%bcond check 0
%global debug_package %{nil}
%global crate clang-ast
Name:           rust-clang-ast
Version:        0.1.35
Release:        1%{?dist}
Summary:        Data structures for processing Clang's -ast-dump=json format
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clang-ast
Source0:        https://static.crates.io/crates/clang-ast/clang-ast-%{version}.crate
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
Summary:        Data structures for processing Clang's -ast-dump=json format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Data structures for processing Clang's -ast-dump=json format
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-clang-ast-devel -f %{oreon_filedir}/rust-clang-ast-devel.list

%changelog

%autochangelog
