%global source0_hash 6782b1a817d2263875b7ba58bb0b897afdae5d3e11350f340162ad3d360c52aa
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-input
Name:           rust-ironrdp-input
Version:        0.3.0
Release:        1%{?dist}
Summary:        Utilities to manage and build RDP input packets
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-input
Source0:        https://static.crates.io/crates/ironrdp-input/ironrdp-input-%{version}.crate
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
Summary:        Utilities to manage and build RDP input packets
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
%files -n rust-ironrdp-input-devel -f %{oreon_filedir}/rust-ironrdp-input-devel.list

%changelog

%autochangelog
