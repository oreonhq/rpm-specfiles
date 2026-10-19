%global source0_hash 9b7d16fe73fb6d2e16b986392b716409c6ae6fabd35769d66bea391b016cdbc9
%bcond check 0
%global debug_package %{nil}
%global crate jpegxl-rs
%global crate_version 0.14.0+libjxl-0.11.2
Name:           rust-jpegxl-rs0.14
Version:        0.14.0
Release:        1%{?dist}
Summary:        Safe Rust wrapper for JPEG XL reference implementation
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/jpegxl-rs
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          jpegxl-rs-fix-metadata-auto.diff
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
Summary:        Safe Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        Safe Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        Safe Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Safe Rust wrapper for JPEG XL reference implementation
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        Safe Rust wrapper for JPEG XL reference implementation
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
%files -n rust-jpegxl-rs0.14-devel -f %{oreon_filedir}/rust-jpegxl-rs0.14-devel.list

%changelog

%autochangelog
