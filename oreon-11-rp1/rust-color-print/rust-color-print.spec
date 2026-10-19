%global source0_hash 3aa954171903797d5623e047d9ab69d91b493657917bdfb8c2c80ecaf9cdb6f4
%bcond check 1
%global debug_package %{nil}
%global crate color-print
Name:           rust-color-print
Version:        0.3.7
Release:        1%{?dist}
Summary:        Colorize and stylize strings for terminal at compile-time, by
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/color-print
Source0:        https://static.crates.io/crates/color-print/color-print-%{version}.crate
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
Summary:        Colorize and stylize strings for terminal at compile-time, by
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+terminfo-devel
Summary:        Colorize and stylize strings for terminal at compile-time, by
BuildArch:      noarch
%description -n %{name}+terminfo-devel

This package contains library source intended for building other packages which
use the "terminfo" feature of the "%{crate}" crate.

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
%files -n rust-color-print-devel -f %{oreon_filedir}/rust-color-print-devel.list

%changelog

%autochangelog
