%global source0_hash dc00caaa3fb3201ff7a18aa458e8c3ab042b9da154cfdf948bdde3936c31c36e
%bcond check 1
%global debug_package %{nil}
%global crate icu_calendar_data
Name:           rust-icu_calendar_data
Version:        2.3.0
Release:        1%{?dist}
Summary:        Data for the icu_calendar crate
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_calendar_data
Source0:        https://static.crates.io/crates/icu_calendar_data/icu_calendar_data-%{version}.crate
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
Summary:        Data for the icu_calendar crate
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
%files -n rust-icu_calendar_data-devel -f %{oreon_filedir}/rust-icu_calendar_data-devel.list

%changelog

%autochangelog
