%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash e2db585e1d738fc771bf08a151420d3ed193d9d895a36df7f6f8a9456b911ddc
%bcond check 0
%global debug_package %{nil}
%global crate khronos_api
Name:           rust-khronos_api
Version:        3.1.0
Release:        1%{?dist}
Summary:        Khronos XML API Registry, exposed as byte string constants
License:        Apache-2.0 AND MIT
URL:            https://crates.io/crates/khronos_api
Source0:        https://static.crates.io/crates/khronos_api/khronos_api-%{version}.crate
Source1:        https://github.com/brendanzab/gl-rs/raw/khronos_api-v%{version}/LICENSE
Patch:          khronos_api-fix-metadata.diff
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
Summary:        Khronos XML API Registry, exposed as byte string constants
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-khronos_api-devel -f %{oreon_filedir}/rust-khronos_api-devel.list

%changelog

%autochangelog
