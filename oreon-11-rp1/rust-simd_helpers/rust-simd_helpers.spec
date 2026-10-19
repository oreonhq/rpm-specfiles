%global source0_hash 95890f873bec569a0362c235787f3aca6e1e887302ba4840839bcc6459c42da6
%bcond check 0
%global debug_package %{nil}
%global crate simd_helpers
Name:           rust-simd_helpers
Version:        0.1.0
Release:        1%{?dist}
Summary:        Helpers to write more compact simd code
License:        MIT
URL:            https://crates.io/crates/simd_helpers
Source0:        https://static.crates.io/crates/simd_helpers/simd_helpers-%{version}.crate
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
Summary:        Helpers to write more compact simd code
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
%files -n rust-simd_helpers-devel -f %{oreon_filedir}/rust-simd_helpers-devel.list

%changelog

%autochangelog
