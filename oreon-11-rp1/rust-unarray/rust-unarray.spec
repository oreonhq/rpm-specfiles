%global source0_hash eaea85b334db583fe3274d12b4cd1880032beab409c0d774be044d4480ab9a94
%bcond check 1
%global debug_package %{nil}
%global crate unarray
Name:           rust-unarray
Version:        0.1.4
Release:        1%{?dist}
Summary:        Utilities for working with uninitialized arrays
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unarray
Source0:        https://static.crates.io/crates/unarray/unarray-%{version}.crate
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
Summary:        Utilities for working with uninitialized arrays
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
%files -n rust-unarray-devel -f %{oreon_filedir}/rust-unarray-devel.list

%changelog

%autochangelog
