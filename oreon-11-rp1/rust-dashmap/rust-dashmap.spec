%global source0_hash e6361d5c062261c78a176addb82d4c821ae42bed6089de0e12603cd25de2059c
%bcond check 0
%global debug_package %{nil}
%global crate dashmap
Name:           rust-dashmap
Version:        6.2.1
Release:        1%{?dist}
Summary:        Blazing fast concurrent HashMap for Rust.
License:        MIT
URL:            https://crates.io/crates/dashmap
Source0:        https://static.crates.io/crates/dashmap/dashmap-%{version}.crate
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

%package     -n %{name}+arbitrary-devel
Summary:        Blazing fast concurrent HashMap for Rust.
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+inline-devel
Summary:        Blazing fast concurrent HashMap for Rust.
BuildArch:      noarch
%description -n %{name}+inline-devel

This package contains library source intended for building other packages which
use the "inline" feature of the "%{crate}" crate.

%package     -n %{name}+raw-api-devel
Summary:        Blazing fast concurrent HashMap for Rust.
BuildArch:      noarch
%description -n %{name}+raw-api-devel

This package contains library source intended for building other packages which
use the "raw-api" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Blazing fast concurrent HashMap for Rust.
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Blazing fast concurrent HashMap for Rust.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+typesize-devel
Summary:        Blazing fast concurrent HashMap for Rust.
BuildArch:      noarch
%description -n %{name}+typesize-devel

This package contains library source intended for building other packages which
use the "typesize" feature of the "%{crate}" crate.

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
%files -n rust-dashmap-devel -f %{oreon_filedir}/rust-dashmap-devel.list

%changelog

%autochangelog
