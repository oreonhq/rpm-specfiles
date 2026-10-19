%global source0_hash adc43a60c217b0c6ff46e47f26911015ad8d2e5a8be1af668c67e370d99a4346
%bcond check 0
%global debug_package %{nil}
%global crate nalgebra
Name:           rust-nalgebra0.35
Version:        0.35.0
Release:        1%{?dist}
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
License:        Apache-2.0
URL:            https://crates.io/crates/nalgebra
Source0:        https://static.crates.io/crates/nalgebra/nalgebra-%{version}.crate
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
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alga-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+alga-devel

This package contains library source intended for building other packages which
use the "alga" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+compare-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+compare-devel

This package contains library source intended for building other packages which
use the "compare" feature of the "%{crate}" crate.

%package     -n %{name}+convert-bytemuck-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+convert-bytemuck-devel

This package contains library source intended for building other packages which
use the "convert-bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+convert-glam030-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+convert-glam030-devel

This package contains library source intended for building other packages which
use the "convert-glam030" feature of the "%{crate}" crate.

%package     -n %{name}+convert-glam031-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+convert-glam031-devel

This package contains library source intended for building other packages which
use the "convert-glam031" feature of the "%{crate}" crate.

%package     -n %{name}+convert-glam032-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+convert-glam032-devel

This package contains library source intended for building other packages which
use the "convert-glam032" feature of the "%{crate}" crate.

%package     -n %{name}+convert-glam033-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+convert-glam033-devel

This package contains library source intended for building other packages which
use the "convert-glam033" feature of the "%{crate}" crate.

%package     -n %{name}+convert-mint-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+convert-mint-devel

This package contains library source intended for building other packages which
use the "convert-mint" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

%package     -n %{name}+encase-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+encase-devel

This package contains library source intended for building other packages which
use the "encase" feature of the "%{crate}" crate.

%package     -n %{name}+glam030-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+glam030-devel

This package contains library source intended for building other packages which
use the "glam030" feature of the "%{crate}" crate.

%package     -n %{name}+glam031-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+glam031-devel

This package contains library source intended for building other packages which
use the "glam031" feature of the "%{crate}" crate.

%package     -n %{name}+glam032-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+glam032-devel

This package contains library source intended for building other packages which
use the "glam032" feature of the "%{crate}" crate.

%package     -n %{name}+glam033-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+glam033-devel

This package contains library source intended for building other packages which
use the "glam033" feature of the "%{crate}" crate.

%package     -n %{name}+io-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+io-devel

This package contains library source intended for building other packages which
use the "io" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+libm-force-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+libm-force-devel

This package contains library source intended for building other packages which
use the "libm-force" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+matrixcompare-core-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+matrixcompare-core-devel

This package contains library source intended for building other packages which
use the "matrixcompare-core" feature of the "%{crate}" crate.

%package     -n %{name}+matrixmultiply-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+matrixmultiply-devel

This package contains library source intended for building other packages which
use the "matrixmultiply" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+nalgebra-macros-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+nalgebra-macros-devel

This package contains library source intended for building other packages which
use the "nalgebra-macros" feature of the "%{crate}" crate.

%package     -n %{name}+pest-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+pest-devel

This package contains library source intended for building other packages which
use the "pest" feature of the "%{crate}" crate.

%package     -n %{name}+pest_derive-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+pest_derive-devel

This package contains library source intended for building other packages which
use the "pest_derive" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-support-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+proptest-support-devel

This package contains library source intended for building other packages which
use the "proptest-support" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rand-no-std-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rand-no-std-devel

This package contains library source intended for building other packages which
use the "rand-no-std" feature of the "%{crate}" crate.

%package     -n %{name}+rand-package-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rand-package-devel

This package contains library source intended for building other packages which
use the "rand-package" feature of the "%{crate}" crate.

%package     -n %{name}+rand_distr-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rand_distr-devel

This package contains library source intended for building other packages which
use the "rand_distr" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-safe-deser-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rkyv-safe-deser-devel

This package contains library source intended for building other packages which
use the "rkyv-safe-deser" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-serialize-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rkyv-serialize-devel

This package contains library source intended for building other packages which
use the "rkyv-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-serialize-no-std-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+rkyv-serialize-no-std-devel

This package contains library source intended for building other packages which
use the "rkyv-serialize-no-std" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-serialize-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+serde-serialize-devel

This package contains library source intended for building other packages which
use the "serde-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+serde-serialize-no-std-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+serde-serialize-no-std-devel

This package contains library source intended for building other packages which
use the "serde-serialize-no-std" feature of the "%{crate}" crate.

%package     -n %{name}+slow-tests-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+slow-tests-devel

This package contains library source intended for building other packages which
use the "slow-tests" feature of the "%{crate}" crate.

%package     -n %{name}+sparse-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
BuildArch:      noarch
%description -n %{name}+sparse-devel

This package contains library source intended for building other packages which
use the "sparse" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices
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
%files -n rust-nalgebra0.35-devel -f %{oreon_filedir}/rust-nalgebra0.35-devel.list

%changelog

%autochangelog
