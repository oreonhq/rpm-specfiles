%global source0_hash 8f42a60cbdf9a97f5d2305f08a87dc4e09308d1276d28c869c684d7777685682
%bcond check 1
%global debug_package %{nil}
%global crate itoa
Name:           rust-itoa
Version:        1.0.18
Release:        1%{?dist}
Summary:        Fast integer primitive to string conversion
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/itoa
Source0:        https://static.crates.io/crates/itoa/itoa-%{version}.crate
Patch:          itoa-fix-metadata.diff
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
Summary:        Fast integer primitive to string conversion
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no-panic-devel
Summary:        Fast integer primitive to string conversion
BuildArch:      noarch
%description -n %{name}+no-panic-devel

This package contains library source intended for building other packages which
use the "no-panic" feature of the "%{crate}" crate.

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
%files -n rust-itoa-devel -f %{oreon_filedir}/rust-itoa-devel.list

%changelog

%autochangelog
