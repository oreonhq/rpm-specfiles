%global source2_hash a0e8cff364a4d739c5bf71722e072f09ba84a80ea1fee0e3a1334e640bcccea9
%global forgeurl0 https://github.com/NetworkConfiguration/dhcpcd
Name: dhcpcd
Version: 10.5.2
Release:        1%{?dist}
Summary:        A minimalistic network configuration daemon with DHCPv4, rdisc and DHCPv6 support
License: BSD-2-Clause AND ISC AND MIT
URL: http://roy.marples.name/projects/%{name}/
VCS: git:%{forgeurl0}
Source0:        %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1: %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2: https://github.com/rsmarples.gpg
Source3: %{name}.service
Source4: %{name}@.service
Source5: systemd-sysusers.conf
Source6: systemd-tmpfiles.conf
Source7: 99-prefixlen
%{?systemd_requires}
# oreon:deps
BuildRequires:  chrony
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The dhcpcd package provides a minimalistic network configuration daemon
that supports IPv4 and IPv6 configuration including configuration discovery
through NDP, DHCPv4 and DHCPv6 protocols.

%prep
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    --dbdir=/var/lib/%{name} --runstatedir=%{_rundir}
%make_build
%check

%make_build test
%install
export BINMODE=755
%make_install
find %{buildroot} -name '*.la' -delete -print
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}@.service
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 444 %{SOURCE7} %{buildroot}%{_libexecdir}/%{name}-hooks/99-prefixlen
install -d %{buildroot}%{_sharedstatedir}/%{_name}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
