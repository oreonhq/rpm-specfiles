%global source0_hash e128f19525861dbded59e1e7c17653a8ed63d573ca04aed708d552dbef5bb32a
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-tencent-cos
Name:           rust-reqsign-tencent-cos
Version:        3.0.0
Release:        1%{?dist}
Summary:        Tencent Cloud COS signing implementation for reqsign
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-tencent-cos
Source0:        https://static.crates.io/crates/reqsign-tencent-cos/reqsign-tencent-cos-%{version}.crate
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
Summary:        Tencent Cloud COS signing implementation for reqsign
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
%files -n rust-reqsign-tencent-cos-devel -f %{oreon_filedir}/rust-reqsign-tencent-cos-devel.list

%changelog

%autochangelog
