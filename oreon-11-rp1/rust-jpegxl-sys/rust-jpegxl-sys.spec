%global source0_hash d07cb5b362c69ced9ebfcdb3301dc6cadf7d186a3e6a3d8f4fcb9094a83ab408
%bcond check 0
%global debug_package %{nil}
%global crate jpegxl-sys
%global crate_version 0.12.0+libjxl-0.11.1
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-jpegxl-sys
Version:        0.12.0
Release:        1%{?dist}
Summary:        Rust wrapper for JPEG XL reference implementation
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/jpegxl-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          jpegxl-sys-fix-metadata-auto.diff
Patch:          jpegxl-sys-fix-metadata.diff
Patch:          0001-unconditionally-use-pkg-config-to-find-libjxl.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libjxl)
Requires:       pkgconfig(libjxl_threads)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-jpegxl-sys-devel -f %{oreon_filedir}/rust-jpegxl-sys-devel.list

%changelog

%autochangelog
