%global source0_hash e2db0b750e9ae64e6c3d913832dc19ed580b9210bcd7c4dd6d0dd21af469fc14
%bcond check 1
%global debug_package %{nil}
%global crate keyvalues-serde
Name:           rust-keyvalues-serde
Version:        0.2.2
Release:        1%{?dist}
Summary:        (De)serialize VDF text with serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/keyvalues-serde
Source0:        https://static.crates.io/crates/keyvalues-serde/keyvalues-serde-%{version}.crate
Patch:          keyvalues-serde-fix-metadata.diff
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
Summary:        (De)serialize VDF text with serde
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
%files -n rust-keyvalues-serde-devel -f %{oreon_filedir}/rust-keyvalues-serde-devel.list

%changelog

%autochangelog
