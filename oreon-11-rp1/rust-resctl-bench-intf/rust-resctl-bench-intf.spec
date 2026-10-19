%global source0_hash 323032792f63513ede99f0194008db7618cc79cb19ad8369c8b09f6cfaa9cddb
%bcond check 0
%global debug_package %{nil}
%global crate resctl-bench-intf
Name:           rust-resctl-bench-intf
Version:        2.2.5
Release:        1%{?dist}
Summary:        Whole system resource control benchmarks with realistic scenarios
License:        Apache-2.0
URL:            https://crates.io/crates/resctl-bench-intf
Source0:        https://static.crates.io/crates/resctl-bench-intf/resctl-bench-intf-%{version}.crate
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
Summary:        Whole system resource control benchmarks with realistic scenarios
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
%files -n rust-resctl-bench-intf-devel -f %{oreon_filedir}/rust-resctl-bench-intf-devel.list

%changelog

%autochangelog
