%global source0_hash dc80eff56f2dc5c8224b8d56b8814f765858f5485db35b76805eeb820b39c211
%bcond check 0
%global crate asahi-nvram
Name:           rust-asahi-nvram
Version:        0.2.3
Release:        1%{?dist}
Summary:        Tool to read and write nvram variables on ARM Macs
License:        MIT
URL:            https://crates.io/crates/asahi-nvram
Source0:        https://static.crates.io/crates/asahi-nvram/asahi-nvram-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool to read and write nvram variables on ARM Macs
License:        MIT AND Zlib AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n asahi-nvram -f %{oreon_filedir}/asahi-nvram.list

%changelog

%autochangelog
