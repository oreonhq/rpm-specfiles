%global source0_hash 1fe266d2e243c931d8190177f20bf7f24eed45e96f39e87dc49a27b32d12d407
%bcond check 0
%global debug_package %{nil}
%global crate is_debug
Name:           rust-is_debug
Version:        1.1.0
Release:        1%{?dist}
Summary:        Get build model is debug
License:        MIT AND Apache-2.0
URL:            https://crates.io/crates/is_debug
Source0:        https://static.crates.io/crates/is_debug/is_debug-%{version}.crate
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
Summary:        Get build model is debug
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
%files -n rust-is_debug-devel -f %{oreon_filedir}/rust-is_debug-devel.list

%changelog

%autochangelog
