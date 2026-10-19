%global source0_hash 1727b3130294e88369c7aaed58a0c2a0666376edc3376157468e667e767b7ea6
%bcond check 0
%global debug_package %{nil}
%global crate rd-hashd-intf
Name:           rust-rd-hashd-intf
Version:        2.2.5
Release:        1%{?dist}
Summary:        Latency-sensitive pseudo workload for resctl-demo (interface library)
License:        Apache-2.0
URL:            https://crates.io/crates/rd-hashd-intf
Source0:        https://static.crates.io/crates/rd-hashd-intf/rd-hashd-intf-%{version}.crate
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
Summary:        Latency-sensitive pseudo workload for resctl-demo (interface library)
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
%files -n rust-rd-hashd-intf-devel -f %{oreon_filedir}/rust-rd-hashd-intf-devel.list

%changelog

%autochangelog
