%global source0_hash 328c4789d42200f1eeec05bd86c9c13c7f091d2ba9a6ea35acdf51f31bc0f043
%bcond check 1
%global debug_package %{nil}
%global crate libdbus-sys
Name:           rust-libdbus-sys
Version:        0.2.7
Release:        1%{?dist}
Summary:        FFI bindings to libdbus
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/libdbus-sys
Source0:        https://static.crates.io/crates/libdbus-sys/libdbus-sys-%{version}.crate
Patch:          libdbus-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(dbus-1) >= 1.6
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libdbus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        FFI bindings to libdbus
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r vendor/
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
%files -n rust-libdbus-sys-devel -f %{oreon_filedir}/rust-libdbus-sys-devel.list

%changelog

%autochangelog
