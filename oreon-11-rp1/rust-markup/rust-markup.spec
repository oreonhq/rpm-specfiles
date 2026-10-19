%global source0_hash be10fa8085360758d551c6577b0692c9e7614d2d743036cf2fa452476a3e0569
%bcond check 0
%global debug_package %{nil}
%global crate markup
Name:           rust-markup
Version:        0.16.0
Release:        1%{?dist}
Summary:        A blazing fast, type-safe template engine for Rust.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/markup
Source0:        https://static.crates.io/crates/markup/markup-%{version}.crate
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
Summary:        A blazing fast, type-safe template engine for Rust.
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
%files -n rust-markup-devel -f %{oreon_filedir}/rust-markup-devel.list

%changelog

%autochangelog
