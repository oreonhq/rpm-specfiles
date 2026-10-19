%global source0_hash f35502358aa77e598570bbf9a79ad19c4985a1bcd157b5d70197688dafca9b48
%bcond check 0
%global debug_package %{nil}
%global crate nettle-sys
Name:           rust-nettle-sys
Version:        2.3.2
Release:        1%{?dist}
Summary:        Low-level Rust bindings for the Nettle cryptographic library
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://crates.io/crates/nettle-sys
Source0:        https://static.crates.io/crates/nettle-sys/nettle-sys-%{version}.crate
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
Summary:        Low-level Rust bindings for the Nettle cryptographic library
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
%files -n rust-nettle-sys-devel -f %{oreon_filedir}/rust-nettle-sys-devel.list

%changelog

%autochangelog
