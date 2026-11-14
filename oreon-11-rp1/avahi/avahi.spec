# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5b0a9d88110b0fc8aaafc5cc0a26e83e7d2a4aca3a36bc27c9b626db7ead27b0
%global upstream_version 0.9-rc5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           avahi
Version:        0.9~rc5
Release:        1%{?dist}
Summary:        Local network service discovery
License:        LGPL-2.1-or-later
URL:            https://avahi.org
Source0:        https://github.com/avahi/avahi/archive/v%{upstream_version}/avahi-%{upstream_version}.tar.gz
Source1:        avahi-sysusers.conf

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  perl-interpreter
BuildRequires:  xmltoman
BuildRequires:  systemd
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  gdbm-devel
BuildRequires:  libcap-devel
BuildRequires:  gobject-introspection-devel

%{?systemd_ordering}
%{?sysusers_requires_compat}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       dbus

%description
Avahi is a system which facilitates service discovery on a local network.
This means that you can plug your laptop or computer into a network and
instantly be able to see other people who you can chat with, find printers
to print to or find files being shared. This kind of technology is already
found in Mac OS X (branded Rendezvous, Bonjour and sometimes Zeroconf) and
is very convenient.

%package        libs
Summary:        Libraries for avahi run-time use

%description    libs
The avahi-libs package contains the libraries needed to run programs that
use avahi.

%package        devel
Summary:        Libraries and header files for avahi development
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The avahi-devel package contains the header files and libraries necessary
for developing programs using avahi.

%package        glib
Summary:        Glib integration for avahi
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    glib
Libraries for easy use of avahi from glib applications.

%package        glib-devel
Summary:        Libraries and header files for avahi glib development
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-glib%{?_isa} = %{version}-%{release}
Requires:       glib2-devel

%description    glib-devel
The avahi-glib-devel package contains the header files and libraries
necessary for developing programs using avahi with glib.

%package        gobject
Summary:        GObject wrapper for avahi
Requires:       %{name}-glib%{?_isa} = %{version}-%{release}

%description    gobject
This library contains a GObject wrapper for the Avahi API.

%package        gobject-devel
Summary:        Libraries and header files for avahi GObject development
Requires:       %{name}-gobject%{?_isa} = %{version}-%{release}
Requires:       %{name}-glib-devel%{?_isa} = %{version}-%{release}

%description    gobject-devel
The avahi-gobject-devel package contains the header files and libraries
necessary for developing programs using avahi with GObject.

%package        tools
Summary:        Command line tools for mDNS browsing and publishing
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    tools
Command line tools that use avahi to browse and publish mDNS services.

%package        autoipd
Summary:        Link-local IPv4 address automatic configuration daemon (IPv4LL)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    autoipd
avahi-autoipd implements IPv4LL, "Dynamic Configuration of IPv4 Link-Local
Addresses" (IETF RFC3927), a protocol for automatic IP address configuration
from the link-local 169.254.0.0/16 range without the need for a central
server.

%package        dnsconfd
Summary:        Avahi DNS configuration daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    dnsconfd
avahi-dnsconfd connects to a running avahi-daemon and runs the script
/etc/avahi/avahi-dnsconfd.action for each unicast DNS server that is
announced on the local LAN.

%package        compat-libdns_sd
Summary:        Libraries for Apple Bonjour mDNSResponder compatibility
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    compat-libdns_sd
Libraries for Apple Bonjour mDNSResponder compatibility.

%package        compat-libdns_sd-devel
Summary:        Header files for the Apple Bonjour mDNSResponder compatibility libraries
Requires:       %{name}-compat-libdns_sd%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(libdns_sd) = %{version}

%description    compat-libdns_sd-devel
Header files for the Apple Bonjour mDNSResponder compatibility libraries.

%prep
%oreon_sha256
%autosetup -n avahi-%{upstream_version}

%build
NOCONFIGURE=1 autoreconf -fiv
%configure \
    --disable-static \
    --disable-silent-rules \
    --disable-qt3 \
    --disable-qt4 \
    --disable-qt5 \
    --disable-gtk \
    --disable-gtk3 \
    --disable-mono \
    --disable-monodoc \
    --disable-python \
    --disable-pygobject \
    --disable-python-dbus \
    --disable-compat-howl \
    --enable-compat-libdns_sd \
    --enable-introspection=yes \
    --enable-libevent \
    --enable-tests \
    --with-distro=none \
    --with-avahi-priv-access-group=avahi \
    --with-systemdsystemunitdir=%{_unitdir}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print
rm -rf %{buildroot}%{_localstatedir}/run
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/avahi.conf
mkdir -p %{buildroot}%{_localstatedir}/lib/avahi-autoipd
ln -s avahi-compat-libdns_sd/dns_sd.h %{buildroot}%{_includedir}/dns_sd.h
%find_lang %{name}

%check
make check

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post avahi-daemon.socket avahi-daemon.service

%preun
%systemd_preun avahi-daemon.socket avahi-daemon.service

%postun
%systemd_postun_with_restart avahi-daemon.socket avahi-daemon.service

%post dnsconfd
%systemd_post avahi-dnsconfd.service

%preun dnsconfd
%systemd_preun avahi-dnsconfd.service

%postun dnsconfd
%systemd_postun_with_restart avahi-dnsconfd.service

%pre autoipd
%sysusers_create_compat %{SOURCE1}

%ldconfig_scriptlets libs
%ldconfig_scriptlets glib
%ldconfig_scriptlets gobject
%ldconfig_scriptlets compat-libdns_sd

%files -f %{name}.lang
%license LICENSE
%doc README docs/NEWS docs/AUTHORS
%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/services
%config(noreplace) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %{_sysconfdir}/avahi/hosts
%config(noreplace) %{_sysconfdir}/avahi/services/*.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/avahi-dbus.conf
%{_sbindir}/avahi-daemon
%dir %{_datadir}/avahi
%{_datadir}/avahi/avahi-service.dtd
%{_datadir}/avahi/service-types
%{_datadir}/dbus-1/interfaces/org.freedesktop.Avahi.*.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%dir %{_libdir}/avahi
%{_libdir}/avahi/service-types.db
%{_sysusersdir}/avahi.conf
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_mandir}/man5/avahi-daemon.conf.5*
%{_mandir}/man5/avahi.hosts.5*
%{_mandir}/man5/avahi.service.5*
%{_mandir}/man8/avahi-daemon.8*

%files libs
%license LICENSE
%{_libdir}/libavahi-common.so.3*
%{_libdir}/libavahi-client.so.3*
%{_libdir}/libavahi-core.so.7*
%{_libdir}/libavahi-libevent.so.1*

%files devel
%{_includedir}/avahi-client/
%{_includedir}/avahi-common/
%{_includedir}/avahi-core/
%{_includedir}/avahi-libevent/
%{_libdir}/libavahi-common.so
%{_libdir}/libavahi-client.so
%{_libdir}/libavahi-core.so
%{_libdir}/libavahi-libevent.so
%{_libdir}/pkgconfig/avahi-client.pc
%{_libdir}/pkgconfig/avahi-core.pc
%{_libdir}/pkgconfig/avahi-libevent.pc

%files glib
%{_libdir}/libavahi-glib.so.1*

%files glib-devel
%{_includedir}/avahi-glib/
%{_libdir}/libavahi-glib.so
%{_libdir}/pkgconfig/avahi-glib.pc

%files gobject
%{_libdir}/libavahi-gobject.so.0*
%{_libdir}/girepository-1.0/Avahi-0.6.typelib
%{_libdir}/girepository-1.0/AvahiCore-0.6.typelib

%files gobject-devel
%{_includedir}/avahi-gobject/
%{_libdir}/libavahi-gobject.so
%{_libdir}/pkgconfig/avahi-gobject.pc
%{_datadir}/gir-1.0/Avahi-0.6.gir
%{_datadir}/gir-1.0/AvahiCore-0.6.gir

%files tools
%{_bindir}/avahi-browse
%{_bindir}/avahi-browse-domains
%{_bindir}/avahi-publish
%{_bindir}/avahi-publish-address
%{_bindir}/avahi-publish-service
%{_bindir}/avahi-resolve
%{_bindir}/avahi-resolve-address
%{_bindir}/avahi-resolve-host-name
%{_bindir}/avahi-set-host-name
%{_mandir}/man1/avahi-browse.1*
%{_mandir}/man1/avahi-browse-domains.1*
%{_mandir}/man1/avahi-publish.1*
%{_mandir}/man1/avahi-publish-address.1*
%{_mandir}/man1/avahi-publish-service.1*
%{_mandir}/man1/avahi-resolve.1*
%{_mandir}/man1/avahi-resolve-address.1*
%{_mandir}/man1/avahi-resolve-host-name.1*
%{_mandir}/man1/avahi-set-host-name.1*

%files autoipd
%{_sbindir}/avahi-autoipd
%config(noreplace) %{_sysconfdir}/avahi/avahi-autoipd.action
%dir %attr(0755,avahi-autoipd,avahi-autoipd) %{_localstatedir}/lib/avahi-autoipd
%{_mandir}/man8/avahi-autoipd.8*
%{_mandir}/man8/avahi-autoipd.action.8*

%files dnsconfd
%{_sbindir}/avahi-dnsconfd
%config(noreplace) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%{_unitdir}/avahi-dnsconfd.service
%{_mandir}/man8/avahi-dnsconfd.8*
%{_mandir}/man8/avahi-dnsconfd.action.8*

%files compat-libdns_sd
%{_libdir}/libdns_sd.so.1*

%files compat-libdns_sd-devel
%{_includedir}/avahi-compat-libdns_sd/
%{_includedir}/dns_sd.h
%{_libdir}/libdns_sd.so
%{_libdir}/pkgconfig/avahi-compat-libdns_sd.pc

%changelog
%autochangelog
