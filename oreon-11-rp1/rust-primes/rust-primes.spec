%global source0_hash 0466ef49edd4a5a4bc9d62804a34e89366810bd8bfc3ed537101e3d099f245c5
%bcond check 1
%global debug_package %{nil}
%global crate primes
Name:           rust-primes
Version:        0.4.0
Release:        1%{?dist}
Summary:        Package for calculating primes using the Sieve of Eratosthenes
License:        BSD-3-Clause
URL:            https://crates.io/crates/primes
Source0:        https://static.crates.io/crates/primes/primes-%{version}.crate
Patch:          primes-fix-metadata.diff
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
Summary:        Package for calculating primes using the Sieve of Eratosthenes
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
%files -n rust-primes-devel -f %{oreon_filedir}/rust-primes-devel.list

%changelog

%autochangelog
