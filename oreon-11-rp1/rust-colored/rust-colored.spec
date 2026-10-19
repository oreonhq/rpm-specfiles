%global source0_hash faf9468729b8cbcea668e36183cb69d317348c2e08e994829fb56ebfdfbaac34
%bcond check 0
%global debug_package %{nil}
%global crate colored
Name:           rust-colored
Version:        3.1.1
Release:        1%{?dist}
Summary:        The most simple way to add colors in your terminal
License:        MPL-2.0
URL:            https://crates.io/crates/colored
Source0:        https://static.crates.io/crates/colored/colored-%{version}.crate
Patch:          colored-fix-metadata-auto.diff
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

%package     -n %{name}+no-color-devel
Summary:        The most simple way to add colors in your terminal
BuildArch:      noarch
%description -n %{name}+no-color-devel

This package contains library source intended for building other packages which
use the "no-color" feature of the "%{crate}" crate.

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
%files -n rust-colored-devel -f %{oreon_filedir}/rust-colored-devel.list

%changelog

%autochangelog
