%global source0_hash a29ab7c0ed62970beb0534d637a8688842506d0ff9157de83286dacd065c8149
%bcond check 1
%global debug_package %{nil}
%global crate assert_cli
Name:           rust-assert_cli
Version:        0.6.3
Release:        1%{?dist}
Summary:        Test CLI Applications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/assert_cli
Source0:        https://static.crates.io/crates/assert_cli/assert_cli-%{version}.crate
Patch:          assert_cli-fix-metadata.diff
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
Summary:        Test CLI Applications
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
%files -n rust-assert_cli-devel -f %{oreon_filedir}/rust-assert_cli-devel.list

%changelog

%autochangelog
