%global source0_hash e31bc9ad994ba00e440a8aa5c9ef0ec67d5cb5e5cb0cc7f8b744a35b389cc470
%bcond check 1
%global debug_package %{nil}
%global crate iana-time-zone
Name:           rust-iana-time-zone
Version:        0.1.65
Release:        1%{?dist}
Summary:        get the IANA time zone for the current system
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/iana-time-zone
Source0:        https://static.crates.io/crates/iana-time-zone/iana-time-zone-%{version}.crate
Patch:          iana-time-zone-fix-metadata-auto.diff
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
Summary:        get the IANA time zone for the current system
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fallback-devel
Summary:        get the IANA time zone for the current system
BuildArch:      noarch
%description -n %{name}+fallback-devel

This package contains library source intended for building other packages which
use the "fallback" feature of the "%{crate}" crate.

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
%files -n rust-iana-time-zone-devel -f %{oreon_filedir}/rust-iana-time-zone-devel.list

%changelog

%autochangelog
