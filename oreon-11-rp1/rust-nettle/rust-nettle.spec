%global source0_hash 2578a3627c28fefb60f1680e20e85f38bd8c8bf98c288b370489a573b0640907
%bcond check 0
%global debug_package %{nil}
%global crate nettle
Name:           rust-nettle
Version:        7.5.0
Release:        1%{?dist}
Summary:        Rust bindings for the Nettle cryptographic library
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://crates.io/crates/nettle
Source0:        https://static.crates.io/crates/nettle/nettle-%{version}.crate
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
Summary:        Rust bindings for the Nettle cryptographic library
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
%files -n rust-nettle-devel -f %{oreon_filedir}/rust-nettle-devel.list

%changelog

%autochangelog
