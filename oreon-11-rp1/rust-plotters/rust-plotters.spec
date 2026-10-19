%global source0_hash 5aeb6f403d7a4911efb1e33402027fc44f29b5bf6def3effcc22d7bb75f2b747
%bcond check 0
%global debug_package %{nil}
%global crate plotters
Name:           rust-plotters
Version:        0.3.7
Release:        1%{?dist}
Summary:        A Rust drawing library focus on data plotting for both WASM and
License:        MIT
URL:            https://crates.io/crates/plotters
Source0:        https://static.crates.io/crates/plotters/plotters-%{version}.crate
Patch:          plotters-fix-metadata-auto.diff
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
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all_elements-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+all_elements-devel

This package contains library source intended for building other packages which
use the "all_elements" feature of the "%{crate}" crate.

%package     -n %{name}+all_series-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+all_series-devel

This package contains library source intended for building other packages which
use the "all_series" feature of the "%{crate}" crate.

%package     -n %{name}+area_series-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+area_series-devel

This package contains library source intended for building other packages which
use the "area_series" feature of the "%{crate}" crate.

%package     -n %{name}+bitmap_backend-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+bitmap_backend-devel

This package contains library source intended for building other packages which
use the "bitmap_backend" feature of the "%{crate}" crate.

%package     -n %{name}+bitmap_encoder-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+bitmap_encoder-devel

This package contains library source intended for building other packages which
use the "bitmap_encoder" feature of the "%{crate}" crate.

%package     -n %{name}+bitmap_gif-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+bitmap_gif-devel

This package contains library source intended for building other packages which
use the "bitmap_gif" feature of the "%{crate}" crate.

%package     -n %{name}+boxplot-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+boxplot-devel

This package contains library source intended for building other packages which
use the "boxplot" feature of the "%{crate}" crate.

%package     -n %{name}+candlestick-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+candlestick-devel

This package contains library source intended for building other packages which
use the "candlestick" feature of the "%{crate}" crate.

%package     -n %{name}+colormaps-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+colormaps-devel

This package contains library source intended for building other packages which
use the "colormaps" feature of the "%{crate}" crate.

%package     -n %{name}+datetime-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+datetime-devel

This package contains library source intended for building other packages which
use the "datetime" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated_items-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+deprecated_items-devel

This package contains library source intended for building other packages which
use the "deprecated_items" feature of the "%{crate}" crate.

%package     -n %{name}+errorbar-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+errorbar-devel

This package contains library source intended for building other packages which
use the "errorbar" feature of the "%{crate}" crate.

%package     -n %{name}+evcxr-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+evcxr-devel

This package contains library source intended for building other packages which
use the "evcxr" feature of the "%{crate}" crate.

%package     -n %{name}+evcxr_bitmap-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+evcxr_bitmap-devel

This package contains library source intended for building other packages which
use the "evcxr_bitmap" feature of the "%{crate}" crate.

%package     -n %{name}+full_palette-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+full_palette-devel

This package contains library source intended for building other packages which
use the "full_palette" feature of the "%{crate}" crate.

%package     -n %{name}+histogram-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+histogram-devel

This package contains library source intended for building other packages which
use the "histogram" feature of the "%{crate}" crate.

%package     -n %{name}+line_series-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+line_series-devel

This package contains library source intended for building other packages which
use the "line_series" feature of the "%{crate}" crate.

%package     -n %{name}+point_series-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+point_series-devel

This package contains library source intended for building other packages which
use the "point_series" feature of the "%{crate}" crate.

%package     -n %{name}+surface_series-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+surface_series-devel

This package contains library source intended for building other packages which
use the "surface_series" feature of the "%{crate}" crate.

%package     -n %{name}+svg_backend-devel
Summary:        A Rust drawing library focus on data plotting for both WASM and
BuildArch:      noarch
%description -n %{name}+svg_backend-devel

This package contains library source intended for building other packages which
use the "svg_backend" feature of the "%{crate}" crate.

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
%files -n rust-plotters-devel -f %{oreon_filedir}/rust-plotters-devel.list

%changelog

%autochangelog
