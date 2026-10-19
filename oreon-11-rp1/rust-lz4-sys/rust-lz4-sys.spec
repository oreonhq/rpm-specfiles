%global source0_hash 6bd8c0d6c6ed0cd30b3652886bb8711dc4bb01d637a68105a3d5158039b418e6
%bcond check 1
%global debug_package %{nil}
%global crate lz4-sys
%global crate_version 1.11.1+lz4-1.10.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-lz4-sys
Version:        1.11.1
Release:        1%{?dist}
Summary:        Rust LZ4 sys package
License:        MIT
URL:            https://crates.io/crates/lz4-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          lz4-sys-fix-metadata-auto.diff
Patch:          lz4-sys-fix-metadata.diff
Patch10:        lz4-sys-1.11.0-system-liblz4.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(liblz4)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust LZ4 sys package
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
rm -rv liblz4
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
%files -n rust-lz4-sys-devel -f %{oreon_filedir}/rust-lz4-sys-devel.list

%changelog

%autochangelog
