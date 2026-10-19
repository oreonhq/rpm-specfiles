%global source0_hash 2707e3afba5e19b75d582d88bc79237418f2a2a2d673d01cf9b03633b46e98f3
%bcond check 0
%global debug_package %{nil}
%global crate crc64
Name:           rust-crc64
Version:        2.0.0
Release:        1%{?dist}
Summary:        CRC64 checksum implementation
License:        BSD-3-Clause
URL:            https://crates.io/crates/crc64
Source0:        https://static.crates.io/crates/crc64/crc64-%{version}.crate
Patch:          crc64-fix-metadata.diff
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
Summary:        CRC64 checksum implementation
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
%files -n rust-crc64-devel -f %{oreon_filedir}/rust-crc64-devel.list

%changelog

%autochangelog
