%global source0_hash fe5e43d0f78a42ad591453aedb1d7ae631ce7ee445c7643691055a9ed8d3b01c
%bcond check 0
%global debug_package %{nil}
%global crate fail
Name:           rust-fail
Version:        0.5.1
Release:        1%{?dist}
Summary:        Fail points for rust.
License:        Apache-2.0
URL:            https://crates.io/crates/fail
Source0:        https://static.crates.io/crates/fail/fail-%{version}.crate
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

%package     -n %{name}+failpoints-devel
Summary:        Fail points for rust.
BuildArch:      noarch
%description -n %{name}+failpoints-devel

This package contains library source intended for building other packages which
use the "failpoints" feature of the "%{crate}" crate.

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
%files -n rust-fail-devel -f %{oreon_filedir}/rust-fail-devel.list

%changelog

%autochangelog
