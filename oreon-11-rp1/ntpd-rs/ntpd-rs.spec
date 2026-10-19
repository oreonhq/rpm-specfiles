%global source0_hash 58840fa2dfe16f64be5e450a99b27238f031b9fcb08bd9c0f42ca15cc95f5487
%bcond check 0
Name:           ntpd-rs
Version:        1.7.1
Release:        1%{?dist}
Summary:        Full-featured implementation of NTP with NTS support
SourceLicense:  Apache-2.0 OR MIT
License:        %{shrink:
    Apache-2.0 AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
URL:            https://github.com/pendulum-project/ntpd-rs
Source0:        https://github.com/pendulum-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        ntpd-rs.sysusers
Source2:        ntpd-rs.tmpfiles
Patch:          0001-Move-default-socket-path-from-var-run-to-run.patch
Patch:          0002-Fix-names-of-conflicting-systemd-services.patch
Patch:          0003-Temporarily-disable-PPS-feature.patch
Patch:          https://github.com/pendulum-project/ntpd-rs/commit/1df0cc9.patch
Requires(pre):  systemd-sysusers
Requires(pre):  systemd-tmpfiles
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
install -Dpm0755 target/rpm/ntp-ctl -t %{buildroot}/%{_bindir}
install -Dpm0755 target/rpm/ntp-daemon -t %{buildroot}/%{_bindir}
install -Dpm0755 target/rpm/ntp-metrics-exporter -t %{buildroot}/%{_bindir}
install -Dpm0644 docs/precompiled/man/*.5 -t %{buildroot}/%{_mandir}/man5
install -Dpm0644 docs/precompiled/man/*.8 -t %{buildroot}/%{_mandir}/man8
install -Dpm0644 docs/examples/conf/ntp.toml.default -t %{buildroot}/%{_pkgdocdir}/
install -Dpm0644 docs/examples/conf/ntp.toml.default %{buildroot}/%{_sysconfdir}/ntpd-rs/ntp.toml
install -Dpm0644 docs/examples/conf/ntpd-rs.service -t %{buildroot}/%{_unitdir}
install -Dpm0644 docs/examples/conf/ntpd-rs-metrics.service -t %{buildroot}/%{_unitdir}
install -Dpm0644 %{SOURCE1} %{buildroot}/%{_sysusersdir}/ntpd-rs.conf
install -Dpm0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/ntpd-rs.conf
mkdir -p %{buildroot}/%{_sharedstatedir}/ntpd-rs
mkdir -p %{buildroot}/%{_sharedstatedir}/ntpd-rs-observe
mkdir -p %{buildroot}/%{_rundir}/ntpd-rs
%oreon_autofiles main
%if %{with check}
%check

%{cargo_test -- -- --test-threads 2 %{shrink:
    --skip algorithm::kalman::peer::tests::test_offset_steering_and_measurements
    --skip hwtimestamp::tests::get_hwtimestamp
    --skip socket::tests::test_send_timestamp
    --skip daemon::ntp_source::tests::test_deny_stops_poll
    --skip daemon::ntp_source::tests::test_timeroundtrip
    --skip daemon::server::tests::test_server_serves
}}
%endif
%pre

%sysusers_create_package ntpd-rs %{SOURCE1}
%tmpfiles_create_package ntpd-rs %{SOURCE2}
%post

%systemd_post ntpd-rs.service
%preun

%systemd_preun ntpd-rs.service
%postun

%systemd_postun_with_restart ntpd-rs.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
