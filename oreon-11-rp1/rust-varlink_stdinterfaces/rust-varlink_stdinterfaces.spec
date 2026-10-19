%global source0_hash 7d2ee0565003f10d8207c9e2d8e2209b280a94a8d1ad5e6f0711454f8e42abe1
%bcond check 0
%global debug_package %{nil}
%global crate varlink_stdinterfaces
Name:           rust-varlink_stdinterfaces
Version:        11.0.2
Release:        1%{?dist}
Summary:        Varlink common interfaces
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/varlink_stdinterfaces
Source0:        https://static.crates.io/crates/varlink_stdinterfaces/varlink_stdinterfaces-%{version}.crate
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
Summary:        Varlink common interfaces
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
%files -n rust-varlink_stdinterfaces-devel -f %{oreon_filedir}/rust-varlink_stdinterfaces-devel.list

%changelog

%autochangelog
