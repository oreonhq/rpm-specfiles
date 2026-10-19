%global source0_hash b0b54e23f056992a7e63360e7ab962328956a06ba01013afc245874b1ee986d0
%bcond check 0
%global crate asahi-wifisync
Name:           rust-asahi-wifisync
Version:        0.2.2
Release:        1%{?dist}
Summary:        Tool to sync Wifi passwords with macos on ARM Macs
License:        MIT
URL:            https://crates.io/crates/asahi-wifisync
Source0:        https://static.crates.io/crates/asahi-wifisync/asahi-wifisync-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool to sync Wifi passwords with macos on ARM Macs
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
%files -n asahi-wifisync -f %{oreon_filedir}/asahi-wifisync.list

%changelog

%autochangelog
