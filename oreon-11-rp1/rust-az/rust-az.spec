%global source0_hash 7b7e4c2464d97fe331d41de9d5db0def0a96f4d823b8b32a2efd503578988973
%bcond check 0
%global debug_package %{nil}
%global crate az
Name:           rust-az
Version:        1.2.1
Release:        1%{?dist}
Summary:        Casts and checked casts
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/az
Source0:        https://static.crates.io/crates/az/az-%{version}.crate
Patch:          0001-deny-warnings-considered-harmful.patch
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
Summary:        Casts and checked casts
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fail-on-warnings-devel
Summary:        Casts and checked casts
BuildArch:      noarch
%description -n %{name}+fail-on-warnings-devel

This package contains library source intended for building other packages which
use the "fail-on-warnings" feature of the "%{crate}" crate.

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
%files -n rust-az-devel -f %{oreon_filedir}/rust-az-devel.list

%changelog

%autochangelog
