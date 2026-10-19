%global source0_hash 447d8234fba933a5198401c673607dd75758bab32136766da61711cc362294e9
%bcond check 1
%global debug_package %{nil}
%global crate yuv
Name:           rust-yuv
Version:        0.8.10
Release:        1%{?dist}
Summary:        High performance utilities for YUV format handling and conversion
License:        BSD-3-Clause OR Apache-2.0
URL:            https://crates.io/crates/yuv
Source0:        https://static.crates.io/crates/yuv/yuv-%{version}.crate
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
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avx-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+avx-devel

This package contains library source intended for building other packages which
use the "avx" feature of the "%{crate}" crate.

%package     -n %{name}+big_endian-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+big_endian-devel

This package contains library source intended for building other packages which
use the "big_endian" feature of the "%{crate}" crate.

%package     -n %{name}+fast_mode-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+fast_mode-devel

This package contains library source intended for building other packages which
use the "fast_mode" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_f16-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+nightly_f16-devel

This package contains library source intended for building other packages which
use the "nightly_f16" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_i8mm-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+nightly_i8mm-devel

This package contains library source intended for building other packages which
use the "nightly_i8mm" feature of the "%{crate}" crate.

%package     -n %{name}+professional_mode-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+professional_mode-devel

This package contains library source intended for building other packages which
use the "professional_mode" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rdm-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+rdm-devel

This package contains library source intended for building other packages which
use the "rdm" feature of the "%{crate}" crate.

%package     -n %{name}+rdp-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+rdp-devel

This package contains library source intended for building other packages which
use the "rdp" feature of the "%{crate}" crate.

%package     -n %{name}+sse-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+sse-devel

This package contains library source intended for building other packages which
use the "sse" feature of the "%{crate}" crate.

%package     -n %{name}+ycgco_r_type-devel
Summary:        High performance utilities for YUV format handling and conversion
BuildArch:      noarch
%description -n %{name}+ycgco_r_type-devel

This package contains library source intended for building other packages which
use the "ycgco_r_type" feature of the "%{crate}" crate.

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
%files -n rust-yuv-devel -f %{oreon_filedir}/rust-yuv-devel.list

%changelog

%autochangelog
