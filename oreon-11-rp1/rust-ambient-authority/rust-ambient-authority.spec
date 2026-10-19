%global source0_hash e9d4ee0d472d1cd2e28c97dfa124b3d8d992e10eb0a035f33f5d12e3a177ba3b
%bcond check 0
%global debug_package %{nil}
%global crate ambient-authority
Name:           rust-ambient-authority
Version:        0.0.2
Release:        1%{?dist}
Summary:        Ambient Authority
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/ambient-authority
Source0:        https://static.crates.io/crates/ambient-authority/ambient-authority-%{version}.crate
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
Summary:        Ambient Authority
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
%files -n rust-ambient-authority-devel -f %{oreon_filedir}/rust-ambient-authority-devel.list

%changelog

%autochangelog
