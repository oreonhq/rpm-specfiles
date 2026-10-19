%global source0_hash 7e31d442c16f047a671b5a71e2161d6e68814012b7f5379d269ebd915fac2729
%bcond check 0
%global debug_package %{nil}
%global crate signal-hook
Name:           rust-signal-hook0.1
Version:        0.1.17
Release:        1%{?dist}
Summary:        Unix signal handling
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/signal-hook
Source0:        https://static.crates.io/crates/signal-hook/signal-hook-%{version}.crate
Patch:          signal-hook-fix-metadata.diff
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
Summary:        Unix signal handling
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
%files -n rust-signal-hook0.1-devel -f %{oreon_filedir}/rust-signal-hook0.1-devel.list

%changelog

%autochangelog
