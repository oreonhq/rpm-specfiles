# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0a51b8f920254d8e83c34a4c3082b7d241f5d6fd65188afadf29859d5223ef78
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_without quota_enables_extdirect
%bcond_without quota_enables_netlink
%bcond_without quota_enables_rpc
%bcond_without quota_enables_rpcsetquota
%bcond_with quota_enables_tcpwrappers

Name:       quota
Epoch:      1
Version:    4.11
Release:    1%{?dist}
Summary:    System administration tools for monitoring users' disk usage
License:    GPL-2.0-only AND GPL-2.0-or-later
URL:        http://sourceforge.net/projects/linuxquota/
Source0:        https://downloads.sourceforge.net/linuxquota/%{name}-%{version}.tar.gz
Source1:    quota_nld.service
Source2:    quota_nld.sysconfig
Source3:    rpc-rquotad.service
Source4:    rpc-rquotad.sysconfig
Patch0:     quota-4.06-warnquota-configuration-tunes.patch
Patch1:     quota-4.03-Validate-upper-bound-of-RPC-port.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  e2fsprogs-devel
BuildRequires:  clang
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  openldap-devel
%if %{with quota_enables_extdirect}
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ext2fs)
%endif
%if %{with quota_enables_netlink}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  systemd-rpm-macros
%endif
%if %{with quota_enables_rpc}
BuildRequires:  rpcgen
BuildRequires:  pkgconfig(libtirpc)
%if %{with quota_enables_tcpwrappers}
BuildRequires:  tcp_wrappers-devel
%endif
%endif
Requires:       quota-nls = %{epoch}:%{version}-%{release}
Conflicts:      kernel < 2.4

%description
The quota package contains system administration tools for monitoring
and limiting user and or group disk usage per file system.

%if %{with quota_enables_netlink}
%package nld
Summary:    quota_nld daemon
License:    GPL-2.0-only AND GPL-2.0-or-later
Requires:   quota-nls = %{epoch}:%{version}-%{release}
Requires:   systemd

%description nld
Daemon that listens on netlink socket and processes received quota warnings.
Note, that you have to enable the kernel support for sending quota messages
over netlink (in Filesystems->Quota menu). The daemon supports forwarding
warning messages to the system D-Bus (so that desktop manager can display
a dialog) and writing them to the terminal user has last accessed.
%endif

%if %{with quota_enables_rpc}
%package rpc
Summary:    RPC quota daemon
License:    LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later
Requires:   quota-nls = %{epoch}:%{version}-%{release}
Requires:   rpcbind
Requires:   systemd
%if %{with quota_enables_tcpwrappers}
Requires:   tcp_wrappers
%endif
Conflicts:  quota < 1:4.02-3

%description rpc
The RPC daemon allows to query and set disk quotas over network. If you run
the daemon on NFS server, you could use quota tools to manage the quotas from
NFS client.
%endif

%package warnquota
Summary:    Send e-mail to users over quota
License:    GPL-2.0-only AND GPL-2.0-or-later
Requires:   quota-nls = %{epoch}:%{version}-%{release}

%description warnquota
Utility that checks disk quota for each local file system and mails a warning
message to those users who have reached their soft limit.  It is typically run
via cron(8).

%package nls
Summary:    Gettext catalogs for disk quota tools
License:    LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later
BuildArch:  noarch

%description nls
Disk quota tools messages translated into different natural languages.

%if %{with quota_enables_rpc}
%package devel
Summary:    Development files for quota RPC
License:    GPL-2.0-only
Requires:   libtirpc-devel

%description devel
This package contains development header files for implementing disk quotas
on remote machines.
%endif

%package doc
Summary:    Additional documentation for disk quotas
Requires:   quota =  %{epoch}:%{version}-%{release}
BuildArch:  noarch
AutoReq:    0

%description doc
This package contains additional documentation for disk quotas concept in
Linux/UNIX environment.

%prep
%oreon_sha256
%setup -q
%patch -P0 -p1
%patch -P1 -p1

autoreconf -f -i

%build
%global _hardened_build 1
%configure \
    --enable-bsd-behaviour \
%if %{with quota_enables_extdirect}
    --enable-ext2direct=yes \
%else
    --enable-ext2direct=no \
%endif
    --enable-ldapmail=yes \
%if %{with quota_enables_tcpwrappers}
    --enable-libwrap=yes \
%else
    --disable-libwrap \
%endif
%if %{with quota_enables_netlink}
    --enable-netlink=yes \
%else
    --disable-netlink \
%endif
    --enable-nls \
    --with-pid-dir=/run \
    --disable-rpath \
%if %{with quota_enables_rpc}
    --enable-rpc=yes \
%else
    --disable-rpc \
%endif
%if %{with quota_enables_rpcsetquota}
    --enable-rpcsetquota=yes \
%else
    --disable-rpcsetquota \
%endif
    --disable-silent-rules \
    --disable-xfs-roothack
%{make_build}

%install
%{make_install}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with quota_enables_netlink}
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/quota_nld.service
install -p -m644 -D %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/quota_nld
%endif
%if %{with quota_enables_rpc}
install -p -m644 -D %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/rpc-rquotad.service
install -p -m644 -D %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rpc-rquotad
%endif

%find_lang %{name}

%check
make check

%if %{with quota_enables_netlink}
%post nld
%systemd_post quota_nld.service

%preun nld
%systemd_preun quota_nld.service

%postun nld
%systemd_postun_with_restart quota_nld.service
%endif

%if %{with quota_enables_rpc}
%post rpc
%systemd_post rpc-rquotad.service

%preun rpc
%systemd_preun rpc-rquotad.service

%postun rpc
%systemd_postun_with_restart rpc-rquotad.service
%endif

%files
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sbindir}/quota_nld
%if %{with quota_enables_rpc}
%exclude %{_sbindir}/rpc.rquotad
%endif
%exclude %{_sbindir}/warnquota
%{_mandir}/man1/*
%{_mandir}/man8/*
%exclude %{_mandir}/man8/quota_nld.8*
%if %{with quota_enables_rpc}
%exclude %{_mandir}/man8/rpc.rquotad.8*
%endif
%exclude %{_mandir}/man8/warnquota.8*
%doc Changelog

%if %{with quota_enables_netlink}
%files nld
%config(noreplace) %{_sysconfdir}/sysconfig/quota_nld
%{_unitdir}/quota_nld.service
%{_sbindir}/quota_nld
%{_mandir}/man8/quota_nld.8*
%doc Changelog
%endif

%if %{with quota_enables_rpc}
%files rpc
%config(noreplace) %{_sysconfdir}/sysconfig/rpc-rquotad
%{_unitdir}/rpc-rquotad.service
%{_sbindir}/rpc.rquotad
%{_mandir}/man8/rpc.rquotad.8*
%doc Changelog
%endif

%files warnquota
%config(noreplace) %{_sysconfdir}/quotagrpadmins
%config(noreplace) %{_sysconfdir}/quotatab
%config(noreplace) %{_sysconfdir}/warnquota.conf
%{_sbindir}/warnquota
%{_mandir}/man5/*
%{_mandir}/man8/warnquota.8*
%doc Changelog README.ldap-support README.mailserver

%files nls -f %{name}.lang
%license COPYING
%doc Changelog

%if %{with quota_enables_rpc}
%files devel
%license COPYING
%dir %{_includedir}/rpcsvc
%{_includedir}/rpcsvc/*
%{_mandir}/man3/*
%endif

%files doc
%doc doc/* ldap-scripts

%changelog
%autochangelog
