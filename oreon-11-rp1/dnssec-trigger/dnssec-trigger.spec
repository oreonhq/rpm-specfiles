%global source1_hash 18ae1d5e9443ff1f227489e478e490cd58dd1d92bfe22ec899b919eaad2f103d
%global source0_hash c02519ca689014b219cf9a708494bcddbf6fff2cb48304943139750308462281
%global _hardened_build 1
Summary:        Tool for dynamic reconfiguration of validating resolver Unbound
Name: dnssec-trigger
Version: 0.17
Release:        1%{?dist}
License: BSD-3-clause AND MIT AND ISC
Url: https://www.nlnetlabs.nl/projects/dnssec-trigger/
%if 0%{?snapshot:1}
Source0:        https://www.nlnetlabs.nl/downloads/dnssec-trigger/%{name}-%{version}.tar.gz
%else
Source1:        https://www.nlnetlabs.nl/downloads/dnssec-trigger/%{name}-%{version}.tar.gz.asc
Source2:        wouter.asc
%endif
Source3: dnssec-trigger.tmpfiles.d
Source6: ssh_config.conf
Patch1: dnssec-trigger-config-workstation.patch
Patch2: dnssec-trigger-config-default.patch
Patch3: 0003-Move-the-NetworkManager-dispatcher-script-out-of-etc.patch
Patch4: 0004-Add-options-edns0-and-trust-ad.patch
Patch5: dnssec-trigger-configure-c99.patch
Patch6: dnssec-trigger-0.17-allowed-characters.patch
Patch7: dnssec-trigger-0.17-openssl-3.2.patch
Patch8: dnssec-trigger-0.17-server-recipe.patch
Obsoletes: %{name} < 0.12-22
Suggests: %{name}-panel
Requires: NetworkManager >= 0.9.9.0-40
Requires: ldns >= 1.6.10, NetworkManager-libnm, unbound
Requires: openssl
Requires: e2fsprogs
%{?systemd_ordering}
Provides: variant_config(Workstation)
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  ldns-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
dnssec-trigger reconfigures the local Unbound DNS server. Unbound is a
resolver performing DNSSEC validation. dnssec-trigger is a set of daemon
and script. On every network configuration change dnssec-trigger performs
set of tests and configures Unbound based on the current NetworkManager
configuration, its own configuration and results of performed tests.

%package panel
Summary: Applet for interaction between the user and dnssec-trigger
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name} < 0.12-22
Requires: xdg-utils
BuildRequires: gtk2-devel, desktop-file-utils
BuildRequires: make
%description panel
This package provides the GTK panel for interaction between the user
and dnssec-trigger daemon. It is able to show the current state and
results of probing performed by dnssec-trigger daemon. Also in case
some user input is needed, the panel creates a dialog window.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup %{?snapshot:-n %{name}-%{version}_%{snapshot}} -N
%autopatch -m 3 -p1

# don't use DNSSEC for forward zones for now
sed -i "s/validate_connection_provided_zones=yes/validate_connection_provided_zones=no/" dnssec.conf

%build

%configure  \
    --with-keydir=%{_sysconfdir}/dnssec-trigger \
    --with-hooks=networkmanager \
    --with-python=%{__python3} \
    --with-pidfile=%{_rundir}/%{name}d.pid \
    --with-login-command=%{_bindir}/xdg-open \
    --with-login-location="http://hotspot-nocache.fedoraproject.org/"
%make_build
%autopatch -p1 2
cp -p example.conf dnssec-trigger-workstation.conf
%autopatch -p1 1
%install
install -d -m 0755 %{buildroot}%{_libexecdir}
%make_install
install -d 0755 %{buildroot}%{_unitdir}
install -p -m 0644 example.conf %{buildroot}%{_sysconfdir}/%{name}/dnssec-trigger-default.conf
install -p -m 0644 dnssec-trigger-workstation.conf %{buildroot}%{_sysconfdir}/%{name}/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications dnssec-trigger-panel.desktop
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}
ln -s dnssec-trigger-panel %{buildroot}%{_bindir}/dnssec-trigger
for all in dnssec-trigger-control dnssec-trigger-control-setup dnssec-triggerd; do
    ln -s dnssec-trigger.8 %{buildroot}/%{_mandir}/man8/"$all".8
done
ln -s dnssec-trigger.8 %{buildroot}/%{_mandir}/man8/dnssec-trigger.conf.8
install -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/ssh_config.d
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/ssh/ssh_config.d/10-%{name}.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}d.service
%preun

%systemd_preun %{name}d.service
%postun

%systemd_postun_with_restart %{name}d.service
%posttrans

if [ ! -e %{_sysconfdir}/%{name}/dnssec-trigger.conf ]; then
    . /etc/os-release || :
    case "$VARIANT_ID" in
        workstation)
            ln -sf %{name}-workstation.conf %{_sysconfdir}/%{name}/dnssec-trigger.conf || :
            ;;
        *)
            ln -sf %{name}-default.conf %{_sysconfdir}/%{name}/dnssec-trigger.conf || :
            ;;
        esac
fi
%files -f %{oreon_filedir}/main.list
%files -n dnssec-trigger-panel -f %{oreon_filedir}/dnssec-trigger-panel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17-1
- Prepare for Oreon 11 (RP1)
