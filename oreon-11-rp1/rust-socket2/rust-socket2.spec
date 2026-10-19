%global source0_hash c3d1e2c7f27f8d4cb10542a02c49005dbd6e93095799d6f3be745fae9f8fedd4
%bcond check 0
%global debug_package %{nil}
%global crate socket2
Name:           rust-socket2
Version:        0.6.5
Release:        1%{?dist}
Summary:        Utilities for handling networking sockets with a maximal amount of co...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/socket2
Source0:        https://static.crates.io/crates/socket2/socket2-%{version}.crate
Patch:          socket2-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/default) = %{version}
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Utilities for handling networking sockets with a maximal amount of co...
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

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
%files -n rust-socket2-devel -f %{oreon_filedir}/rust-socket2-devel.list

%changelog

%autochangelog
