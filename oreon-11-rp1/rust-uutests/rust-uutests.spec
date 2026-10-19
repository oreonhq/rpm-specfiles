%global source10_hash 29953405eaa3dcc41c37d1621d55b6a47eee93e05613e439e73295029740b10c
%global source0_hash 25b8a1598ddd20230a5df59d642e2e5741b0b90038bde8684c984515f947fda5
%bcond check 1
%global debug_package %{nil}
%global crate uutests
Name:           rust-uutests
Version:        0.7.0
Release:        1%{?dist}
Summary:        Uutils ~ 'core' uutils test library (cross-platform)
License:        MIT
URL:            https://crates.io/crates/uutests
Source0:        https://static.crates.io/crates/uutests/uutests-%{version}.crate
Source10:       https://raw.githubusercontent.com/uutils/coreutils/refs/tags/0.7.0/LICENSE
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
Summary:        Uutils ~ 'core' uutils test library (cross-platform)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE10} .
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
%files -n rust-uutests-devel -f %{oreon_filedir}/rust-uutests-devel.list

%changelog

%autochangelog
