%global source0_hash 3e61e67053d25a4e82c844e8424039d9745781b3fc4f32b8d55ed50f5f667ef3
%bcond check 1
%global debug_package %{nil}
%global crate tinyvec
Name:           rust-tinyvec
Version:        1.11.0
Release:        2%{?dist}
Summary:        Tinyvec provides 100% safe vec-like data structures
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/tinyvec
Source0:        https://static.crates.io/crates/tinyvec/tinyvec-%{version}.crate
Patch:          tinyvec-fix-metadata.diff
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
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+experimental_write_impl-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+experimental_write_impl-devel

This package contains library source intended for building other packages which
use the "experimental_write_impl" feature of the "%{crate}" crate.

%package     -n %{name}+grab_spare_slice-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+grab_spare_slice-devel

This package contains library source intended for building other packages which
use the "grab_spare_slice" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_slice_partition_dedup-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+nightly_slice_partition_dedup-devel

This package contains library source intended for building other packages which
use the "nightly_slice_partition_dedup" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_40-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+rustc_1_40-devel

This package contains library source intended for building other packages which
use the "rustc_1_40" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_55-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+rustc_1_55-devel

This package contains library source intended for building other packages which
use the "rustc_1_55" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_57-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+rustc_1_57-devel

This package contains library source intended for building other packages which
use the "rustc_1_57" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_61-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+rustc_1_61-devel

This package contains library source intended for building other packages which
use the "rustc_1_61" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tinyvec_macros-devel
Summary:        Tinyvec provides 100% safe vec-like data structures
BuildArch:      noarch
%description -n %{name}+tinyvec_macros-devel

This package contains library source intended for building other packages which
use the "tinyvec_macros" feature of the "%{crate}" crate.

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
%files -n rust-tinyvec-devel -f %{oreon_filedir}/rust-tinyvec-devel.list

%changelog

%autochangelog
