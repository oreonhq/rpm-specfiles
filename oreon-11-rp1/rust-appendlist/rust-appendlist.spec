%global source0_hash e149dc73cd30538307e7ffa2acd3d2221148eaeed4871f246657b1c3eaa1cbd2
%bcond check 0
%global debug_package %{nil}
%global crate appendlist
Name:           rust-appendlist
Version:        1.4.0
Release:        1%{?dist}
Summary:        Append-only list that preserves references to its elements
License:        MIT
URL:            https://crates.io/crates/appendlist
Source0:        https://static.crates.io/crates/appendlist/appendlist-%{version}.crate
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
Summary:        Append-only list that preserves references to its elements
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
%files -n rust-appendlist-devel -f %{oreon_filedir}/rust-appendlist-devel.list

%changelog

%autochangelog
