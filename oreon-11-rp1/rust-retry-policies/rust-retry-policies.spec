%global source0_hash dc05fbf560421a0357a750cbe78c7ca19d4923918490daabba313d5dbc871e47
%bcond check 1
%global debug_package %{nil}
%global crate retry-policies
Name:           rust-retry-policies
Version:        0.5.2
Release:        1%{?dist}
Summary:        Collection of plug-and-play retry policies for Rust projects
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/retry-policies
Source0:        https://static.crates.io/crates/retry-policies/retry-policies-%{version}.crate
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
Summary:        Collection of plug-and-play retry policies for Rust projects
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
%files -n rust-retry-policies-devel -f %{oreon_filedir}/rust-retry-policies-devel.list

%changelog

%autochangelog
