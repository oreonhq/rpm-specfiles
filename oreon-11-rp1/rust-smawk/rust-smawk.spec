%global source0_hash e8e2fb0f499abb4d162f2bedad68f5ef91a1682b5a03596ddb67efd37768d100
%bcond check 0
%global debug_package %{nil}
%global crate smawk
Name:           rust-smawk
Version:        0.3.3
Release:        1%{?dist}
Summary:        Functions for finding row-minima in a totally monotone matrix.
License:        MIT
URL:            https://crates.io/crates/smawk
Source0:        https://static.crates.io/crates/smawk/smawk-%{version}.crate
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
Summary:        Functions for finding row-minima in a totally monotone matrix.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ndarray-devel
Summary:        Functions for finding row-minima in a totally monotone matrix.
BuildArch:      noarch
%description -n %{name}+ndarray-devel

This package contains library source intended for building other packages which
use the "ndarray" feature of the "%{crate}" crate.

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
%files -n rust-smawk-devel -f %{oreon_filedir}/rust-smawk-devel.list

%changelog

%autochangelog
