%global source0_hash f764005d11ee5f36500a149ace24e00e3da98b0158b3e2d53a7495660d3f4d60
%bcond check 0
%global debug_package %{nil}
%global crate take_mut
Name:           rust-take_mut
Version:        0.2.2
Release:        1%{?dist}
Summary:        Take a T from a &mut T temporarily
License:        MIT
URL:            https://crates.io/crates/take_mut
Source0:        https://static.crates.io/crates/take_mut/take_mut-%{version}.crate
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
Summary:        Take a T from a &mut T temporarily
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
%files -n rust-take_mut-devel -f %{oreon_filedir}/rust-take_mut-devel.list

%changelog

%autochangelog
