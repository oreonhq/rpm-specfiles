%global source0_hash 59ed5838eebb26a2bb2e58f6d5b5316989ae9d08bab10e0e6d103e656d1b0280
%bcond check 0
%global debug_package %{nil}
%global crate cpufeatures
Name:           rust-cpufeatures0.2
Version:        0.2.17
Release:        1%{?dist}
Summary:        Lightweight runtime CPU feature detection for aarch64, loongarch64, a...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cpufeatures
Source0:        https://static.crates.io/crates/cpufeatures/cpufeatures-%{version}.crate
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
Summary:        Lightweight runtime CPU feature detection for aarch64, loongarch64, a...
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
%files -n rust-cpufeatures0.2-devel -f %{oreon_filedir}/rust-cpufeatures0.2-devel.list

%changelog

%autochangelog
