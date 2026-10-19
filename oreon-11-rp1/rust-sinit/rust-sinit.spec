%global source0_hash 81b29f588822880371213aec1da87a4b0c042599a0fd813ae8ccf7f9c4fb6a85
%bcond check 0
%global crate sinit
Name:           rust-sinit
Version:        0.1.2
Release:        1%{?dist}
Summary:        Simple init system for use in containers
License:        BSD-2-Clause
URL:            https://crates.io/crates/sinit
Source0:        https://static.crates.io/crates/sinit/sinit-%{version}.crate
ExclusiveArch:  %{rust_arches}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Simple init system for use in containers
License:        BSD-2-Clause and (MIT or Apache-2.0)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sinit -f %{oreon_filedir}/sinit.list

%changelog

%autochangelog
