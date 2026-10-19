%global source0_hash b67380fd3b2fbe7527a606e18729d21c6f3951633d0500574c4dc22d2d638b9f
%bcond check 0
%global debug_package %{nil}
%global crate libloading
Name:           rust-libloading0.7
Version:        0.7.4
Release:        1%{?dist}
Summary:        Bindings around the platform's dynamic library loading primitives wit...
License:        ISC
URL:            https://crates.io/crates/libloading
Source0:        https://static.crates.io/crates/libloading/libloading-%{version}.crate
Patch:          libloading-fix-metadata-auto.diff
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
Summary:        Bindings around the platform's dynamic library loading primitives wit...
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
%files -n rust-libloading0.7-devel -f %{oreon_filedir}/rust-libloading0.7-devel.list

%changelog

%autochangelog
