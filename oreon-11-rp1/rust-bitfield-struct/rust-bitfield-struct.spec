%global source0_hash 3ca6739863c590881f038d033a146c51ddae239186a4327014839fd864f44ed5
%bcond check 0
%global debug_package %{nil}
%global crate bitfield-struct
Name:           rust-bitfield-struct
Version:        0.13.0
Release:        1%{?dist}
Summary:        Struct-like procedural macro for bitfields
License:        MIT
URL:            https://crates.io/crates/bitfield-struct
Source0:        https://static.crates.io/crates/bitfield-struct/bitfield-struct-%{version}.crate
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
Summary:        Struct-like procedural macro for bitfields
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
%files -n rust-bitfield-struct-devel -f %{oreon_filedir}/rust-bitfield-struct-devel.list

%changelog

%autochangelog
