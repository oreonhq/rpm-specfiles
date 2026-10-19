%global source0_hash 17367f0cc86f2d25802b2c26ee58a7b23faeccf78a396094c13dced0d0182526
%bcond check 0
%global debug_package %{nil}
%global crate phf_generator
Name:           rust-phf_generator0.8
Version:        0.8.0
Release:        1%{?dist}
Summary:        PHF generation logic
License:        MIT
URL:            https://crates.io/crates/phf_generator
Source0:        https://static.crates.io/crates/phf_generator/phf_generator-%{version}.crate
Patch:          phf_generator-fix-metadata.diff
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
Summary:        PHF generation logic
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
%files -n rust-phf_generator0.8-devel -f %{oreon_filedir}/rust-phf_generator0.8-devel.list

%changelog

%autochangelog
