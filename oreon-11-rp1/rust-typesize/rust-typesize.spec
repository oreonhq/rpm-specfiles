%global source0_hash a313188364f7e10138257cb288c64e9b0e282510abefc91c796799559fa14762
%bcond check 0
%global debug_package %{nil}
%global crate typesize
Name:           rust-typesize
Version:        0.1.15
Release:        1%{?dist}
Summary:        A library to fetch an accurate estimate of the total memory usage of...
License:        MIT
URL:            https://crates.io/crates/typesize
Source0:        https://static.crates.io/crates/typesize/typesize-%{version}.crate
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
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+bitvec-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+bitvec-devel

This package contains library source intended for building other packages which
use the "bitvec" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+details-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+details-devel

This package contains library source intended for building other packages which
use the "details" feature of the "%{crate}" crate.

%package     -n %{name}+extract_map-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+extract_map-devel

This package contains library source intended for building other packages which
use the "extract_map" feature of the "%{crate}" crate.

%package     -n %{name}+extract_map_01-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+extract_map_01-devel

This package contains library source intended for building other packages which
use the "extract_map_01" feature of the "%{crate}" crate.

%package     -n %{name}+halfbrown-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+halfbrown-devel

This package contains library source intended for building other packages which
use the "halfbrown" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown_14-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+hashbrown_14-devel

This package contains library source intended for building other packages which
use the "hashbrown_14" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown_15-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+hashbrown_15-devel

This package contains library source intended for building other packages which
use the "hashbrown_15" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+jiff-devel

This package contains library source intended for building other packages which
use the "jiff" feature of the "%{crate}" crate.

%package     -n %{name}+mini-moka-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+mini-moka-devel

This package contains library source intended for building other packages which
use the "mini-moka" feature of the "%{crate}" crate.

%package     -n %{name}+mini_moka-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+mini_moka-devel

This package contains library source intended for building other packages which
use the "mini_moka" feature of the "%{crate}" crate.

%package     -n %{name}+nonmax-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+nonmax-devel

This package contains library source intended for building other packages which
use the "nonmax" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+saturating_impls-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+saturating_impls-devel

This package contains library source intended for building other packages which
use the "saturating_impls" feature of the "%{crate}" crate.

%package     -n %{name}+secrecy-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+secrecy-devel

This package contains library source intended for building other packages which
use the "secrecy" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+simd-json-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+simd-json-devel

This package contains library source intended for building other packages which
use the "simd-json" feature of the "%{crate}" crate.

%package     -n %{name}+simd_json-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+simd_json-devel

This package contains library source intended for building other packages which
use the "simd_json" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+web-time-devel
Summary:        A library to fetch an accurate estimate of the total memory usage of...
BuildArch:      noarch
%description -n %{name}+web-time-devel

This package contains library source intended for building other packages which
use the "web-time" feature of the "%{crate}" crate.

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
%files -n rust-typesize-devel -f %{oreon_filedir}/rust-typesize-devel.list

%changelog

%autochangelog
