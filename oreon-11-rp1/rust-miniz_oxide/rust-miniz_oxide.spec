%global source0_hash b63fbc4a50860e98e7b2aa7804ded1db5cbc3aff9193adaff57a6931bf7c4b4c
%bcond check 1
%global debug_package %{nil}
%global crate miniz_oxide
Name:           rust-miniz_oxide
Version:        0.9.1
Release:        2%{?dist}
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
License:        MIT OR Zlib OR Apache-2.0
URL:            https://crates.io/crates/miniz_oxide
Source0:        https://static.crates.io/crates/miniz_oxide/miniz_oxide-%{version}.crate
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
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+block-boundary-devel
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+block-boundary-devel

This package contains library source intended for building other packages which
use the "block-boundary" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+simd-adler32-devel
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+simd-adler32-devel

This package contains library source intended for building other packages which
use the "simd-adler32" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+with-alloc-devel
Summary:        DEFLATE compression and decompression library rewritten in Rust based on miniz
BuildArch:      noarch
%description -n %{name}+with-alloc-devel

This package contains library source intended for building other packages which
use the "with-alloc" feature of the "%{crate}" crate.

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
%files -n rust-miniz_oxide-devel -f %{oreon_filedir}/rust-miniz_oxide-devel.list

%changelog

%autochangelog
