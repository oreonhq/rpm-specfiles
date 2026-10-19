%global source0_hash 8df54ec7de5d7a5b917695a67baba53ec6fa5d75ce4c4f4550db68618779a6d7
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-huaweicloud-obs
Name:           rust-reqsign-huaweicloud-obs
Version:        3.0.0
Release:        1%{?dist}
Summary:        Huawei Cloud OBS signing implementation for reqsign
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-huaweicloud-obs
Source0:        https://static.crates.io/crates/reqsign-huaweicloud-obs/reqsign-huaweicloud-obs-%{version}.crate
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
Summary:        Huawei Cloud OBS signing implementation for reqsign
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
%files -n rust-reqsign-huaweicloud-obs-devel -f %{oreon_filedir}/rust-reqsign-huaweicloud-obs-devel.list

%changelog

%autochangelog
