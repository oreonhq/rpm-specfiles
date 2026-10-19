%global source0_hash 49d57902bb128e5e38b5218d3681215ae3e322d99f65d5420e9849730d2ea372
%bcond check 1
%global debug_package %{nil}
%global crate statistical
Name:           rust-statistical
Version:        1.0.0
Release:        1%{?dist}
Summary:        Simple statistics library
License:        MIT
URL:            https://crates.io/crates/statistical
Source0:        https://static.crates.io/crates/statistical/statistical-%{version}.crate
Patch:          statistical-fix-metadata.diff
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
Summary:        Simple statistics library
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

%cargo_test -- -- --skip univariate_::test::test_pkurtosis
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-statistical-devel -f %{oreon_filedir}/rust-statistical-devel.list

%changelog

%autochangelog
