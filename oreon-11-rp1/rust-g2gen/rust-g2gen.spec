%global source0_hash c5a7e0eb46f83a20260b850117d204366674e85d3a908d90865c78df9a6b1dfc
%bcond check 1
%global debug_package %{nil}
%global crate g2gen
Name:           rust-g2gen
Version:        1.2.2
Release:        1%{?dist}
Summary:        Macro to create types that implement fast finite field arithmetic
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/g2gen
Source0:        https://static.crates.io/crates/g2gen/g2gen-%{version}.crate
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
Summary:        Macro to create types that implement fast finite field arithmetic
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
%files -n rust-g2gen-devel -f %{oreon_filedir}/rust-g2gen-devel.list

%changelog

%autochangelog
