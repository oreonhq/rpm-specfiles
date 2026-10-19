%global source0_hash 925383efa346730478fb4838dbe9137d2a47675ad789c546d150a6e1dd4ab31c
%bcond check 0
%global debug_package %{nil}
%global crate precomputed-hash
Name:           rust-precomputed-hash
Version:        0.1.1
Release:        2%{?dist}
Summary:        A library intending to be a base dependency to expose a precomputed hash
License:        MIT
URL:            https://crates.io/crates/precomputed-hash
Source0:        https://static.crates.io/crates/precomputed-hash/precomputed-hash-%{version}.crate
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
Summary:        A library intending to be a base dependency to expose a precomputed hash
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
%files -n rust-precomputed-hash-devel -f %{oreon_filedir}/rust-precomputed-hash-devel.list

%changelog

%autochangelog
