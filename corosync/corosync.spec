# Conditionals
# Invoke "rpmbuild --without <feature>" or "rpmbuild --with <feature>"
# to disable or enable specific features
%bcond_with watchdog
%bcond_with monitoring
%bcond_without snmp
%bcond_without dbus
%bcond_without systemd
%bcond_without xmlconf
%bcond_without nozzle
%bcond_without vqsim
%bcond_without runautogen
%bcond_without userflags

Name: corosync
Summary: The Corosync Cluster Engine and Application Programming Interfaces
Version: 3.1.10
Release: 4%{?dist}
License: BSD-3-Clause
URL: http://corosync.github.io/corosync/
Source0: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# Runtime bits
# The automatic dependency overridden in favor of explicit version lock
Requires: corosynclib%{?_isa} = %{version}-%{release}

# Support crypto reload
Requires: libknet1 >= 1.18
# NSS crypto plugin should be always installed
Requires: libknet1-crypto-nss-plugin >= 1.18

# Build bits
BuildRequires: gcc
BuildRequires: groff
BuildRequires: libqb-devel
BuildRequires: libknet1-devel >= 1.18
BuildRequires: zlib-devel
%if %{with runautogen}
BuildRequires: autoconf automake libtool
%endif
%if %{with monitoring}
BuildRequires: libstatgrab-devel
%endif
%if %{with snmp}
BuildRequires: net-snmp-devel
%endif
%if %{with dbus}
BuildRequires: dbus-devel
%endif
%if %{with nozzle}
BuildRequires: libnozzle1-devel
%endif
%if %{with systemd}
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: systemd-devel
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
%endif
%if %{with xmlconf}
Requires: libxslt
%endif
%if %{with vqsim}
BuildRequires: readline-devel
%endif
BuildRequires: make
BuildRequires: git

%prep
%autosetup -S git_am

%build
%if %{with runautogen}
./autogen.sh
%endif

%{configure} \
%if %{with watchdog}
	--enable-watchdog \
%endif
%if %{with monitoring}
	--enable-monitoring \
%endif
%if %{with snmp}
	--enable-snmp \
%endif
%if %{with dbus}
	--enable-dbus \
%endif
%if %{with systemd}
	--enable-systemd \
%endif
%if %{with xmlconf}
	--enable-xmlconf \
%endif
%if %{with nozzle}
	--enable-nozzle \
%endif
%if %{with vqsim}
	--enable-vqsim \
%endif
%if %{with userflags}
	--enable-user-flags \
%endif
	--with-initddir=%{_initrddir} \
	--with-systemddir=%{_unitdir} \
	--docdir=%{_docdir}

%make_build

%install
%make_install

%if %{with dbus}
mkdir -p -m 0700 %{buildroot}/%{_sysconfdir}/dbus-1/system.d
install -m 644 %{_builddir}/%{name}-%{version}/conf/corosync-signals.conf %{buildroot}/%{_datadir}/dbus-1/system.d/corosync-signals.conf
%endif

## tree fixup
# drop static libs
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
# drop docs and html docs for now
rm -rf %{buildroot}%{_docdir}/*
# /etc/sysconfig/corosync-notifyd
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 tools/corosync-notifyd.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-notifyd
# /etc/sysconfig/corosync
install -m 644 init/corosync.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync

%description
This package contains the Corosync Cluster Engine Executive, several default
APIs and libraries, default configuration files, and an init script.

%post
%if %{with systemd} && 0%{?systemd_post:1}
%systemd_post corosync.service
%else
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add corosync || :
fi
%endif

%preun
%if %{with systemd} && 0%{?systemd_preun:1}
%systemd_preun corosync.service
%else
if [ $1 -eq 0 ]; then
	/sbin/service corosync stop &>/dev/null || :
	/sbin/chkconfig --del corosync || :
fi
%endif

%postun
%if %{with systemd} && 0%{?systemd_postun:1}
%systemd_postun corosync.service
%endif

%files
%doc LICENSE
%{_sbindir}/corosync
%{_sbindir}/corosync-keygen
%{_sbindir}/corosync-cmapctl
%{_sbindir}/corosync-cfgtool
%{_sbindir}/corosync-cpgtool
%{_sbindir}/corosync-quorumtool
%{_sbindir}/corosync-notifyd
%{_bindir}/corosync-blackbox
%if %{with xmlconf}
%{_bindir}/corosync-xmlproc
%dir %{_datadir}/corosync
%{_datadir}/corosync/xml2conf.xsl
%{_mandir}/man8/corosync-xmlproc.8*
%{_mandir}/man5/corosync.xml.5*
%endif
%dir %{_sysconfdir}/corosync
%dir %{_sysconfdir}/corosync/uidgid.d
%config(noreplace) %{_sysconfdir}/corosync/corosync.conf.example
%config(noreplace) %{_sysconfdir}/sysconfig/corosync-notifyd
%config(noreplace) %{_sysconfdir}/sysconfig/corosync
%config(noreplace) %{_sysconfdir}/logrotate.d/corosync
%if %{with dbus}
%{_datadir}/dbus-1/system.d/corosync-signals.conf
%endif
%if %{with snmp}
%{_datadir}/snmp/mibs/COROSYNC-MIB.txt
%endif
%if %{with systemd}
%{_unitdir}/corosync.service
%{_unitdir}/corosync-notifyd.service
%else
%{_initrddir}/corosync
%{_initrddir}/corosync-notifyd
%endif
%if %{without systemd}
%dir %{_localstatedir}/lib/corosync
%dir %{_localstatedir}/log/cluster
%endif
%{_mandir}/man7/corosync_overview.7*
%{_mandir}/man8/corosync.8*
%{_mandir}/man8/corosync-blackbox.8*
%{_mandir}/man8/corosync-cmapctl.8*
%{_mandir}/man8/corosync-keygen.8*
%{_mandir}/man8/corosync-cfgtool.8*
%{_mandir}/man8/corosync-cpgtool.8*
%{_mandir}/man8/corosync-notifyd.8*
%{_mandir}/man8/corosync-quorumtool.8*
%{_mandir}/man5/corosync.conf.5*
%{_mandir}/man5/votequorum.5*
%{_mandir}/man7/cmap_keys.7*

# library
#
%package -n corosynclib
Summary: The Corosync Cluster Engine Libraries

%description -n corosynclib
This package contains corosync libraries.

%files -n corosynclib
%doc LICENSE
%{_libdir}/libcfg.so.*
%{_libdir}/libcpg.so.*
%{_libdir}/libcmap.so.*
%{_libdir}/libquorum.so.*
%{_libdir}/libvotequorum.so.*
%{_libdir}/libsam.so.*
%{_libdir}/libcorosync_common.so.*

%ldconfig_scriptlets -n corosynclib

%package -n corosynclib-devel
Summary: The Corosync Cluster Engine Development Kit
Requires: corosynclib%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: corosync-devel = %{version}-%{release}
Provides: corosync-devel%{?_isa} = %{version}-%{release}

%description -n corosynclib-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%files -n corosynclib-devel
%doc LICENSE
%dir %{_includedir}/corosync/
%{_includedir}/corosync/corodefs.h
%{_includedir}/corosync/cfg.h
%{_includedir}/corosync/cmap.h
%{_includedir}/corosync/corotypes.h
%{_includedir}/corosync/cpg.h
%{_includedir}/corosync/hdb.h
%{_includedir}/corosync/sam.h
%{_includedir}/corosync/quorum.h
%{_includedir}/corosync/votequorum.h
%{_libdir}/libcfg.so
%{_libdir}/libcpg.so
%{_libdir}/libcmap.so
%{_libdir}/libquorum.so
%{_libdir}/libvotequorum.so
%{_libdir}/libsam.so
%{_libdir}/libcorosync_common.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/cpg_*3*
%{_mandir}/man3/quorum_*3*
%{_mandir}/man3/votequorum_*3*
%{_mandir}/man3/sam_*3*
%{_mandir}/man3/cmap_*3*

%if %{with vqsim}
%package -n corosync-vqsim
Summary: The Corosync Cluster Engine - Votequorum Simulator
Requires: corosynclib%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description -n corosync-vqsim
A command-line simulator for the corosync votequorum subsystem.
It uses the same code as the corosync quorum system but forks
them into subprocesses to simulate nodes.
Nodes can be added and removed as well as partitioned (to simulate
network splits)

%files -n corosync-vqsim
%doc LICENSE
%{_bindir}/corosync-vqsim
%{_mandir}/man8/corosync-vqsim.8*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.10-4
- Prepare for Oreon 11 (RP1)
