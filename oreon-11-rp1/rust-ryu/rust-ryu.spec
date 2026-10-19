%global source0_hash 9774ba4a74de5f7b1c1451ed6cd5285a32eddb5cccb8cc655a4e50009e06477f
%bcond check 1
%global debug_package %{nil}
%global crate ryu
Name:           rust-ryu
Version:        1.0.23
Release:        1%{?dist}
Summary:        Fast floating point to string conversion
License:        Apache-2.0 OR BSL-1.0
URL:            https://crates.io/crates/ryu
Source0:        https://static.crates.io/crates/ryu/ryu-%{version}.crate
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

%package     -n %{name}+no-panic-devel
Summary:        Fast floating point to string conversion
BuildArch:      noarch
%description -n %{name}+no-panic-devel

This package contains library source intended for building other packages which
use the "no-panic" feature of the "%{crate}" crate.

%package     -n %{name}+small-devel
Summary:        Fast floating point to string conversion
BuildArch:      noarch
%description -n %{name}+small-devel

This package contains library source intended for building other packages which
use the "small" feature of the "%{crate}" crate.

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
%files -n rust-ryu-devel -f %{oreon_filedir}/rust-ryu-devel.list

%changelog

%autochangelog
