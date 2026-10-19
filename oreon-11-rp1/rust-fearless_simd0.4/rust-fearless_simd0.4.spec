%global source0_hash b97b65636e5b9ef369943878ac74335ba1c55c1cb6adbf1e2c293c624248d693
%bcond check 0
%global debug_package %{nil}
%global crate fearless_simd
Name:           rust-fearless_simd0.4
Version:        0.4.1
Release:        1%{?dist}
Summary:        Safer and easier SIMD
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/fearless_simd
Source0:        https://static.crates.io/crates/fearless_simd/fearless_simd-%{version}.crate
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
Summary:        Safer and easier SIMD
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+force_support_fallback-devel
Summary:        Safer and easier SIMD
BuildArch:      noarch
%description -n %{name}+force_support_fallback-devel

This package contains library source intended for building other packages which
use the "force_support_fallback" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Safer and easier SIMD
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+safe_wrappers-devel
Summary:        Safer and easier SIMD
BuildArch:      noarch
%description -n %{name}+safe_wrappers-devel

This package contains library source intended for building other packages which
use the "safe_wrappers" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safer and easier SIMD
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
%files -n rust-fearless_simd0.4-devel -f %{oreon_filedir}/rust-fearless_simd0.4-devel.list

%changelog

%autochangelog
