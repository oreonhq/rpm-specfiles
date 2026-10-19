%global source0_hash 022dfe9eb35f19ebbcb51e0b40a5ab759f46ad60cadf7297e0bd085afb50e076
%bcond check 0
%global debug_package %{nil}
%global crate base32
Name:           rust-base32
Version:        0.5.1
Release:        1%{?dist}
Summary:        Encoder/decoder for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/base32
Source0:        https://static.crates.io/crates/base32/base32-%{version}.crate
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
Summary:        Encoder/decoder for Rust
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
%files -n rust-base32-devel -f %{oreon_filedir}/rust-base32-devel.list

%changelog

%autochangelog
