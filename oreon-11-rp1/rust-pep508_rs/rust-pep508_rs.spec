%global source0_hash faee7227064121fcadcd2ff788ea26f0d8f2bd23a0574da11eca23bc935bcc05
%bcond check 1
%global debug_package %{nil}
%global crate pep508_rs
Name:           rust-pep508_rs
Version:        0.9.2
Release:        1%{?dist}
Summary:        Library for python dependency specifiers, better known as PEP 508
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://crates.io/crates/pep508_rs
Source0:        https://static.crates.io/crates/pep508_rs/pep508_rs-%{version}.crate
Patch:          pep508_rs-fix-metadata.diff
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
Summary:        Library for python dependency specifiers, better known as PEP 508
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+non-pep508-extensions-devel
Summary:        Library for python dependency specifiers, better known as PEP 508
BuildArch:      noarch
%description -n %{name}+non-pep508-extensions-devel

This package contains library source intended for building other packages which
use the "non-pep508-extensions" feature of the "%{crate}" crate.

%package     -n %{name}+schemars-devel
Summary:        Library for python dependency specifiers, better known as PEP 508
BuildArch:      noarch
%description -n %{name}+schemars-devel

This package contains library source intended for building other packages which
use the "schemars" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Library for python dependency specifiers, better known as PEP 508
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-pep508_rs-devel -f %{oreon_filedir}/rust-pep508_rs-devel.list

%changelog

%autochangelog
