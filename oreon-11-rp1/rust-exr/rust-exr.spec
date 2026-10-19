%global source0_hash 711fe42c9964295e01ee3fba3f9fe0e1d24b98886950d68efe81b1c76e21adf3
%bcond check 0
%global debug_package %{nil}
%global crate exr
Name:           rust-exr
Version:        1.74.2
Release:        1%{?dist}
Summary:        Read and write OpenEXR files without any unsafe code
License:        BSD-3-Clause
URL:            https://crates.io/crates/exr
Source0:        https://static.crates.io/crates/exr/exr-%{version}.crate
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
Summary:        Read and write OpenEXR files without any unsafe code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avx2-tests-devel
Summary:        Read and write OpenEXR files without any unsafe code
BuildArch:      noarch
%description -n %{name}+avx2-tests-devel

This package contains library source intended for building other packages which
use the "avx2-tests" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Read and write OpenEXR files without any unsafe code
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-core-devel
Summary:        Read and write OpenEXR files without any unsafe code
BuildArch:      noarch
%description -n %{name}+rayon-core-devel

This package contains library source intended for building other packages which
use the "rayon-core" feature of the "%{crate}" crate.

%package     -n %{name}+simd-benches-devel
Summary:        Read and write OpenEXR files without any unsafe code
BuildArch:      noarch
%description -n %{name}+simd-benches-devel

This package contains library source intended for building other packages which
use the "simd-benches" feature of the "%{crate}" crate.

%package     -n %{name}+sse2-tests-devel
Summary:        Read and write OpenEXR files without any unsafe code
BuildArch:      noarch
%description -n %{name}+sse2-tests-devel

This package contains library source intended for building other packages which
use the "sse2-tests" feature of the "%{crate}" crate.

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
%files -n rust-exr-devel -f %{oreon_filedir}/rust-exr-devel.list

%changelog

%autochangelog
