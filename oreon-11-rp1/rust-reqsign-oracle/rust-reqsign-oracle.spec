%global source0_hash d53fa7e985db64d7221cc02016a5ec5750a1c15b7482b29f9c66e26f2c3202a5
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-oracle
Name:           rust-reqsign-oracle
Version:        3.0.6
Release:        1%{?dist}
Summary:        Oracle Cloud signing implementation for reqsign
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-oracle
Source0:        https://static.crates.io/crates/reqsign-oracle/reqsign-oracle-%{version}.crate
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
Summary:        Oracle Cloud signing implementation for reqsign
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
%files -n rust-reqsign-oracle-devel -f %{oreon_filedir}/rust-reqsign-oracle-devel.list

%changelog

%autochangelog
