%global source2_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash e9b78b910beafa1aae5c59bf00877c6cece1c5db28a1241ad801e86cecdff4ad
%bcond check 1
%global debug_package %{nil}
%global crate unic-ucd-common
Name:           rust-unic-ucd-common
Version:        0.9.0
Release:        1%{?dist}
Summary:        UNIC — Unicode Character Database — Common Properties
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-ucd-common
Source0:        https://static.crates.io/crates/unic-ucd-common/unic-ucd-common-%{version}.crate
Source1:        https://github.com/open-i18n/rust-unic/raw/v0.9.0/LICENSE-APACHE
Source2:        https://github.com/open-i18n/rust-unic/raw/v0.9.0/LICENSE-MIT
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
Summary:        UNIC — Unicode Character Database — Common Properties
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
%files -n rust-unic-ucd-common-devel -f %{oreon_filedir}/rust-unic-ucd-common-devel.list

%changelog

%autochangelog
