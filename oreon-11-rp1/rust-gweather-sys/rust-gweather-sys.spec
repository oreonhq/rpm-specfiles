%global source0_hash 5bd48d8a64d00703dc2a77efb2284c07192a1345d0162e0bc15488b55d577f0e
%bcond check 1
%global debug_package %{nil}
%global crate gweather-sys
Name:           rust-gweather-sys
Version:        4.8.0
Release:        1%{?dist}
Summary:        FFI bindings for libgweather
License:        MIT
URL:            https://crates.io/crates/gweather-sys
Source0:        https://static.crates.io/crates/gweather-sys/gweather-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gweather4) >= 4
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings for libgweather
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
%files -n rust-gweather-sys-devel -f %{oreon_filedir}/rust-gweather-sys-devel.list

%changelog

%autochangelog
