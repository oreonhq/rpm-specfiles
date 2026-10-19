%global source0_hash 00cb4f7ffb45ee4327e9ec6ca1a732f3abef470ee008f7d4be3afb414075cd7d
%bcond check 0
%global debug_package %{nil}
%global crate jpegxl-sys
%global crate_version 0.12.1+libjxl-0.11.2
Name:           rust-jpegxl-sys0.12
Version:        0.12.1
Release:        1%{?dist}
Summary:        Rust wrapper for JPEG XL reference implementation
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/jpegxl-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          jpegxl-sys-fix-metadata-auto.diff
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

%package     -n %{name}+vendored-devel
Summary:        Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

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
%files -n rust-jpegxl-sys0.12-devel -f %{oreon_filedir}/rust-jpegxl-sys0.12-devel.list

%changelog

%autochangelog
