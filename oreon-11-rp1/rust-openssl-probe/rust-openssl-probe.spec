%global source0_hash 7c87def4c32ab89d880effc9e097653c8da5d6ef28e6b539d313baaacfbafcbe
%bcond check 0
%global debug_package %{nil}
%global crate openssl-probe
Name:           rust-openssl-probe
Version:        0.2.1
Release:        2%{?dist}
Summary:        Tool for helping to find SSL certificate locations on the system for...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openssl-probe
Source0:        https://static.crates.io/crates/openssl-probe/openssl-probe-%{version}.crate
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
Summary:        Tool for helping to find SSL certificate locations on the system for...
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
%files -n rust-openssl-probe-devel -f %{oreon_filedir}/rust-openssl-probe-devel.list

%changelog

%autochangelog
