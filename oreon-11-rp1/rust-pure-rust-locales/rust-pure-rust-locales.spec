%global source0_hash 869675ad2d7541aea90c6d88c81f46a7f4ea9af8cd0395d38f11a95126998a0d
%bcond check 0
%global debug_package %{nil}
%global crate pure-rust-locales
Name:           rust-pure-rust-locales
Version:        0.8.2
Release:        1%{?dist}
Summary:        Pure Rust locales imported directly from the GNU C Library. `LC_COLLA...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pure-rust-locales
Source0:        https://static.crates.io/crates/pure-rust-locales/pure-rust-locales-%{version}.crate
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

%package     -n %{name}+defmt-devel
Summary:        Pure Rust locales imported directly from the GNU C Library. `LC_COLLA...
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

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
%files -n rust-pure-rust-locales-devel -f %{oreon_filedir}/rust-pure-rust-locales-devel.list

%changelog

%autochangelog
