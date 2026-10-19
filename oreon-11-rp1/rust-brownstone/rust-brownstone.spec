%global source0_hash c5839ee4f953e811bfdcf223f509cb2c6a3e1447959b0bff459405575bc17f22
%bcond check 0
%global debug_package %{nil}
%global crate brownstone
Name:           rust-brownstone
Version:        3.0.0
Release:        1%{?dist}
Summary:        Utilities for building fixed-size arrays
License:        MPL-2.0
URL:            https://crates.io/crates/brownstone
Source0:        https://static.crates.io/crates/brownstone/brownstone-%{version}.crate
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
Summary:        Utilities for building fixed-size arrays
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
%files -n rust-brownstone-devel -f %{oreon_filedir}/rust-brownstone-devel.list

%changelog

%autochangelog
