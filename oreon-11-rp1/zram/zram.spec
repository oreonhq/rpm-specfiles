%global source0_hash none

Name:      zram
Version:   0.4
Release:   10%{?dist}
Summary:   ZRAM for swap config and services for Fedora
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later

# No upstream as it's Fedora specific.
Source0:   COPYING
Source1:   zram.conf
Source2:   zram-swap.service
Source3:   zramstart
Source4:   zramstop

BuildArch: noarch

%{?systemd_requires}
BuildRequires: systemd
Requires: util-linux gawk grep

%description
ZRAM is a Linux block device that can be used for compressed swap in memory.
It's useful in memory constrained devices. This provides a service to setup
ZRAM as a swap device based on criteria such as available memory.

%prep
# None required

%build
# None required

%install
install -d %{buildroot}%{_datadir}/licenses/%{name}/
install -pm 0644 %{SOURCE0} %{buildroot}%{_datadir}/licenses/%{name}/COPYING

install -d %{buildroot}%{_sysconfdir}/
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/

install -d %{buildroot}%{_unitdir}/
install -pm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/

install -d %{buildroot}%{_sbindir}
install -pm 0755 %{SOURCE3} %{buildroot}%{_sbindir}
install -pm 0755 %{SOURCE4} %{buildroot}%{_sbindir}

%postun
%systemd_postun zram-swap.service

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/zram-swap.service
%{_sbindir}/zramstart
%{_sbindir}/zramstop

%changelog
%autochangelog
