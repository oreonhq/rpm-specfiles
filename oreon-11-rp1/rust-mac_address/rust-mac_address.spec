%global source0_hash c0aeb26bf5e836cc1c341c8106051b573f1766dfa05aa87f0b98be5e51b02303
%bcond check 1
%global debug_package %{nil}
%global crate mac_address
Name:           rust-mac_address
Version:        1.1.8
Release:        1%{?dist}
Summary:        Cross-platform retrieval of a network interface MAC address
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mac_address
Source0:        https://static.crates.io/crates/mac_address/mac_address-%{version}.crate
Patch:          mac_address-fix-metadata-auto.diff
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
Summary:        Cross-platform retrieval of a network interface MAC address
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Cross-platform retrieval of a network interface MAC address
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
%files -n rust-mac_address-devel -f %{oreon_filedir}/rust-mac_address-devel.list

%changelog

%autochangelog
