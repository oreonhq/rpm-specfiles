%global source0_hash c2459377285ad874054d797f3ccebf984978aa39129f6eafde5cdc8315b612f8
%bcond check 1
%global debug_package %{nil}
%global crate const-oid
Name:           rust-const-oid0.9
Version:        0.9.6
Release:        1%{?dist}
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
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

%package     -n %{name}+default-devel
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+db-devel
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
BuildArch:      noarch
%description -n %{name}+db-devel

This package contains library source intended for building other packages which
use the "db" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard
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
%files -n rust-const-oid0.9-devel -f %{oreon_filedir}/rust-const-oid0.9-devel.list

%changelog

%autochangelog
