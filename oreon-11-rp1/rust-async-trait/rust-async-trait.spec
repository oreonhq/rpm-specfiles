%global source0_hash ae36dc4177970ef04fde5178d3e2429882def40e57a451f919c098f72baa6cec
%bcond check 0
%global debug_package %{nil}
%global crate async-trait
Name:           rust-async-trait
Version:        0.1.91
Release:        1%{?dist}
Summary:        Type erasure for async trait methods
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-trait
Source0:        https://static.crates.io/crates/async-trait/async-trait-%{version}.crate
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
Summary:        Type erasure for async trait methods
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
%files -n rust-async-trait-devel -f %{oreon_filedir}/rust-async-trait-devel.list

%changelog

%autochangelog
