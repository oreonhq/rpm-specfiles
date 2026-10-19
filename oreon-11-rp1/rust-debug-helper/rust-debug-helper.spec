%global source0_hash 80a4af69c60438a1a82af89d362f4729fd38db7b73f305a237636fad31ceb2bf
%bcond check 0
%global debug_package %{nil}
%global crate debug-helper
Name:           rust-debug-helper
Version:        0.3.14
Release:        1%{?dist}
Summary:        Declarative macros to help you implement the Debug trait manually
License:        MIT
URL:            https://crates.io/crates/debug-helper
Source0:        https://static.crates.io/crates/debug-helper/debug-helper-%{version}.crate
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
Summary:        Declarative macros to help you implement the Debug trait manually
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
%files -n rust-debug-helper-devel -f %{oreon_filedir}/rust-debug-helper-devel.list

%changelog

%autochangelog
