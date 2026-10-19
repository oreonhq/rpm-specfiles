%global source0_hash 879917b256f6317769b9f374b435805a8697013098aacce5a38ac106cd6a9469
%bcond check 0
%global debug_package %{nil}
%global crate libz-ng-sys
Name:           rust-libz-ng-sys
Version:        1.1.29
Release:        1%{?dist}
Summary:        Low-level bindings to zlib-ng (libz-ng), a high-performance zlib libr...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libz-ng-sys
Source0:        https://static.crates.io/crates/libz-ng-sys/libz-ng-sys-%{version}.crate
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
Summary:        Low-level bindings to zlib-ng (libz-ng), a high-performance zlib libr...
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
%files -n rust-libz-ng-sys-devel -f %{oreon_filedir}/rust-libz-ng-sys-devel.list

%changelog

%autochangelog
