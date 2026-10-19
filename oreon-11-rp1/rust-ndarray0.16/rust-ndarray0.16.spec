%global source0_hash 882ed72dce9365842bf196bdeedf5055305f11fc8c03dee7bb0194a6cad34841
%bcond check 1
%global debug_package %{nil}
%global crate ndarray
Name:           rust-ndarray0.16
Version:        0.16.1
Release:        1%{?dist}
Summary:        N-dimensional array for general elements and for numerics
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ndarray
Source0:        https://static.crates.io/crates/ndarray/ndarray-%{version}.crate
Patch:          ndarray-fix-metadata-auto.diff
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
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+approx-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+approx-devel

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%package     -n %{name}+blas-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+blas-devel

This package contains library source intended for building other packages which
use the "blas" feature of the "%{crate}" crate.

%package     -n %{name}+docs-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+docs-devel

This package contains library source intended for building other packages which
use the "docs" feature of the "%{crate}" crate.

%package     -n %{name}+matrixmultiply-threading-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+matrixmultiply-threading-devel

This package contains library source intended for building other packages which
use the "matrixmultiply-threading" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-critical-section-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+portable-atomic-critical-section-devel

This package contains library source intended for building other packages which
use the "portable-atomic-critical-section" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-1-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+serde-1-devel

This package contains library source intended for building other packages which
use the "serde-1" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        N-dimensional array for general elements and for numerics
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

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
%files -n rust-ndarray0.16-devel -f %{oreon_filedir}/rust-ndarray0.16-devel.list

%changelog

%autochangelog
