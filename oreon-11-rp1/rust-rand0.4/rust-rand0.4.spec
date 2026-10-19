%global source0_hash 552840b97013b1a26992c11eac34bdd778e464601a4c2054b5f0bff7c6761293
%bcond check 1
%global debug_package %{nil}
%global crate rand
Name:           rust-rand0.4
Version:        0.4.6
Release:        1%{?dist}
Summary:        Random number generators and other randomness functionality
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
Source0:        https://static.crates.io/crates/rand/rand-%{version}.crate
Patch:          rand-fix-metadata-auto.diff
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
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+i128_support-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+i128_support-devel

This package contains library source intended for building other packages which
use the "i128_support" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Random number generators and other randomness functionality
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i 's@^#!/usr/bin/env python$@#!/usr/bin/python3@' utils/ziggurat_tables.py
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
%files -n rust-rand0.4-devel -f %{oreon_filedir}/rust-rand0.4-devel.list

%changelog

%autochangelog
