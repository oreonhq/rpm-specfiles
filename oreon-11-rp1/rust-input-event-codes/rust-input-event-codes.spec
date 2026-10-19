%global source0_hash d437b85b6856c30525a380e2de28d630cd2f03b4eec8e8a043d71d7e223792dd
%bcond check 1
%global debug_package %{nil}
%global crate input-event-codes
Name:           rust-input-event-codes
Version:        6.2.0
Release:        1%{?dist}
Summary:        Linux input event codes form linux/input_event_codes.h
License:        GPL-2.0-only
URL:            https://crates.io/crates/input-event-codes
Source0:        https://static.crates.io/crates/input-event-codes/input-event-codes-%{version}.crate
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
Summary:        Linux input event codes form linux/input_event_codes.h
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
%files -n rust-input-event-codes-devel -f %{oreon_filedir}/rust-input-event-codes-devel.list

%changelog

%autochangelog
