%global source0_hash 5d6fa99d535dd930d1249e6c79cb3c2915f9172a540fe2b02a4c8f9ca954721e
%bcond check 1
%global debug_package %{nil}
%global crate prometheus-client
Name:           rust-prometheus-client
Version:        0.19.0
Release:        1%{?dist}
Summary:        Open Metrics client library allowing users to natively instrument applications
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/prometheus-client
Source0:        https://static.crates.io/crates/prometheus-client/prometheus-client-%{version}.crate
Patch:          prometheus-client-fix-metadata.diff
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
Summary:        Open Metrics client library allowing users to natively instrument applications
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
%files -n rust-prometheus-client-devel -f %{oreon_filedir}/rust-prometheus-client-devel.list

%changelog

%autochangelog
