%global source0_hash a0eb5a3343abf848c0984fe4604b2b105da9539376e24fc0a3b0007411ae4fd9
%bcond check 0
%global debug_package %{nil}
%global crate impl-trait-for-tuples
Name:           rust-impl-trait-for-tuples
Version:        0.2.3
Release:        1%{?dist}
Summary:        Attribute macro to implement a trait for tuples
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/impl-trait-for-tuples
Source0:        https://static.crates.io/crates/impl-trait-for-tuples/impl-trait-for-tuples-%{version}.crate
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
Summary:        Attribute macro to implement a trait for tuples
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
%files -n rust-impl-trait-for-tuples-devel -f %{oreon_filedir}/rust-impl-trait-for-tuples-devel.list

%changelog

%autochangelog
