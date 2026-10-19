%global source0_hash 1e061d1b48cb8d38042de4ae0a7a6401009d6143dc80d2e2d6f31f0bdd6470c7
%bcond check 0
%global debug_package %{nil}
%global crate resolv-conf
Name:           rust-resolv-conf
Version:        0.7.6
Release:        1%{?dist}
Summary:        The resolv.conf file parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/resolv-conf
Source0:        https://static.crates.io/crates/resolv-conf/resolv-conf-%{version}.crate
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

%package     -n %{name}+system-devel
Summary:        The resolv.conf file parser
BuildArch:      noarch
%description -n %{name}+system-devel

This package contains library source intended for building other packages which
use the "system" feature of the "%{crate}" crate.

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
%files -n rust-resolv-conf-devel -f %{oreon_filedir}/rust-resolv-conf-devel.list

%changelog

%autochangelog
