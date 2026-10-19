%global source0_hash aba069c070b5e213f2a094deb7e5ed50ecb092be36102a4f4042e8d2056d060e
%bcond check 1
%global debug_package %{nil}
%global crate speedate
Name:           rust-speedate
Version:        0.17.0
Release:        1%{?dist}
Summary:        Fast and simple datetime, date, time and duration parsing
License:        MIT
URL:            https://crates.io/crates/speedate
Source0:        https://static.crates.io/crates/speedate/speedate-%{version}.crate
Patch:          speedate-fix-metadata.diff
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
Summary:        Fast and simple datetime, date, time and duration parsing
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
%files -n rust-speedate-devel -f %{oreon_filedir}/rust-speedate-devel.list

%changelog

%autochangelog
