%global source0_hash aeb62e0959d5a1bebc965f4d15d9e2b7cea002b6b0f5ba8cde6cc26738467100
%bcond check 0
%global debug_package %{nil}
%global crate phf_generator
Name:           rust-phf_generator
Version:        0.14.0
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
%files -n rust-phf_generator-devel -f %{oreon_filedir}/rust-phf_generator-devel.list

%changelog

%autochangelog
