%global source0_hash 73f88a1307638156682bada9d7604135552957b7818057dcef22705b4d509495
%bcond check 1
%global debug_package %{nil}
%global crate num-complex
Name:           rust-num-complex
Version:        0.4.6
Release:        1%{?dist}
Summary:        Complex numbers implementation for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-complex
Source0:        https://static.crates.io/crates/num-complex/num-complex-%{version}.crate
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
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Complex numbers implementation for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Complex numbers implementation for Rust
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
%files -n rust-num-complex-devel -f %{oreon_filedir}/rust-num-complex-devel.list

%changelog

%autochangelog
