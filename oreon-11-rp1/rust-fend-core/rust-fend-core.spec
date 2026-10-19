%global source0_hash 59b16d394a9991c9b0fee89855daafc7c6cd341be9528ac8b45f9b7aed3d8be8
%bcond check 1
%global debug_package %{nil}
%global crate fend-core
Name:           rust-fend-core
Version:        1.5.8
Release:        1%{?dist}
Summary:        Arbitrary-precision unit-aware calculator
License:        MIT
URL:            https://crates.io/crates/fend-core
Source0:        https://static.crates.io/crates/fend-core/fend-core-%{version}.crate
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
Summary:        Arbitrary-precision unit-aware calculator
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
%files -n rust-fend-core-devel -f %{oreon_filedir}/rust-fend-core-devel.list

%changelog

%autochangelog
