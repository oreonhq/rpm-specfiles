%global source0_hash 4595346337e5a357f0322669f45d7f5f75f9c8636061c66edb72e1064597fc71
%bcond check 0
%global debug_package %{nil}
%global crate netmap_sys
Name:           rust-netmap_sys
Version:        0.1.4
Release:        1%{?dist}
Summary:        Bindings to netmap - the fast packet I/O framework
License:        BSD-2-Clause
URL:            https://crates.io/crates/netmap_sys
Source0:        https://static.crates.io/crates/netmap_sys/netmap_sys-%{version}.crate
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
Summary:        Bindings to netmap - the fast packet I/O framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+netmap_with_libs-devel
Summary:        Bindings to netmap - the fast packet I/O framework
BuildArch:      noarch
%description -n %{name}+netmap_with_libs-devel

This package contains library source intended for building other packages which
use the "netmap_with_libs" feature of the "%{crate}" crate.

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
%files -n rust-netmap_sys-devel -f %{oreon_filedir}/rust-netmap_sys-devel.list

%changelog

%autochangelog
