%global source0_hash 6120e7e5dcd1c90098e349def389e2797377cdbe6b465ad8fdd115c0c99d5cf2
%bcond check 1
%global debug_package %{nil}
%global crate dns-lookup
Name:           rust-dns-lookup
Version:        4.0.1
Release:        1%{?dist}
Summary:        Simple dns resolving api, much like rust's unstable api
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dns-lookup
Source0:        https://static.crates.io/crates/dns-lookup/dns-lookup-%{version}.crate
Patch:          dns-lookup-fix-metadata-auto.diff
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
Summary:        Simple dns resolving api, much like rust's unstable api
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
%files -n rust-dns-lookup-devel -f %{oreon_filedir}/rust-dns-lookup-devel.list

%changelog

%autochangelog
