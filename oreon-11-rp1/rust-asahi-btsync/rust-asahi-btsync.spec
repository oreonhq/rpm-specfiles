%global source0_hash 3a967ee15e338cb653250a42c6a57c1d424397a03cccda725ab1dcb6de28aa51
%bcond check 0
%global crate asahi-btsync
Name:           rust-asahi-btsync
Version:        0.2.6
Release:        1%{?dist}
Summary:        Tool to sync Bluetooth pairing keys with macos on ARM Macs
License:        MIT
URL:            https://crates.io/crates/asahi-btsync
Source0:        https://static.crates.io/crates/asahi-btsync/asahi-btsync-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool to sync Bluetooth pairing keys with macos on ARM Macs
License:        MIT AND Zlib AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND Unicode-DFS-2016
Recommends:     bluez
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
install -p -m 0644 -D etc/systemd/system/asahi-btsync.service %{buildroot}%{_unitdir}/asahi-btsync.service
install -p -m 0644 -D etc/udev/rules.d/96-asahi-btsync.rules %{buildroot}%{_udevrulesdir}/96-asahi-btsync.rules
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%post -n %{crate}

%systemd_post asahi-btsync.service
%preun -n %{crate}

%systemd_preun asahi-btsync.service
%postun -n %{crate}

%systemd_postun_with_restart asahi-btsync.service
%files -f %{oreon_filedir}/main.list
%files -n asahi-btsync -f %{oreon_filedir}/asahi-btsync.list

%changelog

%autochangelog
