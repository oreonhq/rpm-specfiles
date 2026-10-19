%global source0_hash a6ef517f0926dd24a1582492c791b6a4818a4d94e789a334894aa15b0d12f55c
%bcond check 0
%global debug_package %{nil}
%global crate const-oid
Name:           rust-const-oid0.10
Version:        0.10.2
Release:        1%{?dist}
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID)...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/const-oid
Source0:        https://static.crates.io/crates/const-oid/const-oid-%{version}.crate
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

%package     -n %{name}+arbitrary-devel
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID)...
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+db-devel
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID)...
BuildArch:      noarch
%description -n %{name}+db-devel

This package contains library source intended for building other packages which
use the "db" feature of the "%{crate}" crate.

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
%files -n rust-const-oid0.10-devel -f %{oreon_filedir}/rust-const-oid0.10-devel.list

%changelog

%autochangelog
