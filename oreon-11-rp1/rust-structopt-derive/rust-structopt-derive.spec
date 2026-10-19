%global source0_hash dcb5ae327f9cc13b68763b5749770cb9e048a99bd9dfdfa58d0cf05d5f64afe0
%bcond check 0
%global debug_package %{nil}
%global crate structopt-derive
Name:           rust-structopt-derive
Version:        0.4.18
Release:        1%{?dist}
Summary:        Parse command line argument by defining a struct, derive crate
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/structopt-derive
Source0:        https://static.crates.io/crates/structopt-derive/structopt-derive-%{version}.crate
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
Summary:        Parse command line argument by defining a struct, derive crate
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
%files -n rust-structopt-derive-devel -f %{oreon_filedir}/rust-structopt-derive-devel.list

%changelog

%autochangelog
