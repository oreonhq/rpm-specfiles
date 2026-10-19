%global source0_hash 0e7465ac9959cc2b1404e8e2367b43684a6d13790fe23056cc8c6c5a6b7bcb94
%bcond check 0
%global debug_package %{nil}
%global crate matchit
Name:           rust-matchit0.7
Version:        0.7.3
Release:        1%{?dist}
Summary:        A high performance, zero-copy URL router.
License:        MIT AND BSD-3-Clause
URL:            https://crates.io/crates/matchit
Source0:        https://static.crates.io/crates/matchit/matchit-%{version}.crate
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
Summary:        A high performance, zero-copy URL router.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__test_helpers-devel
Summary:        A high performance, zero-copy URL router.
BuildArch:      noarch
%description -n %{name}+__test_helpers-devel

This package contains library source intended for building other packages which
use the "__test_helpers" feature of the "%{crate}" crate.

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
%files -n rust-matchit0.7-devel -f %{oreon_filedir}/rust-matchit0.7-devel.list

%changelog

%autochangelog
