%global source0_hash e9a75ae9fea4a9cafa5d6e93646c4d9a3d74699a2abf77f876595ff60d5b5c94
%bcond check 1
%global crate crypto-auditing-agent
Name:           rust-crypto-auditing-agent
Version:        0.3.2
Release:        1%{?dist}
Summary:        Event collector agent for crypto-auditing project
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/crypto-auditing-agent
Source0:        https://static.crates.io/crates/crypto-auditing-agent/crypto-auditing-agent-%{version}.crate
Source1:        agent.conf
Source2:        crypto-auditing-agent.service
Source3:	crypto-auditing.sysusers
Patch:		rust-crypto-auditing-agent-0.2.4-no-probe.patch
%{?sysusers_requires_compat}
ExcludeArch: i386 i686
# oreon:deps
BuildRequires:  bpftool
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  kernel-devel
BuildRequires:  libbpf-devel
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Event collector agent for crypto-auditing project
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (LGPL-2.1-only OR BSD-2-Clause) AND (Unlicense OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p2
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
mkdir -p $RPM_BUILD_ROOT%{_sysusersdir}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysusersdir}/crypto-auditing.conf
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/crypto-auditing
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%pre -n %{crate}

%sysusers_create_compat %{SOURCE3}
%post -n %{crate}

%systemd_post crypto-auditing-agent.service
%preun -n %{crate}

%systemd_preun crypto-auditing-agent.service
%postun -n %{crate}

%systemd_postun_with_restart crypto-auditing-agent.service
%files -f %{oreon_filedir}/main.list
%files -n crypto-auditing-agent -f %{oreon_filedir}/crypto-auditing-agent.list

%changelog

%autochangelog
