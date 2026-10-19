%global source0_hash f70749695b063ecbf6b62949ccccde2e733ec3ecbbd71d467dca4e5c6c97cca0
%bcond check 0
%global debug_package %{nil}
%global crate glam
Name:           rust-glam0.32
Version:        0.32.1
Release:        1%{?dist}
Summary:        Simple and fast 3D math library for games and graphics
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/glam
Source0:        https://static.crates.io/crates/glam/glam-%{version}.crate
Patch:          glam-fix-metadata-auto.diff
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
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+approx-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+approx-devel

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+core-simd-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+core-simd-devel

This package contains library source intended for building other packages which
use the "core-simd" feature of the "%{crate}" crate.

%package     -n %{name}+cuda-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+cuda-devel

This package contains library source intended for building other packages which
use the "cuda" feature of the "%{crate}" crate.

%package     -n %{name}+debug-glam-assert-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+debug-glam-assert-devel

This package contains library source intended for building other packages which
use the "debug-glam-assert" feature of the "%{crate}" crate.

%package     -n %{name}+encase-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+encase-devel

This package contains library source intended for building other packages which
use the "encase" feature of the "%{crate}" crate.

%package     -n %{name}+fast-math-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+fast-math-devel

This package contains library source intended for building other packages which
use the "fast-math" feature of the "%{crate}" crate.

%package     -n %{name}+glam-assert-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+glam-assert-devel

This package contains library source intended for building other packages which
use the "glam-assert" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+nostd-libm-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+nostd-libm-devel

This package contains library source intended for building other packages which
use the "nostd-libm" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+scalar-math-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+scalar-math-devel

This package contains library source intended for building other packages which
use the "scalar-math" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+speedy-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+speedy-devel

This package contains library source intended for building other packages which
use the "speedy" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-devel
Summary:        Simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

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
%files -n rust-glam0.32-devel -f %{oreon_filedir}/rust-glam0.32-devel.list

%changelog

%autochangelog
