%global source0_hash 8d1296fab5231654a5aec8bf9e87ba4e3938c502fc4c3c0425a00084c78944be
%bcond check 1
%global debug_package %{nil}
%global crate open-enum-derive
Name:           rust-open-enum-derive
Version:        0.5.2
Release:        1%{?dist}
Summary:        Attribute for generating "open" fieldless enums that accept any integer value
License:        Apache-2.0
URL:            https://crates.io/crates/open-enum-derive
Source0:        https://static.crates.io/crates/open-enum-derive/open-enum-derive-%{version}.crate
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
Summary:        Attribute for generating "open" fieldless enums that accept any integer value
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+repr_c-devel
Summary:        Attribute for generating "open" fieldless enums that accept any integer value
BuildArch:      noarch
%description -n %{name}+repr_c-devel

This package contains library source intended for building other packages which
use the "repr_c" feature of the "%{crate}" crate.

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
%files -n rust-open-enum-derive-devel -f %{oreon_filedir}/rust-open-enum-derive-devel.list

%changelog

%autochangelog
