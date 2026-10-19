%global source0_hash 67c78a4d8fdf9953a5c9d458f9efe940fd97a0cab0941c075a813ac594733827
%bcond check 0
%global debug_package %{nil}
%global crate enumflags2_derive
Name:           rust-enumflags2_derive
Version:        0.7.12
Release:        1%{?dist}
Summary:        Do not use directly, use the reexport in the `enumflags2` crate. This...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/enumflags2_derive
Source0:        https://static.crates.io/crates/enumflags2_derive/enumflags2_derive-%{version}.crate
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
Summary:        Do not use directly, use the reexport in the `enumflags2` crate. This...
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
%files -n rust-enumflags2_derive-devel -f %{oreon_filedir}/rust-enumflags2_derive-devel.list

%changelog

%autochangelog
