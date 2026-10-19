%global source0_hash d0881ea181b1df73ff77ffaaf9c7544ecc11e82fba9b5f27b262a3c73a332555
%bcond check 1
%global debug_package %{nil}
%global crate dyn-clone
Name:           rust-dyn-clone
Version:        1.0.20
Release:        1%{?dist}
Summary:        Clone trait that is dyn-compatible
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dyn-clone
Source0:        https://static.crates.io/crates/dyn-clone/dyn-clone-%{version}.crate
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
Summary:        Clone trait that is dyn-compatible
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
%files -n rust-dyn-clone-devel -f %{oreon_filedir}/rust-dyn-clone-devel.list

%changelog

%autochangelog
