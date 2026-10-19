%global source0_hash 54ef5ffec8bc52ded04ee424ab8d959e25e64fd40a48a16d21f8991ce824c1bb
%bcond check 0
%global debug_package %{nil}
%global crate sval_ref
Name:           rust-sval_ref
Version:        2.20.0
Release:        1%{?dist}
Summary:        A variant of sval::Value for types with internal references
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_ref
Source0:        https://static.crates.io/crates/sval_ref/sval_ref-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        A variant of sval::Value for types with internal references
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A variant of sval::Value for types with internal references
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-sval_ref-devel -f %{oreon_filedir}/rust-sval_ref-devel.list

%changelog

%autochangelog
