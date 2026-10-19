%global source0_hash 11031e251abf8611c80f460e19dbdeb54a66db918e49c65a7065b46ac7aec520
%bcond check 0
%global debug_package %{nil}
%global crate simd_cesu8
Name:           rust-simd_cesu8
Version:        1.2.0
Release:        1%{?dist}
Summary:        An extremely fast, SIMD accelerated, encoding and decoding library fo...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/simd_cesu8
Source0:        https://static.crates.io/crates/simd_cesu8/simd_cesu8-%{version}.crate
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
Summary:        An extremely fast, SIMD accelerated, encoding and decoding library fo...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        An extremely fast, SIMD accelerated, encoding and decoding library fo...
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        An extremely fast, SIMD accelerated, encoding and decoding library fo...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        An extremely fast, SIMD accelerated, encoding and decoding library fo...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-simd_cesu8-devel -f %{oreon_filedir}/rust-simd_cesu8-devel.list

%changelog

%autochangelog
