%global source0_hash 6fe2267d4ed49bc07b63801559be28c718ea06c4738b7a03c94df7386d2cde46
%bcond check 0
%global debug_package %{nil}
%global crate hex-literal
Name:           rust-hex-literal0.4
Version:        0.4.1
Release:        1%{?dist}
Summary:        Macro for converting hexadecimal string to a byte array at compile time
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hex-literal
Source0:        https://static.crates.io/crates/hex-literal/hex-literal-%{version}.crate
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
Summary:        Macro for converting hexadecimal string to a byte array at compile time
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
%files -n rust-hex-literal0.4-devel -f %{oreon_filedir}/rust-hex-literal0.4-devel.list

%changelog

%autochangelog
