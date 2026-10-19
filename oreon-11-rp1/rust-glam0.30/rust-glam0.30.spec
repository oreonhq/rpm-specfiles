%global source0_hash 19fc433e8437a212d1b6f1e68c7824af3aed907da60afa994e7f542d18d12aa9
%bcond check 0
%global debug_package %{nil}
%global crate glam
Name:           rust-glam0.30
Version:        0.30.10
Release:        1%{?dist}
Summary:        A simple and fast 3D math library for games and graphics
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/glam
Source0:        https://static.crates.io/crates/glam/glam-%{version}.crate
# oreon:deps
BuildRequires:  cargo-rpm-macros
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

%package     -n %{name}+approx-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+approx-devel

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+core-simd-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+core-simd-devel

This package contains library source intended for building other packages which
use the "core-simd" feature of the "%{crate}" crate.

%package     -n %{name}+cuda-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+cuda-devel

This package contains library source intended for building other packages which
use the "cuda" feature of the "%{crate}" crate.

%package     -n %{name}+debug-glam-assert-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+debug-glam-assert-devel

This package contains library source intended for building other packages which
use the "debug-glam-assert" feature of the "%{crate}" crate.

%package     -n %{name}+encase-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+encase-devel

This package contains library source intended for building other packages which
use the "encase" feature of the "%{crate}" crate.

%package     -n %{name}+fast-math-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+fast-math-devel

This package contains library source intended for building other packages which
use the "fast-math" feature of the "%{crate}" crate.

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

%package     -n %{name}+nostd-libm-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+nostd-libm-devel

This package contains library source intended for building other packages which
use the "nostd-libm" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

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

%package     -n %{name}+speedy-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+speedy-devel

This package contains library source intended for building other packages which
use the "speedy" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-devel
Summary:        A simple and fast 3D math library for games and graphics
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

%files -f %{oreon_filedir}/main.list
%files -n rust-glam0.30-devel -f %{oreon_filedir}/rust-glam0.30-devel.list
