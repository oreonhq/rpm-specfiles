%global source0_hash 3abb554f8ee44336b72d522e0a7fe86a29e09f839a36022fa869a7dfe941a54b
%bcond check 0
%global debug_package %{nil}
%global crate glam
Name:           rust-glam0.15
Version:        0.15.2
Release:        1%{?dist}
Summary:        A simple and fast 3D math library for games and graphics
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/glam
Source0:        https://static.crates.io/crates/glam/glam-%{version}.crate
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
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+debug-glam-assert-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+debug-glam-assert-devel

This package contains library source intended for building other packages which
use the "debug-glam-assert" feature of the "%{crate}" crate.

%package     -n %{name}+glam-assert-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+glam-assert-devel

This package contains library source intended for building other packages which
use the "glam-assert" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+num-traits-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+num-traits-devel

This package contains library source intended for building other packages which
use the "num-traits" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+scalar-math-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+scalar-math-devel

This package contains library source intended for building other packages which
use the "scalar-math" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+spirv-std-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+spirv-std-devel

This package contains library source intended for building other packages which
use the "spirv-std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+transform-types-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+transform-types-devel

This package contains library source intended for building other packages which
use the "transform-types" feature of the "%{crate}" crate.

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
%files -n rust-glam0.15-devel -f %{oreon_filedir}/rust-glam0.15-devel.list

%changelog

%autochangelog
