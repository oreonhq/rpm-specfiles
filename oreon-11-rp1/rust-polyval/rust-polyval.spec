%global source0_hash 9d1fe60d06143b2430aa532c94cfe9e29783047f06c0d7fd359a9a51b729fa25
%bcond check 0
%global debug_package %{nil}
%global crate polyval
Name:           rust-polyval
Version:        0.6.2
Release:        1%{?dist}
Summary:        POLYVAL is a GHASH-like universal hash over GF(2^128) useful for cons...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/polyval
Source0:        https://static.crates.io/crates/polyval/polyval-%{version}.crate
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

%package     -n %{name}+std-devel
Summary:        POLYVAL is a GHASH-like universal hash over GF(2^128) useful for cons...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        POLYVAL is a GHASH-like universal hash over GF(2^128) useful for cons...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-polyval-devel -f %{oreon_filedir}/rust-polyval-devel.list

%changelog

%autochangelog
