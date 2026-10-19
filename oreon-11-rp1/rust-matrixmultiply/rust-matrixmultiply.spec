%global source0_hash 3f607c237553f086e7043417a51df26b2eb899d3caff94e6a67592ff992fedc7
%bcond check 0
%global debug_package %{nil}
%global crate matrixmultiply
Name:           rust-matrixmultiply
Version:        0.3.11
Release:        1%{?dist}
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/matrixmultiply
Source0:        https://static.crates.io/crates/matrixmultiply/matrixmultiply-%{version}.crate
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
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avx512-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+avx512-devel

This package contains library source intended for building other packages which
use the "avx512" feature of the "%{crate}" crate.

%package     -n %{name}+cgemm-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+cgemm-devel

This package contains library source intended for building other packages which
use the "cgemm" feature of the "%{crate}" crate.

%package     -n %{name}+constconf-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+constconf-devel

This package contains library source intended for building other packages which
use the "constconf" feature of the "%{crate}" crate.

%package     -n %{name}+num_cpus-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+num_cpus-devel

This package contains library source intended for building other packages which
use the "num_cpus" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thread-tree-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+thread-tree-devel

This package contains library source intended for building other packages which
use the "thread-tree" feature of the "%{crate}" crate.

%package     -n %{name}+threading-devel
Summary:        General matrix multiplication for f32 and f64 matrices. Operates on m...
BuildArch:      noarch
%description -n %{name}+threading-devel

This package contains library source intended for building other packages which
use the "threading" feature of the "%{crate}" crate.

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
%files -n rust-matrixmultiply-devel -f %{oreon_filedir}/rust-matrixmultiply-devel.list

%changelog

%autochangelog
