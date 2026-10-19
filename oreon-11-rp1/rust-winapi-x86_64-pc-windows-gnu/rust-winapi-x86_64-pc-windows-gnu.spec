%global source0_hash 712e227841d057c1ee1cd2fb22fa7e5a5461ae8e48fa2ca79ec42cfc1931183f
%bcond check 0
%global debug_package %{nil}
%global crate winapi-x86_64-pc-windows-gnu
Name:           rust-winapi-x86_64-pc-windows-gnu
Version:        0.4.0
Release:        1%{?dist}
Summary:        Import libraries for the Windows API, x86_64
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/winapi-x86_64-pc-windows-gnu
Source0:        https://static.crates.io/crates/winapi-x86_64-pc-windows-gnu/winapi-x86_64-pc-windows-gnu-%{version}.crate
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
use the "winapi-x86_64-pc-windows-gnu" crate.

%package     -n %{name}+default-devel
Summary:        Import libraries for the Windows API, x86_64
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-winapi-x86_64-pc-windows-gnu-devel -f %{oreon_filedir}/rust-winapi-x86_64-pc-windows-gnu-devel.list

%changelog

%autochangelog
