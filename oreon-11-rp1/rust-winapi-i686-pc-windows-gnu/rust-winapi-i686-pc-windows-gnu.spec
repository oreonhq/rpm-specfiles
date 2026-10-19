%global source0_hash ac3b87c63620426dd9b991e5ce0329eff545bccbbb34f3be09ff6fb6ab51b7b6
%bcond check 0
%global debug_package %{nil}
%global crate winapi-i686-pc-windows-gnu
Name:           rust-winapi-i686-pc-windows-gnu
Version:        0.4.0
Release:        1%{?dist}
Summary:        Import libraries for the Windows API, i686
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/winapi-i686-pc-windows-gnu
Source0:        https://static.crates.io/crates/winapi-i686-pc-windows-gnu/winapi-i686-pc-windows-gnu-%{version}.crate
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
use the "winapi-i686-pc-windows-gnu" crate.

%package     -n %{name}+default-devel
Summary:        Import libraries for the Windows API, i686
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
%files -n rust-winapi-i686-pc-windows-gnu-devel -f %{oreon_filedir}/rust-winapi-i686-pc-windows-gnu-devel.list

%changelog

%autochangelog
