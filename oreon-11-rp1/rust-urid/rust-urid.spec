%global source0_hash 6828b5d766e783093935fb2f23f26ffb28b7cb9313921cec67db8ca09f38a6a4
%bcond check 0
%global debug_package %{nil}
%global crate urid
Name:           rust-urid
Version:        0.1.0
Release:        1%{?dist}
Summary:        Library for idiomatic URID support
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/urid
Source0:        https://static.crates.io/crates/urid/urid-%{version}.crate
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
Summary:        Library for idiomatic URID support
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
%files -n rust-urid-devel -f %{oreon_filedir}/rust-urid-devel.list

%changelog

%autochangelog
