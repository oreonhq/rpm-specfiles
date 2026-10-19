%global source0_hash 882941af9bf86e16699e5fe72c9a931a562d0fce246bbf707b54ee444355c1b4
%bcond check 0
%global crate crypto-auditing-client
Name:           rust-crypto-auditing-client
Version:        0.3.2
Release:        1%{?dist}
Summary:        Event broker client for crypto-auditing project
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/crypto-auditing-client
Source0:        https://static.crates.io/crates/crypto-auditing-client/crypto-auditing-client-%{version}.crate
Source1:	client.conf
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Event broker client for crypto-auditing project
License:        GPL-3.0-or-later AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND MIT AND (Unlicense OR MIT)
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n crypto-auditing-client -f %{oreon_filedir}/crypto-auditing-client.list

%changelog

%autochangelog
