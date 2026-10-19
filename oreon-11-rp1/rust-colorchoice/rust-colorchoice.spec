%global source0_hash 1d07550c9036bf2ae0c684c4297d503f838287c83c53686d05370d0e139ae570
%bcond check 1
%global debug_package %{nil}
%global crate colorchoice
Name:           rust-colorchoice
Version:        1.0.5
Release:        1%{?dist}
Summary:        Global override of color control
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/colorchoice
Source0:        https://static.crates.io/crates/colorchoice/colorchoice-%{version}.crate
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
Summary:        Global override of color control
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
%files -n rust-colorchoice-devel -f %{oreon_filedir}/rust-colorchoice-devel.list

%changelog

%autochangelog
