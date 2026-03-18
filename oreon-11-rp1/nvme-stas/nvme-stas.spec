Name:    nvme-stas
Summary: NVMe STorage Appliance Services
Version: 2.4.1
Release: 6%{?dist}
License: Apache-2.0
URL:     https://github.com/linux-nvme/nvme-stas
Source0: %{url}/archive/v%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

BuildArch:     noarch

BuildRequires: meson >= 0.57.0
BuildRequires: glib2-devel
BuildRequires: libnvme-devel >= 1.12
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

BuildRequires: python3-devel
BuildRequires: python3-libnvme
BuildRequires: python3-dasbus
BuildRequires: python3-pyudev
BuildRequires: python3-systemd
BuildRequires: python3-gobject-devel
BuildRequires: python3-lxml

Requires:      avahi
Requires:      python3-libnvme >= 1.12
Requires:      python3-dasbus
Requires:      python3-pyudev
Requires:      python3-systemd
Requires:      python3-gobject
Requires:      python3-lxml

%description
nvme-stas is a Central Discovery Controller (CDC) client for Linux. It
handles Asynchronous Event Notifications (AEN), Automated NVMe subsystem
connection controls, Error handling and reporting, and Automatic (zeroconf)
and Manual configuration. nvme-stas is composed of two daemons:
stafd (STorage Appliance Finder) and stacd (STorage Appliance Connector).

%prep
%autosetup -p1 -n %{name}-%{version_no_tilde}

%build
%meson -Dman=true -Dhtml=true
%meson_build

%install
%meson_install
mv %{buildroot}/%{_sysconfdir}/stas/sys.conf.doc %{buildroot}/%{_sysconfdir}/stas/sys.conf

%post
%systemd_post stacd.service
%systemd_post stafd.service

%preun
%systemd_preun stacd.service
%systemd_preun stafd.service

%postun
%systemd_postun_with_restart stacd.service
%systemd_postun_with_restart stafd.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/stas
%config(noreplace) %{_sysconfdir}/stas/stacd.conf
%config(noreplace) %{_sysconfdir}/stas/stafd.conf
%config(noreplace) %{_sysconfdir}/stas/sys.conf
%{_datadir}/dbus-1/system.d/org.nvmexpress.*.conf
%{_bindir}/stacctl
%{_bindir}/stafctl
%{_bindir}/stasadm
%{_sbindir}/stacd
%{_sbindir}/stafd
%{_unitdir}/stacd.service
%{_unitdir}/stafd.service
%{_unitdir}/stas-config.target
%{_unitdir}/stas-config@.service
%dir %{python3_sitelib}/staslib
%{python3_sitelib}/staslib/*
%doc %{_pkgdocdir}/html
%{_mandir}/man1/sta*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/nvme*.7*
%{_mandir}/man8/sta*.8*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.1-6
- Prepare for Oreon 11 (RP1)
