%global source0_hash a4546773ffeab9e4ea02b8872faa49bb616a80a7da66afc2f32688943f97efa7
%bcond check 1
%global debug_package %{nil}
%global crate tower-test
Name:           rust-tower-test
Version:        0.4.0
Release:        1%{?dist}
Summary:        Utilities for writing client and server Service tests
License:        MIT
URL:            https://crates.io/crates/tower-test
Source0:        https://static.crates.io/crates/tower-test/tower-test-%{version}.crate
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
Summary:        Utilities for writing client and server Service tests
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
%files -n rust-tower-test-devel -f %{oreon_filedir}/rust-tower-test-devel.list

%changelog

%autochangelog
