%global source0_hash 60ec7a62135e5134172e48cdc4a0e5499d357d65c1ee4f3442d51e05e3f71d7c
%bcond check 0
%global debug_package %{nil}
%global crate version-track
Name:           rust-version-track
Version:        1.0.0
Release:        1%{?dist}
Summary:        Library used to track changes to complex data
License:        ISC
URL:            https://crates.io/crates/version-track
Source0:        https://static.crates.io/crates/version-track/version-track-%{version}.crate
Patch:          version-track-fix-metadata.diff
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
Summary:        Library used to track changes to complex data
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
%files -n rust-version-track-devel -f %{oreon_filedir}/rust-version-track-devel.list

%changelog

%autochangelog
