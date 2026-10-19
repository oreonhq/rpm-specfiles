%global source0_hash fe4d98d0065f4b1daf164b3eafb11974c94662e5e2396cf03f32d0bb5c17da51
%bcond check 0
%global debug_package %{nil}
%global crate nasm-rs
Name:           rust-nasm-rs0.2
Version:        0.2.5
Release:        1%{?dist}
Summary:        Run NASM during your Cargo build.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/nasm-rs
Source0:        https://static.crates.io/crates/nasm-rs/nasm-rs-%{version}.crate
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

%package     -n %{name}+parallel-devel
Summary:        Run NASM during your Cargo build.
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Run NASM during your Cargo build.
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

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
%files -n rust-nasm-rs0.2-devel -f %{oreon_filedir}/rust-nasm-rs0.2-devel.list

%changelog

%autochangelog
