%global source0_hash 79c3c892f121fff406e5dd6b28c1b30096b95111c30701a899d4f2b18da6d1bd
%bcond check 1
%global debug_package %{nil}
%global crate fixed_decimal
Name:           rust-fixed_decimal
Version:        0.7.2
Release:        1%{?dist}
Summary:        API for representing numbers in a human-readable form
License:        Unicode-3.0
URL:            https://crates.io/crates/fixed_decimal
Source0:        https://static.crates.io/crates/fixed_decimal/fixed_decimal-%{version}.crate
Patch:          fixed_decimal-fix-metadata.diff
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
Summary:        API for representing numbers in a human-readable form
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        API for representing numbers in a human-readable form
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+ryu-devel
Summary:        API for representing numbers in a human-readable form
BuildArch:      noarch
%description -n %{name}+ryu-devel

This package contains library source intended for building other packages which
use the "ryu" feature of the "%{crate}" crate.

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
%files -n rust-fixed_decimal-devel -f %{oreon_filedir}/rust-fixed_decimal-devel.list

%changelog

%autochangelog
