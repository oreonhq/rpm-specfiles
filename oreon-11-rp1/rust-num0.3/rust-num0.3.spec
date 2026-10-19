%global source0_hash 8b7a8e9be5e039e2ff869df49155f1c06bd01ade2117ec783e56ab0932b67a8f
%bcond check 0
%global debug_package %{nil}
%global crate num
Name:           rust-num0.3
Version:        0.3.1
Release:        1%{?dist}
Summary:        Collection of numeric types and traits for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num
Source0:        https://static.crates.io/crates/num/num-%{version}.crate
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
Summary:        Collection of numeric types and traits for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Collection of numeric types and traits for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Collection of numeric types and traits for Rust
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Collection of numeric types and traits for Rust
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Collection of numeric types and traits for Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Collection of numeric types and traits for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Collection of numeric types and traits for Rust
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
%files -n rust-num0.3-devel -f %{oreon_filedir}/rust-num0.3-devel.list

%changelog

%autochangelog
