%global source0_hash 754ca22de805bb5744484a5b151a9e1a8e837d5dc232c2d7d8c2e3492edc8b60
%bcond check 0
%global debug_package %{nil}
%global crate libloading
Name:           rust-libloading
Version:        0.9.0
Release:        2%{?dist}
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

%package     -n %{name}+std-devel
Summary:        Bindings around the platform's dynamic library loading primitives wit...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-libloading-devel -f %{oreon_filedir}/rust-libloading-devel.list

%changelog

%autochangelog
