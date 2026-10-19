%global source0_hash 73ab332fe2f6680068f3582b16a24f90ad7096d5d39b974d1c0aff0125116f02
%bcond check 0
%global debug_package %{nil}
%global crate zune-inflate
Name:           rust-zune-inflate
Version:        0.2.54
Release:        1%{?dist}
Summary:        A heavily optimized deflate decompressor in Pure Rust
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/zune-inflate
Source0:        https://static.crates.io/crates/zune-inflate/zune-inflate-%{version}.crate
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
Summary:        A heavily optimized deflate decompressor in Pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        A heavily optimized deflate decompressor in Pure Rust
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+simd-adler32-devel
Summary:        A heavily optimized deflate decompressor in Pure Rust
BuildArch:      noarch
%description -n %{name}+simd-adler32-devel

This package contains library source intended for building other packages which
use the "simd-adler32" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A heavily optimized deflate decompressor in Pure Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        A heavily optimized deflate decompressor in Pure Rust
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

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
%files -n rust-zune-inflate-devel -f %{oreon_filedir}/rust-zune-inflate-devel.list

%changelog

%autochangelog
