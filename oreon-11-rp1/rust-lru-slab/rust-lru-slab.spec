%global source0_hash 4050469837a6ff301cd14c1f8f24f88549e6d548f24f64e2148eb0f72cebc51f
%bcond check 1
%global debug_package %{nil}
%global crate lru-slab
Name:           rust-lru-slab
Version:        0.1.3
Release:        1%{?dist}
Summary:        Pre-allocated storage with constant-time LRU tracking
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/lru-slab
Source0:        https://static.crates.io/crates/lru-slab/lru-slab-%{version}.crate
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
Summary:        Pre-allocated storage with constant-time LRU tracking
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-lru-slab-devel -f %{oreon_filedir}/rust-lru-slab-devel.list

%changelog

%autochangelog
