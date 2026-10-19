%global source0_hash 1d674e81391d1e1ab681a28d99df07927c6d4aa5b027d7da16ba32d1d21ecd99
%bcond check 0
%global debug_package %{nil}
%global crate fixedbitset
Name:           rust-fixedbitset
Version:        0.5.7
Release:        1%{?dist}
Summary:        FixedBitSet is a simple bitset collection
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fixedbitset
Source0:        https://static.crates.io/crates/fixedbitset/fixedbitset-%{version}.crate
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
Summary:        FixedBitSet is a simple bitset collection
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        FixedBitSet is a simple bitset collection
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        FixedBitSet is a simple bitset collection
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
%files -n rust-fixedbitset-devel -f %{oreon_filedir}/rust-fixedbitset-devel.list

%changelog

%autochangelog
