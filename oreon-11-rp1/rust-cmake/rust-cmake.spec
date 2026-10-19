%global source0_hash c0f78a02292a74a88ac736019ab962ece0bc380e3f977bf72e376c5d78ff0678
%bcond check 0
%global debug_package %{nil}
%global crate cmake
Name:           rust-cmake
Version:        0.1.58
Release:        1%{?dist}
Summary:        A build dependency for running `cmake` to build a native library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cmake
Source0:        https://static.crates.io/crates/cmake/cmake-%{version}.crate
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
Summary:        A build dependency for running `cmake` to build a native library
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
%files -n rust-cmake-devel -f %{oreon_filedir}/rust-cmake-devel.list

%changelog

%autochangelog
