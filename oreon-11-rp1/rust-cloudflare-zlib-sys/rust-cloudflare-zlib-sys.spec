%global source0_hash d11ad9b1a14235a8ce48c2622c57fde45c3f8e7d29344775583a847d245360be
%bcond check 0
%global debug_package %{nil}
%global crate cloudflare-zlib-sys
Name:           rust-cloudflare-zlib-sys
Version:        0.3.7
Release:        1%{?dist}
Summary:        Cloudflare fork of zlib with performance improvements
License:        Zlib
URL:            https://crates.io/crates/cloudflare-zlib-sys
Source0:        https://static.crates.io/crates/cloudflare-zlib-sys/cloudflare-zlib-sys-%{version}.crate
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

%package     -n %{name}+asm-devel
Summary:        Cloudflare fork of zlib with performance improvements
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

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
%files -n rust-cloudflare-zlib-sys-devel -f %{oreon_filedir}/rust-cloudflare-zlib-sys-devel.list

%changelog

%autochangelog
