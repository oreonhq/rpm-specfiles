%global source0_hash 3ae8337f8a065cfc972643663ea4279e04e7256de865aa66fe25cec5fb912d3f
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate xml-rs
Name:           rust-xml-rs
Version:        0.8.28
Release:        1%{?dist}
Summary:        XML library in pure Rust
License:        MIT
URL:            https://crates.io/crates/xml-rs
Source0:        https://static.crates.io/crates/xml-rs/xml-rs-%{version}.crate
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
Summary:        XML library in pure Rust
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
%files -n rust-xml-rs-devel -f %{oreon_filedir}/rust-xml-rs-devel.list

%changelog

%autochangelog
