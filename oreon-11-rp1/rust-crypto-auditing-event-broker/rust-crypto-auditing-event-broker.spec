%global source0_hash c726f4f6f5087fb435c87d37a1b79bd2c8656760450aa95006c96a5aae3b4ca1
%bcond check 1
%global crate crypto-auditing-event-broker
Name:           rust-crypto-auditing-event-broker
Version:        0.3.2
Release:        1%{?dist}
Summary:        Event broker for crypto-auditing project
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/crypto-auditing-event-broker
Source0:        https://static.crates.io/crates/crypto-auditing-event-broker/crypto-auditing-event-broker-%{version}.crate
Source1:        event-broker.conf
Source2:        crypto-auditing-event-broker.service
Source3:        crypto-auditing-event-broker.socket
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Event broker for crypto-auditing project
License:        GPL-3.0-or-later AND (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND BSD-3-Clause AND ISC AND MIT AND (Unlicense OR MIT)
Requires:       crypto-auditing-agent
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
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/crypto-auditing
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/crypto-auditing
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- -- --skip test_event_broker
%endif
%post -n %{crate}

%systemd_post crypto-auditing-event-broker.service
%preun -n %{crate}

%systemd_preun crypto-auditing-event-broker.service
%postun -n %{crate}

%systemd_postun_with_restart crypto-auditing-event-broker.service
%files -f %{oreon_filedir}/main.list
%files -n crypto-auditing-event-broker -f %{oreon_filedir}/crypto-auditing-event-broker.list

%changelog

%autochangelog
