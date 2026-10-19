%global source0_hash eea25e07510aa6ab6547308ebe3c036016d162b8da920dbb079e3ba8acf3d95a
%bcond check 0
%global debug_package %{nil}
%global crate prettytable-rs
Name:           rust-prettytable-rs
Version:        0.10.0
Release:        1%{?dist}
Summary:        Library for printing pretty formatted tables in terminal
License:        BSD-3-Clause
URL:            https://crates.io/crates/prettytable-rs
Source0:        https://static.crates.io/crates/prettytable-rs/prettytable-rs-%{version}.crate
Patch:          prettytable-rs-fix-metadata.diff
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
Summary:        Library for printing pretty formatted tables in terminal
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+csv-devel
Summary:        Library for printing pretty formatted tables in terminal
BuildArch:      noarch
%description -n %{name}+csv-devel

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%package     -n %{name}+evcxr-devel
Summary:        Library for printing pretty formatted tables in terminal
BuildArch:      noarch
%description -n %{name}+evcxr-devel

This package contains library source intended for building other packages which
use the "evcxr" feature of the "%{crate}" crate.

%package     -n %{name}+win_crlf-devel
Summary:        Library for printing pretty formatted tables in terminal
BuildArch:      noarch
%description -n %{name}+win_crlf-devel

This package contains library source intended for building other packages which
use the "win_crlf" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip tests::test_panic
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-prettytable-rs-devel -f %{oreon_filedir}/rust-prettytable-rs-devel.list

%changelog

%autochangelog
