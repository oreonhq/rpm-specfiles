%global source0_hash 495503291b258422ea2bb9863d9f4e31eadbc5bcbdbe8b721769fa2c98dc4d41
%bcond check 0
%global debug_package %{nil}
%global crate databake-derive
Name:           rust-databake-derive
Version:        0.2.2
Release:        1%{?dist}
Summary:        Custom derive for the databake crate
License:        Unicode-3.0
URL:            https://crates.io/crates/databake-derive
Source0:        https://static.crates.io/crates/databake-derive/databake-derive-%{version}.crate
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
Summary:        Custom derive for the databake crate
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
%files -n rust-databake-derive-devel -f %{oreon_filedir}/rust-databake-derive-devel.list

%changelog

%autochangelog
