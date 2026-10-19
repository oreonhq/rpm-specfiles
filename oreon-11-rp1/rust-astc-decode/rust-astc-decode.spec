%global source0_hash 2d6058e6202e20b7fa445692ec4b77ca8eb02508091fcd479ea753d9f60e376b
%bcond check 0
%global debug_package %{nil}
%global crate astc-decode
Name:           rust-astc-decode
Version:        0.3.1
Release:        1%{?dist}
Summary:        Software ASTC decoder in rust
License:        Apache-2.0
URL:            https://crates.io/crates/astc-decode
Source0:        https://static.crates.io/crates/astc-decode/astc-decode-%{version}.crate
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
Summary:        Software ASTC decoder in rust
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
%files -n rust-astc-decode-devel -f %{oreon_filedir}/rust-astc-decode-devel.list

%changelog

%autochangelog
