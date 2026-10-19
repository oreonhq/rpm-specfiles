%global source0_hash 6a1f896587b6f2c069c73d2f0913e2d590c3990285cd2f0b6aa02b786b4c679c
%bcond check 0
%global debug_package %{nil}
%global crate bytemuck_derive
Name:           rust-bytemuck_derive
Version:        1.12.1
Release:        1%{?dist}
Summary:        Derive proc-macros for bytemuck
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/bytemuck_derive
Source0:        https://static.crates.io/crates/bytemuck_derive/bytemuck_derive-%{version}.crate
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
Summary:        Derive proc-macros for bytemuck
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
%files -n rust-bytemuck_derive-devel -f %{oreon_filedir}/rust-bytemuck_derive-devel.list

%changelog

%autochangelog
