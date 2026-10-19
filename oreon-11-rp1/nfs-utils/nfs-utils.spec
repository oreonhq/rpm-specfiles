%global source0_hash 7dbc05eb8b32828b322872b759a62cb3979cb4118f344dd8616813d1390e84e0
Summary:        NFS utilities and supporting clients and daemons for the kernel NFS server
Name: nfs-utils
URL: http://linux-nfs.org/
Version: 3.1.1
Release:        1%{?dist}
Epoch: 1
%global all_32bit_archs i386 i486 i586 i686 athlon ppc sparcv9
Source0:        https://www.kernel.org/pub/linux/utils/nfs-utils/%{version}/%{name}-%{version}.tar.xz
Source1: id_resolver.conf
Source2: lockd.conf
Source3: 24-nfs-server.conf
Source4: 10-nfsv4.conf
Source5: 10-nfsv3.conf
Patch100: nfs-utils-1.2.1-statdpath-man.patch
Patch102: nfs-utils-1.2.5-idmap-errmsg.patch
Patch103: nfs-utils-2.3.1-systemd-gssproxy-restart.patch
Patch104: nfs-utils-2.3.3-man-tcpwrappers.patch
Patch105: nfs-utils-2.3.3-nfsconf-usegssproxy.patch
Patch106: nfs-utils-2.4.2-systemd-svcgssd.patch
%global rpcuser_uid 29
%global nfsnobody_uid 65534
Provides: exportfs    = %{epoch}:%{version}-%{release}
Provides: rpc.idmapd  = %{epoch}:%{version}-%{release}
Provides: rpc.mountd  = %{epoch}:%{version}-%{release}
Provides: user(nfsnobody)
Provides: group(nfsnobody)
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/rpc.mountd
Provides: /usr/sbin/rpc.nfsd
%endif
License: GPL-2.0-only AND GPL-2.0-or-later AND BSD-3-Clause AND BSD-2-Clause AND (HPND-export-US-modify AND HPND-sell-variant) AND (GPL-2.0-only WITH Linux-syscall-note OR BSD-3-Clause)
Requires(pre): shadow-utils >= 4.0.3-25
Requires(pre): util-linux
Requires(pre): coreutils
Requires(preun): coreutils
Requires: nfs-common-utils = %{epoch}:%{version}-%{release}
Requires: nfs-client-utils = %{epoch}:%{version}-%{release}
Requires: libnfsidmap%{?_isa} = %{epoch}:%{version}-%{release} libevent
Requires: libtirpc >= 0.2.3-1 libblkid libcap libmount
Requires: gssproxy => 0.7.0-3
Requires: rpcbind, sed, gawk, grep
Requires: kmod, keyutils, quota
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  krb5-libs
BuildRequires:  libblkid-devel
BuildRequires:  libcap-devel
BuildRequires:  libevent-devel
BuildRequires:  libmount-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  rpcgen
BuildRequires:  sqlite-devel
BuildRequires:  systemd
# /oreon:deps
%package -n nfs-common-utils
Summary: Common NFS utilities
Provides: mount.nfs   = %{epoch}:%{version}-%{release}
Provides: nfsstat     = %{epoch}:%{version}-%{release}
Provides: rpcdebug    = %{epoch}:%{version}-%{release}
Provides: rpc.gssd    = %{epoch}:%{version}-%{release}
Provides: umount.nfs  = %{epoch}:%{version}-%{release}
Requires: gssproxy => 0.7.0-3
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /sbin/mount.nfs
Provides: /usr/sbin/mount.nfs
%endif
%description -n nfs-common-utils
This package contains various programs that are used for both NFSv3
and NFSv4.

This package contains the showmount program.  Showmount queries the
mount daemon on a remote host for information about the NFS (Network File
System) server on the remote host.  For example, showmount can display the
clients which are mounted on that host.

This package also contains the mount.nfs and umount.nfs program.

%package -n nfs-client-utils
Summary: NFS client utilities
Provides: nfs-client         = %{epoch}:%{version}-%{release}
Provides: nfs-utils-coreos   = %{epoch}:%{version}-%{release}
Obsoletes: nfs-utils-coreos  < %{epoch}:%{version}-%{release}
Requires: nfsv3-client-utils = %{epoch}:%{version}-%{release}
Requires: nfsv4-client-utils = %{epoch}:%{version}-%{release}
%description -n nfs-client-utils
Utilities for supporting NFS clients.  This is a metapackage that causes
both nfsv3-client-utils and nfsv4-client-utils to be installed.

%package -n nfs-python-utils
Summary: NFS utilities that require a python interpreter
Provides: mountstats  = %{epoch}:%{version}-%{release}
Provides: nfsiostat   = %{epoch}:%{version}-%{release}
Provides: rpcctl      = %{epoch}:%{version}-%{release}
%description -n nfs-python-utils
This package contains optional NFS utilities that require a python 
interpreter, including mountstats and nfsiostat.

%package -n nfsv3-client-utils
Summary: NFSv3 client utilities
Provides: rpc.statd        = %{epoch}:%{version}-%{release}
Provides: sm-notify        = %{epoch}:%{version}-%{release}
Provides: start-statd      = %{epoch}:%{version}-%{release}
Provides: user(rpcuser)
Provides: group(rpcuser)
Requires: nfs-common-utils = %{epoch}:%{version}-%{release}
Requires: rpcbind
%{?systemd_requires}
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /sbin/rpc.statd
Provides: /usr/sbin/rpc.statd
%endif
%description -n nfsv3-client-utils
This package provides programs necessary for NFSv3 client support,
including rpc.statd and sm-notify.

%package -n nfsv4-client-utils
Summary: NFSv4 client utilities
Provides: mount.nfs4  = %{epoch}:%{version}-%{release}
Provides: nfsidmap    = %{epoch}:%{version}-%{release}
Provides: umount.nfs4 = %{epoch}:%{version}-%{release}
Requires: nfs-common-utils = %{epoch}:%{version}-%{release}
%{?systemd_requires}
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /sbin/mount.nfs4
Provides: /usr/sbin/mount.nfs4
%endif
%description -n nfsv4-client-utils
This package provides files necessary for NFSv4 client support, 
including mount.nfs4, umount.nfs4, and nfsidmap.

%package -n libnfsidmap
Summary: NFSv4 User and Group ID Mapping Library
Provides: libnfsidmap%{?_isa} = %{epoch}:%{version}-%{release}
License: BSD-3-Clause
BuildRequires: pkgconfig, openldap-devel
BuildRequires: automake, libtool
Requires: openldap
%description -n libnfsidmap
Library that handles mapping between names and ids for NFSv4.

%package -n libnfsidmap-devel
Summary: Development files for the libnfsidmap library
License: BSD-3-Clause
Requires: libnfsidmap%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
%description -n libnfsidmap-devel
This package includes header files and libraries necessary for
developing programs which use the libnfsidmap library.

%description
The nfs-utils package provides a daemon for the kernel NFS server and
related tools, which provides a much higher level of performance than the
traditional Linux NFS server used by most users.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Remove .orig files
find . -name "*.orig" | xargs rm -f

# Change shebangs
find -name \*.py -exec sed -r -i '1s|^#!\s*/usr/bin.*python.*|#!%{__python3}|' {} \;

# Create a sysusers.d config file
cat >nfs-utils.sysusers.conf <<EOF
u rpcuser %{rpcuser_uid} 'RPC Service User' /var/lib/nfs -
EOF

%build

sh -x autogen.sh
%global _statdpath /var/lib/nfs/statd
%configure \
    CFLAGS="%{build_cflags} -D_FILE_OFFSET_BITS=64" \
    LDFLAGS="%{build_ldflags}" \
    --enable-mountconfig \
    --enable-ipv6 \
	--with-statdpath=%{_statdpath} \
	--enable-libmount-mount \
	--with-systemd \
	--without-tcp-wrappers \
	--with-pluginpath=%{_libdir}/libnfsidmap \
	--enable-junction
%make_build all
%install
%global _pkgdir %{_prefix}/lib/systemd
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_pkgdir}/system
mkdir -p $RPM_BUILD_ROOT%{_pkgdir}/system-generators
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/request-key.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gssproxy
%make_install
install -s -m 755 tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT%{_sbindir}
install -m 644 utils/mount/nfsmount.conf  $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 nfs.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 support/nfsidmap/idmapd.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/request-key.d
mkdir -p $RPM_BUILD_ROOT/run/sysconfig
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/lockd.conf
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/gssproxy
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.{a,la}
rm -rf $RPM_BUILD_ROOT%{_libdir}/libnfsidmap/*.{a,la}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/rpc_pipefs
touch $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/rmtab
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/statd/sm
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/statd/sm.bak
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/exports.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}/nfs-utils/nfsmount.conf.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/nfs-utils/nfsmount.conf.d
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/nfs-utils/nfsmount.conf.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/nfsmount.conf.d
ln -sf %{_datadir}/nfs-utils/nfsmount.conf.d/10-nfsv4.conf $RPM_BUILD_ROOT%{_sysconfdir}/nfsmount.conf.d
ln -sf %{_datadir}/nfs-utils/nfsmount.conf.d/10-nfsv3.conf $RPM_BUILD_ROOT%{_sysconfdir}/nfsmount.conf.d
mv -v $RPM_BUILD_ROOT/sbin/* $RPM_BUILD_ROOT%{_sbindir}/
install -m0644 -D nfs-utils.sysusers.conf %{buildroot}%{_sysusersdir}/nfs-utils.conf
%oreon_autofiles nfs-common-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nfs-client-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nfs-python-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nfsv3-client-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nfsv4-client-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libnfsidmap usr/*/lib*.so.*
%oreon_autofiles libnfsidmap-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pre

for x in gssd idmapd ; do
    if [ -f /var/lock/subsys/rpc.$x ]; then
		mv /var/lock/subsys/rpc.$x /var/lock/subsys/rpc$x
    fi
done
cat /etc/group | cut -d':' -f 3 | grep --quiet %{nfsnobody_uid} 2>/dev/null
if [ "$?" -eq 1 ]; then
    /usr/sbin/groupadd -g %{nfsnobody_uid} nfsnobody >/dev/null 2>&1 || :
fi
cat /etc/passwd | cut -d':' -f 3 | grep --quiet %{nfsnobody_uid} 2>/dev/null
if [ $? -eq 1 ]; then
    /usr/sbin/useradd -l -c "Anonymous NFS User" -r -g %{nfsnobody_uid} \
		-s /sbin/nologin -u %{nfsnobody_uid} -d /var/lib/nfs nfsnobody >/dev/null 2>&1 || :
fi
%post

%systemd_post nfs-server.service
%post -n nfs-common-utils

%systemd_post nfs-client.target
%post -n nfs-client-utils

rm -f %{_sysconfdir}/nfsmount.conf.d/10-nfsv4.conf
rm -f %{_sysconfdir}/nfsmount.conf.d/10-nfsv3.conf
%preun

%systemd_preun nfs-client.target nfs-server.service
%systemd_preun auth-rpcgss-module.service
%systemd_preun fsidd.service
%systemd_preun rpc-gssd.service
%systemd_preun rpc-statd-notify.service
%systemd_preun var-lib-nfs-rpc_pipefs.mount
if [ $1 -eq 0 ]; then
    ( : >%{_localstatedir}/lib/rpm-state/nfs-server.cleanup ) || :
fi
%preun -n nfs-common-utils

%systemd_preun nfs-client.target
%postun

%systemd_postun_with_reload nfs-server.service
if [ -f %{_localstatedir}/lib/rpm-state/nfs-server.cleanup ]; then
    rm %{_localstatedir}/lib/rpm-state/nfs-server.cleanup || :
    rm -rf /var/lib/nfs/statd || :
    rm -rf /var/lib/nfs/v4recovery || :
fi
%postun -n nfs-common-utils

%systemd_postun_with_reload nfs-client.target
%triggerin -- nfs-utils > 1:2.6.2-1

/bin/systemctl try-restart gssproxy || :
rm -rf /etc/systemd/system/nfs-*.requires
rm -rf /etc/systemd/system/rpc-*.requires
rm -rf %{_libexecdir}/nfs-utils
%triggerun -- nfs-utils > 1:2.6.2-0

/bin/systemctl disable nfs-convert > /dev/null 2>&1 || :
%triggerin -n nfsv3-client-utils -- nfsv4-client-utils

rm -f %{_sysconfdir}/nfsmount.conf.d/10-nfsv3.conf
%triggerin -n nfsv4-client-utils -- nfsv3-client-utils

rm -f %{_sysconfdir}/nfsmount.conf.d/10-nfsv4.conf
%files -f %{oreon_filedir}/main.list
%files -n nfs-common-utils -f %{oreon_filedir}/nfs-common-utils.list
%files -n nfs-client-utils -f %{oreon_filedir}/nfs-client-utils.list
%files -n nfs-python-utils -f %{oreon_filedir}/nfs-python-utils.list
%files -n nfsv3-client-utils -f %{oreon_filedir}/nfsv3-client-utils.list
%files -n nfsv4-client-utils -f %{oreon_filedir}/nfsv4-client-utils.list
%files -n libnfsidmap -f %{oreon_filedir}/libnfsidmap.list
%files -n libnfsidmap-devel -f %{oreon_filedir}/libnfsidmap-devel.list

%changelog

%autochangelog
