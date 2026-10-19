%global source0_hash 4250ce6452e92010fdf7268ccc5d14faa80bb12fc741938534c58f16804e03c7
%bcond check 1
%global debug_package %{nil}
%global crate inout
Name:           rust-inout
Version:        0.2.2
Release:        1%{?dist}
Summary:        Custom reference types for code generic over in-place and
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/inout
Source0:        https://static.crates.io/crates/inout/inout-%{version}.crate
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
Summary:        Custom reference types for code generic over in-place and
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
%files -n rust-inout-devel -f %{oreon_filedir}/rust-inout-devel.list

%changelog

%autochangelog
