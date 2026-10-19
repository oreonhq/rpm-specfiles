%global source0_hash 525e9ff3e1a4be2fbea1fdf0e98686a6d98b4d8f937e1bf7402245af1909e8c3
%bcond check 0
%global debug_package %{nil}
%global crate image-webp
Name:           rust-image-webp
Version:        0.2.4
Release:        1%{?dist}
Summary:        WebP encoding and decoding in pure Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/image-webp
Source0:        https://static.crates.io/crates/image-webp/image-webp-%{version}.crate
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

%package     -n %{name}+_benchmarks-devel
Summary:        WebP encoding and decoding in pure Rust
BuildArch:      noarch
%description -n %{name}+_benchmarks-devel

This package contains library source intended for building other packages which
use the "_benchmarks" feature of the "%{crate}" crate.

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
%files -n rust-image-webp-devel -f %{oreon_filedir}/rust-image-webp-devel.list

%changelog

%autochangelog
