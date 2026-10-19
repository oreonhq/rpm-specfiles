%global source0_hash 996ce95bbdb0203e5b91d4a0c9b81c0d67d11c80f884482a0c1ea19e732e3530
%bcond check 0
%global debug_package %{nil}
%global crate av-metrics
Name:           rust-av-metrics
Version:        0.9.1
Release:        1%{?dist}
Summary:        A collection of algorithms for measuring audio/video metrics
License:        MIT
URL:            https://crates.io/crates/av-metrics
Source0:        https://static.crates.io/crates/av-metrics/av-metrics-%{version}.crate
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

%package     -n %{name}+serde-devel
Summary:        A collection of algorithms for measuring audio/video metrics
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-av-metrics-devel -f %{oreon_filedir}/rust-av-metrics-devel.list

%changelog

%autochangelog
