%global source0_hash 891d15931895091dea5c47afa5b3c9a01ba634b311919fd4d41388fa0e3d76af
%bcond check 0
%global debug_package %{nil}
%global crate hybrid-array
Name:           rust-hybrid-array0.3
Version:        0.3.1
Release:        1%{?dist}
Summary:        Hybrid typenum-based and const generic array types designed to provid...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hybrid-array
Source0:        https://static.crates.io/crates/hybrid-array/hybrid-array-%{version}.crate
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

%package     -n %{name}+bytemuck-devel
Summary:        Hybrid typenum-based and const generic array types designed to provid...
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+extra-sizes-devel
Summary:        Hybrid typenum-based and const generic array types designed to provid...
BuildArch:      noarch
%description -n %{name}+extra-sizes-devel

This package contains library source intended for building other packages which
use the "extra-sizes" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hybrid typenum-based and const generic array types designed to provid...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+subtle-devel
Summary:        Hybrid typenum-based and const generic array types designed to provid...
BuildArch:      noarch
%description -n %{name}+subtle-devel

This package contains library source intended for building other packages which
use the "subtle" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Hybrid typenum-based and const generic array types designed to provid...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-hybrid-array0.3-devel -f %{oreon_filedir}/rust-hybrid-array0.3-devel.list

%changelog

%autochangelog
