%global source0_hash cf32d263c5d5cc2a23ce587097f5ddafdb188492ba2e6fb638eaccdc22453631
%bcond check 1
%global debug_package %{nil}
%global crate grep-cli
Name:           rust-grep-cli
Version:        0.1.12
Release:        1%{?dist}
Summary:        Utilities for search oriented command line applications
License:        Unlicense OR MIT
URL:            https://crates.io/crates/grep-cli
Source0:        https://static.crates.io/crates/grep-cli/grep-cli-%{version}.crate
Patch:          grep-cli-fix-metadata-auto.diff
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
Summary:        Utilities for search oriented command line applications
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
%files -n rust-grep-cli-devel -f %{oreon_filedir}/rust-grep-cli-devel.list

%changelog

%autochangelog
