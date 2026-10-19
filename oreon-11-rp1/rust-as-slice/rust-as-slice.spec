%global source0_hash 516b6b4f0e40d50dcda9365d53964ec74560ad4284da2e7fc97122cd83174516
%bcond check 0
%global debug_package %{nil}
%global crate as-slice
Name:           rust-as-slice
Version:        0.2.1
Release:        1%{?dist}
Summary:        `AsSlice` and `AsMutSlice` traits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/as-slice
Source0:        https://static.crates.io/crates/as-slice/as-slice-%{version}.crate
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
Summary:        `AsSlice` and `AsMutSlice` traits
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
%files -n rust-as-slice-devel -f %{oreon_filedir}/rust-as-slice-devel.list

%changelog

%autochangelog
