%global source0_hash 71146f15c55f02214362b2357630e0b8078e249657b234b52f25469dbbead79b
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_mktemp
Name:           rust-uu_mktemp
Version:        0.12.0
Release:        1%{?dist}
Summary:        mktemp ~ (uutils) create and display a temporary file or directory from TEMPLATE
License:        MIT
URL:            https://crates.io/crates/uu_mktemp
Source0:        https://static.crates.io/crates/uu_mktemp/uu_mktemp-%{version}.crate
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
Summary:        mktemp ~ (uutils) create and display a temporary file or directory from TEMPLATE
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
%files -n rust-uu_mktemp-devel -f %{oreon_filedir}/rust-uu_mktemp-devel.list

%changelog

%autochangelog
