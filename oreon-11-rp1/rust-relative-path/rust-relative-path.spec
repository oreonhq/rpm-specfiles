%global source11_hash 6485b8ed310d3f0340bf1ad1f47645069ce4069dcc6bb46c7d5c6faf41de1fdb
%global source10_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash ba39f3699c378cd8970968dcbff9c43159ea4cfbd88d43c00b22f2ef10a435d2
%bcond check 0
%global debug_package %{nil}
%global crate relative-path
Name:           rust-relative-path
Version:        1.9.3
Release:        1%{?dist}
Summary:        Portable, relative paths for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/relative-path
Source0:        https://static.crates.io/crates/relative-path/relative-path-%{version}.crate
Source10:       https://github.com/udoprog/relative-path/raw/refs/tags/%{version}/LICENSE-APACHE
Source11:       https://github.com/udoprog/relative-path/raw/refs/tags/%{version}/LICENSE-MIT
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
Summary:        Portable, relative paths for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Portable, relative paths for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' '%{SOURCE11}' .
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-relative-path-devel -f %{oreon_filedir}/rust-relative-path-devel.list

%changelog

%autochangelog
