%global source0_hash e0bccbcf40c8938196944a3da0e133e031a33f4d6b72db3bda3cc556e361905d
%bcond check 0
%global debug_package %{nil}
%global crate serial_test
Name:           rust-serial_test0.5
Version:        0.5.1
Release:        1%{?dist}
Summary:        Allows for the creation of serialised Rust tests
License:        MIT
URL:            https://crates.io/crates/serial_test
Source0:        https://static.crates.io/crates/serial_test/serial_test-%{version}.crate
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
Summary:        Allows for the creation of serialised Rust tests
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
%files -n rust-serial_test0.5-devel -f %{oreon_filedir}/rust-serial_test0.5-devel.list

%changelog

%autochangelog
