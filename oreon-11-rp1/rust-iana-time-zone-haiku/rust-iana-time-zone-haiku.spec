%global source0_hash f31827a206f56af32e590ba56d5d2d085f558508192593743f16b2306495269f
%bcond check 0
%global debug_package %{nil}
%global crate iana-time-zone-haiku
Name:           rust-iana-time-zone-haiku
Version:        0.1.2
Release:        1%{?dist}
Summary:        iana-time-zone support crate for Haiku OS
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/iana-time-zone-haiku
Source0:        https://static.crates.io/crates/iana-time-zone-haiku/iana-time-zone-haiku-%{version}.crate
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
Summary:        iana-time-zone support crate for Haiku OS
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
%files -n rust-iana-time-zone-haiku-devel -f %{oreon_filedir}/rust-iana-time-zone-haiku-devel.list

%changelog

%autochangelog
