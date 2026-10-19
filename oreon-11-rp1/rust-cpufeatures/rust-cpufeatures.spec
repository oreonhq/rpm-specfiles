%global source0_hash 5ca28b0ae3115b884660db4118d803791fd6756b6e88f39c0f3f7859060d7566
%bcond check 1
%global debug_package %{nil}
%global crate cpufeatures
Name:           rust-cpufeatures
Version:        0.3.1
Release:        1%{?dist}
Summary:        Lightweight runtime CPU feature detection for aarch64 and x86
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cpufeatures
Source0:        https://static.crates.io/crates/cpufeatures/cpufeatures-%{version}.crate
Patch:          cpufeatures-fix-metadata.diff
# oreon:deps
BuildRequires:  (crate(libc) >= 0.2.155 with crate(libc) < 0.3.1~)
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
Summary:        Lightweight runtime CPU feature detection for aarch64 and x86
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
%files -n rust-cpufeatures-devel -f %{oreon_filedir}/rust-cpufeatures-devel.list

%changelog

%autochangelog
