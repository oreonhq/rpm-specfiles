%global source0_hash 457d7ed3f888dfd2c7af56d4975cade43c622f74bdcddfed6d4352f57acc6310
%bcond check 1
%global debug_package %{nil}
%global crate bb8
Name:           rust-bb8
Version:        0.9.1
Release:        1%{?dist}
Summary:        Full-featured async (tokio-based) connection pool (like r2d2)
License:        MIT
URL:            https://crates.io/crates/bb8
Source0:        https://static.crates.io/crates/bb8/bb8-%{version}.crate
Patch:          bb8-fix-metadata-auto.diff
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
Summary:        Full-featured async (tokio-based) connection pool (like r2d2)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Full-featured async (tokio-based) connection pool (like r2d2)
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

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
%files -n rust-bb8-devel -f %{oreon_filedir}/rust-bb8-devel.list

%changelog

%autochangelog
