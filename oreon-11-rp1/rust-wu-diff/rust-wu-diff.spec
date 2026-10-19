%global source0_hash 8e3e6735fcde06432870db8dc9d7e3ab1b93727c14eaef329969426299f28893
%bcond check 1
%global debug_package %{nil}
%global crate wu-diff
Name:           rust-wu-diff
Version:        0.1.2
Release:        1%{?dist}
Summary:        Compute differences between two slices using wu(the O(NP)) algorithm
License:        MIT
URL:            https://crates.io/crates/wu-diff
Source0:        https://static.crates.io/crates/wu-diff/wu-diff-%{version}.crate
Patch:          wu-diff-fix-metadata.diff
Patch10:        wu-diff-fix-test-for-image-0.23-no-raw_pixels.diff
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
Summary:        Compute differences between two slices using wu(the O(NP)) algorithm
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
%files -n rust-wu-diff-devel -f %{oreon_filedir}/rust-wu-diff-devel.list

%changelog

%autochangelog
