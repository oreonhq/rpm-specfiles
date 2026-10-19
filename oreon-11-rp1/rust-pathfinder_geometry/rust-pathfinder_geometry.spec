%global source2_hash 0621878e61f0d0fda054bcbe02df75192c28bde1ecc8289cbd86aeba2dd72720
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash 0b7b7e7b4ea703700ce73ebf128e1450eb69c3a8329199ffbfb9b2a0418e5ad3
%bcond check 0
%global debug_package %{nil}
%global crate pathfinder_geometry
Name:           rust-pathfinder_geometry
Version:        0.5.1
Release:        1%{?dist}
Summary:        Basic SIMD-accelerated geometry/linear algebra
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pathfinder_geometry
Source0:        https://static.crates.io/crates/pathfinder_geometry/pathfinder_geometry-%{version}.crate
Source1:        https://github.com/servo/pathfinder/raw/pathfinder_simd-v0.5.1/LICENSE-APACHE
Source2:        https://github.com/servo/pathfinder/raw/pathfinder_simd-v0.5.1/LICENSE-MIT
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
Summary:        Basic SIMD-accelerated geometry/linear algebra
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-pathfinder_geometry-devel -f %{oreon_filedir}/rust-pathfinder_geometry-devel.list

%changelog

%autochangelog
