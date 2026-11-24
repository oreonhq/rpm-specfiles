# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d8ee7aa6bbb3ff1be7d9e57637d0d0ec2f18273a8efff1a0afe2c665858b96f7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           unbound
Version:        1.26.2
Release:        1%{?dist}
Summary:        Validating, recursive, and caching DNS(SEC) resolver
License:        BSD-3-Clause
URL:            https://nlnetlabs.nl/projects/unbound/
Source0:        https://nlnetlabs.nl/downloads/unbound/unbound-%{version}.tar.gz
Source1:        unbound.service
Source2:        unbound.sysusers
Source3:        tmpfiles-unbound.conf
Source4:        unbound-anchor.service
Source5:        unbound-anchor.timer
Source6:        root.anchor

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  expat-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  hiredis-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     %{name}-anchor%{?_isa} = %{version}-%{release}

%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

%package libs
Summary:        libunbound, the validating stub resolver library

%description libs
The libunbound shared library and the DNSSEC root trust anchor it uses.

%package devel
Summary:        Development files for libunbound
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       openssl-devel
Provides:       pkgconfig(libunbound) = %{version}

%description devel
Headers and the pkg-config file for libunbound.

%package anchor
Summary:        DNSSEC trust anchor maintenance tool
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description anchor
unbound-anchor keeps the root trust anchor current using RFC 5011 rollover.

%package utils
Summary:        Unbound DNS lookup utilities
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description utils
unbound-host, a DNS lookup tool that can validate DNSSEC.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure \
  --disable-rpath \
  --disable-static \
  --enable-pie \
  --enable-relro-now \
  --enable-subnet \
  --enable-cachedb \
  --enable-systemd \
  --disable-gost \
  --with-pthreads \
  --with-libevent \
  --with-ssl \
  --with-libnghttp2 \
  --with-libhiredis \
  --with-username=unbound \
  --with-chroot-dir="" \
  --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \
  --with-pidfile=%{_rundir}/%{name}/%{name}.pid \
  --with-rootkey-file=%{_sharedstatedir}/%{name}/root.key
%make_build

%install
%make_install unbound-event-install
rm -f %{buildroot}%{_libdir}/*.la
install -p -D -m 0644 contrib/libunbound.pc %{buildroot}%{_libdir}/pkgconfig/libunbound.pc
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/unbound.service
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/unbound-anchor.service
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/unbound-anchor.timer
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sharedstatedir}/%{name}/root.key
mkdir -p %{buildroot}%{_rundir}/%{name}

%check
make check

%post
%systemd_post unbound.service

%preun
%systemd_preun unbound.service

%postun
%systemd_postun_with_restart unbound.service

%post anchor
%systemd_post unbound-anchor.service unbound-anchor.timer

%preun anchor
%systemd_preun unbound-anchor.service unbound-anchor.timer

%postun anchor
%systemd_postun unbound-anchor.service unbound-anchor.timer

%files
%doc doc/CREDITS doc/FEATURES
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/unbound.conf
%{_unitdir}/unbound.service
%{_tmpfilesdir}/%{name}.conf
%attr(0775,unbound,root) %dir %{_rundir}/%{name}
%{_sbindir}/unbound
%{_sbindir}/unbound-checkconf
%{_sbindir}/unbound-control
%{_sbindir}/unbound-control-setup
%{_mandir}/man5/unbound.conf.5*
%{_mandir}/man8/unbound.8*
%{_mandir}/man8/unbound-checkconf.8*
%{_mandir}/man8/unbound-control.8*
%{_mandir}/man8/unbound-control-setup.8*

%files libs
%license LICENSE
%{_libdir}/libunbound.so.8*
%{_sysusersdir}/%{name}.conf
%dir %attr(0755,unbound,unbound) %{_sharedstatedir}/%{name}
%config %verify(not link owner group size mtime mode md5) %attr(0644,unbound,unbound) %{_sharedstatedir}/%{name}/root.key

%files devel
%{_includedir}/unbound.h
%{_includedir}/unbound-event.h
%{_libdir}/libunbound.so
%{_libdir}/pkgconfig/libunbound.pc
%{_mandir}/man3/libunbound.3*
%{_mandir}/man3/ub_*.3*

%files anchor
%{_sbindir}/unbound-anchor
%{_unitdir}/unbound-anchor.service
%{_unitdir}/unbound-anchor.timer
%{_mandir}/man8/unbound-anchor.8*

%files utils
%{_sbindir}/unbound-host
%{_mandir}/man1/unbound-host.1*

%changelog
%autochangelog
