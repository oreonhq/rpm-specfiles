%global source0_hash 4c3cf4824e2d5f025c7b531afcb2325364084a16806f6d47fbc1f5fbd9960590
%bcond check 0
%global debug_package %{nil}
%global crate dtoa
Name:           rust-dtoa
Version:        1.0.11
Release:        1%{?dist}
Summary:        Fast functions for printing floating-point primitives to an io::Write
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dtoa
Source0:        https://static.crates.io/crates/dtoa/dtoa-%{version}.crate
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
Summary:        Fast functions for printing floating-point primitives to an io::Write
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
%files -n rust-dtoa-devel -f %{oreon_filedir}/rust-dtoa-devel.list

%changelog

%autochangelog
