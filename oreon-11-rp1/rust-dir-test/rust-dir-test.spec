%global source0_hash 62c013fe825864f3e4593f36426c1fa7a74f5603f13ca8d1af7a990c1cd94a79
%bcond check 1
%global debug_package %{nil}
%global crate dir-test
Name:           rust-dir-test
Version:        0.4.1
Release:        1%{?dist}
Summary:        Macro to generate tests from files in a directory
License:        Apache-2.0
URL:            https://crates.io/crates/dir-test
Source0:        https://static.crates.io/crates/dir-test/dir-test-%{version}.crate
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
Summary:        Macro to generate tests from files in a directory
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
%files -n rust-dir-test-devel -f %{oreon_filedir}/rust-dir-test-devel.list

%changelog

%autochangelog
