%global source0_hash e14ef017e15d2e5592a9e39a346c1dbaea5120bab7ed7106b210ef58ebd97003
%bcond check 0
%global debug_package %{nil}
%global crate pcsc-sys
Name:           rust-pcsc-sys
Version:        1.3.0
Release:        1%{?dist}
Summary:        Low-level bindings to the PC/SC C API
License:        MIT
URL:            https://crates.io/crates/pcsc-sys
Source0:        https://static.crates.io/crates/pcsc-sys/pcsc-sys-%{version}.crate
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
Summary:        Low-level bindings to the PC/SC C API
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
%files -n rust-pcsc-sys-devel -f %{oreon_filedir}/rust-pcsc-sys-devel.list

%changelog

%autochangelog
