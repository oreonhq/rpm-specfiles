%global source2_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash e4ed5d26be57f84f176157270c112ef57b86debac9cd21daaabbe56db0f88f23
%bcond check 0
%global debug_package %{nil}
%global crate unic-segment
Name:           rust-unic-segment
Version:        0.9.0
Release:        1%{?dist}
Summary:        UNIC — Unicode Text Segmentation Algorithms
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-segment
Source0:        https://static.crates.io/crates/unic-segment/unic-segment-%{version}.crate
Source1:        https://github.com/open-i18n/rust-unic/raw/v0.9.0/LICENSE-APACHE
Source2:        https://github.com/open-i18n/rust-unic/raw/v0.9.0/LICENSE-MIT
Patch:          unic-segment-fix-metadata.diff
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
Summary:        UNIC — Unicode Text Segmentation Algorithms
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
%files -n rust-unic-segment-devel -f %{oreon_filedir}/rust-unic-segment-devel.list

%changelog

%autochangelog
