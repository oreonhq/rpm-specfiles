%global source0_hash 366ffbaa4442f4684d91e2cd7c5ea7c4ed8add41959a31447066e279e432b618
%bcond check 1
%global debug_package %{nil}
%global crate ab_glyph_rasterizer
Name:           rust-ab_glyph_rasterizer
Version:        0.1.10
Release:        1%{?dist}
Summary:        Coverage rasterization for lines, quadratic & cubic beziers
License:        Apache-2.0
URL:            https://crates.io/crates/ab_glyph_rasterizer
Source0:        https://static.crates.io/crates/ab_glyph_rasterizer/ab_glyph_rasterizer-%{version}.crate
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
Summary:        Coverage rasterization for lines, quadratic & cubic beziers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Coverage rasterization for lines, quadratic & cubic beziers
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Coverage rasterization for lines, quadratic & cubic beziers
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
%files -n rust-ab_glyph_rasterizer-devel -f %{oreon_filedir}/rust-ab_glyph_rasterizer-devel.list

%changelog

%autochangelog
