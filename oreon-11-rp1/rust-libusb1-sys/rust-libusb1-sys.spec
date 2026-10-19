%global source0_hash da050ade7ac4ff1ba5379af847a10a10a8e284181e060105bf8d86960ce9ce0f
%bcond check 0
%global debug_package %{nil}
%global crate libusb1-sys
Name:           rust-libusb1-sys
Version:        0.7.0
Release:        1%{?dist}
Summary:        FFI bindings for libusb
License:        MIT
URL:            https://crates.io/crates/libusb1-sys
Source0:        https://static.crates.io/crates/libusb1-sys/libusb1-sys-%{version}.crate
Patch:          libusb1-sys-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libusb-1.0)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings for libusb
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r libusb
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
%files -n rust-libusb1-sys-devel -f %{oreon_filedir}/rust-libusb1-sys-devel.list

%changelog

%autochangelog
