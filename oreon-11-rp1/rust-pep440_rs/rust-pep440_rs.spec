%global source0_hash 31095ca1f396e3de32745f42b20deef7bc09077f918b085307e8eab6ddd8fb9c
%bcond check 1
%global debug_package %{nil}
%global crate pep440_rs
Name:           rust-pep440_rs
Version:        0.7.3
Release:        1%{?dist}
Summary:        Library for python version numbers and specifiers, implementing PEP 440
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://crates.io/crates/pep440_rs
Source0:        https://static.crates.io/crates/pep440_rs/pep440_rs-%{version}.crate
Patch:          pep440_rs-fix-metadata.diff
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
Summary:        Library for python version numbers and specifiers, implementing PEP 440
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rkyv-devel
Summary:        Library for python version numbers and specifiers, implementing PEP 440
BuildArch:      noarch
%description -n %{name}+rkyv-devel

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Library for python version numbers and specifiers, implementing PEP 440
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+version-ranges-devel
Summary:        Library for python version numbers and specifiers, implementing PEP 440
BuildArch:      noarch
%description -n %{name}+version-ranges-devel

This package contains library source intended for building other packages which
use the "version-ranges" feature of the "%{crate}" crate.

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
%files -n rust-pep440_rs-devel -f %{oreon_filedir}/rust-pep440_rs-devel.list

%changelog

%autochangelog
