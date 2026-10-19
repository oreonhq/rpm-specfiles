%global source2_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source1_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source0_hash 86aed873b8202d22b13859dda5fe7c001d271412c31d411fd9b827e030569410
%bcond check 0
%global debug_package %{nil}
%global crate unic-ucd-normal
Name:           rust-unic-ucd-normal
Version:        0.9.0
Release:        1%{?dist}
Summary:        UNIC — Unicode Character Database — Normalization Properties
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-ucd-normal
Source0:        https://static.crates.io/crates/unic-ucd-normal/unic-ucd-normal-%{version}.crate
Source1:        https://raw.githubusercontent.com/open-i18n/rust-unic/v%{version}/LICENSE-MIT
Source2:        https://raw.githubusercontent.com/open-i18n/rust-unic/v%{version}/LICENSE-APACHE
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
Summary:        UNIC — Unicode Character Database — Normalization Properties
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unic-ucd-category-devel
Summary:        UNIC — Unicode Character Database — Normalization Properties
BuildArch:      noarch
%description -n %{name}+unic-ucd-category-devel

This package contains library source intended for building other packages which
use the "unic-ucd-category" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp %{SOURCE1} .
cp %{SOURCE2} .
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
%files -n rust-unic-ucd-normal-devel -f %{oreon_filedir}/rust-unic-ucd-normal-devel.list

%changelog

%autochangelog
