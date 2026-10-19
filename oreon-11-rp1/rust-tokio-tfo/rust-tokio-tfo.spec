%global source0_hash 1e3d7ba01a66a3a6dedebca3788232547ac193b31530bb625cb42eeb8e5154b6
%bcond check 1
%global debug_package %{nil}
%global crate tokio-tfo
Name:           rust-tokio-tfo
Version:        0.3.4
Release:        1%{?dist}
Summary:        TCP Fast Open (TFO) in Rust for tokio
License:        MIT
URL:            https://crates.io/crates/tokio-tfo
Source0:        https://static.crates.io/crates/tokio-tfo/tokio-tfo-%{version}.crate
Patch:          tokio-tfo-fix-metadata-auto.diff
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
Summary:        TCP Fast Open (TFO) in Rust for tokio
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
%files -n rust-tokio-tfo-devel -f %{oreon_filedir}/rust-tokio-tfo-devel.list

%changelog

%autochangelog
