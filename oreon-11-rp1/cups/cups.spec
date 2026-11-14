# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ab4d9cd7f3e58060091d2b24972223d6401675f11c49b65abf4f6ef31dea22ff

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global cupslibdir %{_prefix}/lib/cups

Name:           cups
Epoch:          1
Version:        2.4.20
Release:        1%{?dist}
Summary:        CUPS printing system
License:        Apache-2.0 WITH LLVM-exception
URL:            https://openprinting.github.io/cups/
Source0:        https://github.com/OpenPrinting/cups/releases/download/v%{version}/cups-%{version}-source.tar.gz
Source1:        cups-2.4.20-source.tar.gz.sig
Source2:        gpgkey-7082A0A50A2E92640F3880E0E4522DCC9B246FF7.gpg
Source3:        cups-lpd.socket
Source4:        cups-lpd@.service
Source5:        cups-tmpfiles.conf

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  pam-devel
BuildRequires:  libacl-devel
BuildRequires:  krb5-devel
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(zlib)

%{?systemd_ordering}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-filesystem = %{epoch}:%{version}-%{release}
Requires:       dbus
Requires:       pam
Requires(pre):  setup
Provides:       cups-client = %{epoch}:%{version}-%{release}
Provides:       lpd
Provides:       lpr

%description
CUPS is the standards-based, open source printing system developed by
Apple Inc. and maintained by OpenPrinting for macOS and other UNIX-like
operating systems. It uses the Internet Printing Protocol (IPP) and
provides System V and Berkeley command-line interfaces.

%package        filesystem
Summary:        CUPS directory layout
BuildArch:      noarch

%description    filesystem
This package owns the directories shared between CUPS and the packages
that install filters, backends, drivers and PPD files for it.

%package        libs
Summary:        CUPS shared libraries
Requires:       %{name}-filesystem = %{epoch}:%{version}-%{release}

%description    libs
The CUPS printing system provides a portable printing layer for UNIX
operating systems. This package contains the CUPS shared libraries.

%package        devel
Summary:        CUPS development environment
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       gnutls-devel
Requires:       zlib-devel
Requires:       krb5-devel

%description    devel
This package provides the CUPS headers and development environment.

%package        ipptool
Summary:        Tool for performing IPP requests
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-filesystem = %{epoch}:%{version}-%{release}

%description    ipptool
Sends IPP requests to the specified URI and tests and/or displays the
results. It also contains the IPP test files shipped by CUPS and ippfind
for locating IPP printers.

%package        lpd
Summary:        CUPS LPD support
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    lpd
This package provides support for accepting print jobs from legacy LPD
clients through the cups-lpd helper.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n cups-%{version} -p1

%build
%configure \
    --disable-static \
    --enable-relro \
    --enable-dbus \
    --enable-libusb \
    --enable-acl \
    --enable-gssapi \
    --enable-webif \
    --enable-unit-tests \
    --with-tls=gnutls \
    --with-dnssd=avahi \
    --with-systemd=%{_unitdir} \
    --with-rcdir=no \
    --with-xinetd=no \
    --with-cups-user=lp \
    --with-cups-group=lp \
    --with-system-groups=wheel \
    --with-printcap=%{_sysconfdir}/printcap \
    --with-cachedir=%{_localstatedir}/cache/cups \
    --with-logdir=%{_localstatedir}/log/cups \
    --with-rundir=/run/cups \
    --with-docdir=%{_datadir}/cups/doc-root
%make_build

%install
make BUILDROOT=%{buildroot} install
rm -rf %{buildroot}/run
rm -f %{buildroot}%{_libdir}/*.a
mkdir -p %{buildroot}%{_datadir}/cups/banners
mkdir -p %{buildroot}%{_datadir}/cups/data
mkdir -p %{buildroot}%{_datadir}/cups/model
mkdir -p %{buildroot}%{cupslibdir}/driver
mkdir -p %{buildroot}%{_localstatedir}/cache/cups/rss
mkdir -p %{buildroot}%{_localstatedir}/log/cups
mkdir -p %{buildroot}%{_localstatedir}/spool/cups/tmp
install -Dpm0644 %{SOURCE3} %{buildroot}%{_unitdir}/cups-lpd.socket
install -Dpm0644 %{SOURCE4} %{buildroot}%{_unitdir}/cups-lpd@.service
install -Dpm0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/cups.conf

%check
make check

%post
%systemd_post cups.service cups.socket cups.path
systemd-tmpfiles --create %{_tmpfilesdir}/cups.conf 2>/dev/null || :

%preun
%systemd_preun cups.service cups.socket cups.path

%postun
%systemd_postun_with_restart cups.service cups.socket cups.path

%ldconfig_scriptlets libs

%files
%license LICENSE NOTICE
%doc README.md CHANGES.md CREDITS.md
%config(noreplace) %{_sysconfdir}/cups/*.conf
%{_sysconfdir}/cups/*.default
%dir %{_sysconfdir}/cups/ppd
%dir %attr(0700,root,root) %{_sysconfdir}/cups/ssl
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/cups.conf
%config(noreplace) %{_sysconfdir}/pam.d/cups
%{_unitdir}/cups.service
%{_unitdir}/cups.socket
%{_unitdir}/cups.path
%{_tmpfilesdir}/cups.conf
%{_bindir}/cancel
%{_bindir}/cupstestppd
%{_bindir}/ippeveprinter
%{_bindir}/lp
%{_bindir}/lpoptions
%{_bindir}/lpq
%{_bindir}/lpr
%{_bindir}/lprm
%{_bindir}/lpstat
%{_sbindir}/*
%{cupslibdir}/backend/*
%{cupslibdir}/cgi-bin
%{cupslibdir}/command
%{cupslibdir}/daemon/cups-deviced
%{cupslibdir}/daemon/cups-driverd
%{cupslibdir}/daemon/cups-exec
%{cupslibdir}/filter/*
%{cupslibdir}/monitor
%{cupslibdir}/notifier
%{_datadir}/cups/banners
%{_datadir}/cups/data
%{_datadir}/cups/doc-root
%{_datadir}/cups/drv/*
%{_datadir}/cups/mime/*
%{_datadir}/cups/ppdc/*
%{_datadir}/cups/templates
%{_datadir}/cups/usb
%{_datadir}/applications/cups.desktop
%{_datadir}/icons/hicolor/*/apps/cups.png
%{_datadir}/icons/hicolor/*/apps/cups.svg
%{_datadir}/locale/*/cups_*.po
%{_mandir}/man1/cancel.1*
%{_mandir}/man1/cups.1*
%{_mandir}/man1/cupstestppd.1*
%{_mandir}/man1/ippeveprinter.1*
%{_mandir}/man1/lp.1*
%{_mandir}/man1/lpoptions.1*
%{_mandir}/man1/lpq.1*
%{_mandir}/man1/lpr.1*
%{_mandir}/man1/lprm.1*
%{_mandir}/man1/lpstat.1*
%{_mandir}/man5/*.conf.5*
%{_mandir}/man5/cupsd-logs.5*
%{_mandir}/man5/mime.*.5*
%{_mandir}/man7/ippevepcl.7*
%{_mandir}/man7/ippeveps.7*
%{_mandir}/man8/*
%exclude %{_mandir}/man8/cups-lpd.8*
%ghost %dir /run/cups
%ghost %dir /run/cups/certs
%dir %attr(0755,root,lp) %{_localstatedir}/cache/cups
%dir %attr(0775,root,lp) %{_localstatedir}/cache/cups/rss
%dir %attr(0755,root,lp) %{_localstatedir}/log/cups
%dir %attr(0710,root,lp) %{_localstatedir}/spool/cups
%dir %attr(1770,root,lp) %{_localstatedir}/spool/cups/tmp

%files filesystem
%dir %{_sysconfdir}/cups
%dir %{cupslibdir}
%dir %{cupslibdir}/backend
%dir %{cupslibdir}/daemon
%dir %{cupslibdir}/driver
%dir %{cupslibdir}/filter
%dir %{_datadir}/cups
%dir %{_datadir}/cups/drv
%dir %{_datadir}/cups/mime
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/ppdc

%files libs
%license LICENSE NOTICE
%{_libdir}/libcups.so.2
%{_libdir}/libcupsimage.so.2

%files devel
%{_bindir}/cups-config
%{_bindir}/ppd*
%{_includedir}/cups/
%{_libdir}/libcups.so
%{_libdir}/libcupsimage.so
%{_libdir}/pkgconfig/cups.pc
%{_datadir}/cups/examples
%{_mandir}/man1/cups-config.1*
%{_mandir}/man1/ppd*.1*
%{_mandir}/man5/ppdcfile.5*
%{_mandir}/man7/backend.7*

%files ipptool
%{_bindir}/ipptool
%{_bindir}/ippfind
%{_datadir}/cups/ipptool
%{_mandir}/man1/ipptool.1*
%{_mandir}/man1/ippfind.1*
%{_mandir}/man5/ipptoolfile.5*

%files lpd
%{cupslibdir}/daemon/cups-lpd
%{_unitdir}/cups-lpd.socket
%{_unitdir}/cups-lpd@.service
%{_mandir}/man8/cups-lpd.8*

%changelog
%autochangelog
