%global source0_hash 50a0e551c1e27e1731aba276dbeaeac73f53c7cd34d1bda485d02bd1e0f36844
%bcond check 0
%global debug_package %{nil}
%global crate rtoolbox
Name:           rust-rtoolbox
Version:        0.0.5
Release:        1%{?dist}
Summary:        Utility functions for other crates, no backwards compatibility guaran...
License:        Apache-2.0
URL:            https://crates.io/crates/rtoolbox
Source0:        https://static.crates.io/crates/rtoolbox/rtoolbox-%{version}.crate
Patch:          rtoolbox-fix-metadata-auto.diff
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

%package     -n %{name}+serde-devel
Summary:        Utility functions for other crates, no backwards compatibility guaran...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-rtoolbox-devel -f %{oreon_filedir}/rust-rtoolbox-devel.list

%changelog

%autochangelog
