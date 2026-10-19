%global source0_hash 1f9f08af0c877571712e2e3e686ad79efad9657dbf0f7c3c8ba943ff6c38932d
%bcond check 0
%global debug_package %{nil}
%global crate packed_simd
Name:           rust-packed_simd
Version:        0.3.9
Release:        1%{?dist}
Summary:        Portable Packed SIMD vectors
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/packed_simd
Source0:        https://static.crates.io/crates/packed_simd/packed_simd-%{version}.crate
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
Summary:        Portable Packed SIMD vectors
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+core_arch-devel
Summary:        Portable Packed SIMD vectors
BuildArch:      noarch
%description -n %{name}+core_arch-devel

This package contains library source intended for building other packages which
use the "core_arch" feature of the "%{crate}" crate.

%package     -n %{name}+into_bits-devel
Summary:        Portable Packed SIMD vectors
BuildArch:      noarch
%description -n %{name}+into_bits-devel

This package contains library source intended for building other packages which
use the "into_bits" feature of the "%{crate}" crate.

%package     -n %{name}+libcore_neon-devel
Summary:        Portable Packed SIMD vectors
BuildArch:      noarch
%description -n %{name}+libcore_neon-devel

This package contains library source intended for building other packages which
use the "libcore_neon" feature of the "%{crate}" crate.

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
%files -n rust-packed_simd-devel -f %{oreon_filedir}/rust-packed_simd-devel.list

%changelog

%autochangelog
