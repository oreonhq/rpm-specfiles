%global source0_hash 4c203737164e9734db8fb03921a35917a5775ce5721f920dbcadd8bd4f98f673
%bcond check 0
%global debug_package %{nil}
%global crate lv2-time
Name:           rust-lv2-time
Version:        0.1.3
Release:        1%{?dist}
Summary:        Rust-lv2's wrapper of LV2's time types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2-time
Source0:        https://static.crates.io/crates/lv2-time/lv2-time-%{version}.crate
ExcludeArch:    ppc64le s390x
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
Summary:        Rust-lv2's wrapper of LV2's time types
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
%files -n rust-lv2-time-devel -f %{oreon_filedir}/rust-lv2-time-devel.list

%changelog

%autochangelog
