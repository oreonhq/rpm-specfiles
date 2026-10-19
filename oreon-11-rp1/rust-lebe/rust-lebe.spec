%global source0_hash 7a79a3332a6609480d7d0c9eab957bca6b455b91bb84e66d19f5ff66294b85b8
%bcond check 0
%global debug_package %{nil}
%global crate lebe
Name:           rust-lebe
Version:        0.5.3
Release:        1%{?dist}
Summary:        Tiny, dead simple, high performance endianness conversions with a gen...
License:        BSD-3-Clause
URL:            https://crates.io/crates/lebe
Source0:        https://static.crates.io/crates/lebe/lebe-%{version}.crate
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
Summary:        Tiny, dead simple, high performance endianness conversions with a gen...
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
%files -n rust-lebe-devel -f %{oreon_filedir}/rust-lebe-devel.list

%changelog

%autochangelog
