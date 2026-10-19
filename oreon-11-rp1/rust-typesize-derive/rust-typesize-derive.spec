%global source0_hash 536b6812192bda8551cfa0e52524e328c6a951b48e66529ee4522d6c721243d6
%bcond check 0
%global debug_package %{nil}
%global crate typesize-derive
Name:           rust-typesize-derive
Version:        0.1.11
Release:        1%{?dist}
Summary:        Internal proc-macro crate for typesize
License:        MIT
URL:            https://crates.io/crates/typesize-derive
Source0:        https://static.crates.io/crates/typesize-derive/typesize-derive-%{version}.crate
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

%package     -n %{name}+details-devel
Summary:        Internal proc-macro crate for typesize
BuildArch:      noarch
%description -n %{name}+details-devel

This package contains library source intended for building other packages which
use the "details" feature of the "%{crate}" crate.

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
%files -n rust-typesize-derive-devel -f %{oreon_filedir}/rust-typesize-derive-devel.list

%changelog

%autochangelog
