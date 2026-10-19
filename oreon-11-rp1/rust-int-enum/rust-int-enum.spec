%global source0_hash e366a1634cccc76b4cfd3e7580de9b605e4d93f1edac48d786c1f867c0def495
%bcond check 1
%global debug_package %{nil}
%global crate int-enum
Name:           rust-int-enum
Version:        1.2.0
Release:        1%{?dist}
Summary:        Derive macro for conversion between integer and enum types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/int-enum
Source0:        https://static.crates.io/crates/int-enum/int-enum-%{version}.crate
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
Summary:        Derive macro for conversion between integer and enum types
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
%files -n rust-int-enum-devel -f %{oreon_filedir}/rust-int-enum-devel.list

%changelog

%autochangelog
