%global source0_hash 312d2295c7302019c395cfb90dacd00a82a2eabd700429bba9c7a3f38dbbe11b
%bcond check 1
%global debug_package %{nil}
%global crate g2poly
Name:           rust-g2poly
Version:        1.2.2
Release:        1%{?dist}
Summary:        Primitive implementation of polynomials over the field GF(2)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/g2poly
Source0:        https://static.crates.io/crates/g2poly/g2poly-%{version}.crate
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
Summary:        Primitive implementation of polynomials over the field GF(2)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-g2poly-devel -f %{oreon_filedir}/rust-g2poly-devel.list

%changelog

%autochangelog
