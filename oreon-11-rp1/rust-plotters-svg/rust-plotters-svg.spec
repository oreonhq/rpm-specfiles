%global source0_hash 51bae2ac328883f7acdfea3d66a7c35751187f870bc81f94563733a154d7a670
%bcond check 1
%global debug_package %{nil}
%global crate plotters-svg
Name:           rust-plotters-svg
Version:        0.3.7
Release:        1%{?dist}
Summary:        Plotters SVG backend
License:        MIT
URL:            https://crates.io/crates/plotters-svg
Source0:        https://static.crates.io/crates/plotters-svg/plotters-svg-%{version}.crate
Patch0:         0001-smoke-tests-without-plotters.patch
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
Summary:        Plotters SVG backend
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitmap_encoder-devel
Summary:        Plotters SVG backend
BuildArch:      noarch
%description -n %{name}+bitmap_encoder-devel

This package contains library source intended for building other packages which
use the "bitmap_encoder" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Plotters SVG backend
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

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
%files -n rust-plotters-svg-devel -f %{oreon_filedir}/rust-plotters-svg-devel.list

%changelog

%autochangelog
