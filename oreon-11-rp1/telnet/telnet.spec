%global source0_hash 9c80d5c7838361a328fb6b60016d503def9ce53ad3c589f3b08ff71a2bb88e00
%global source2_hash fef13d44c600f7c8defc57b8b82d6edd312a39c960eebdbbeda6d01716e77a51

%global _hardened_build 1

Summary: The client program for the Telnet remote login protocol
Name: telnet
Version: 0.17
Release: 96%{?dist}
Epoch: 1
License: BSD-3-Clause AND BSD-4-Clause AND BSD-4-Clause-UC
Source0:        https://repository.timesys.com/buildsources/n/netkit-telnet/netkit-telnet-%{version}/netkit-telnet-%{version}.tar.gz
Url: http://web.archive.org/web/20070819111735/www.hcs.harvard.edu/~dholland/computers/old-netkit.html
# telnet-client tarball is snapshot of the OpenBSD client telnet
Source2: https://src.fedoraproject.org/repo/pkgs/telnet/telnet-client.tar.gz/d74983062470c5a3e7ae14f34c489e00/telnet-client.tar.gz
Source4: telnet.wmconfig
Source5: telnet@.service
Source6: telnet.socket
Patch1: telnet-client-cvs.patch
Patch5: telnetd-0.17.diff
Patch6: telnet-0.17-env.patch
Patch7: telnet-0.17-issue.patch
Patch8: telnet-0.17-sa-01-49.patch
Patch10: telnet-0.17-pek.patch
Patch11: telnet-0.17-8bit.patch
Patch12: telnet-0.17-argv.patch
Patch13: telnet-0.17-conf.patch
Patch14: telnet-0.17-cleanup_race.patch
Patch15: telnetd-0.17-pty_read.patch
Patch16: telnet-0.17-CAN-2005-468_469.patch
Patch18: telnet-gethostbyname.patch
Patch19: netkit-telnet-0.17-ipv6.diff
Patch20: netkit-telnet-0.17-nodns.patch
Patch21: telnet-0.17-errno_test_sys_bsd.patch
Patch22: netkit-telnet-0.17-reallynodns.patch
Patch23: telnet-rh678324.patch
Patch24: telnet-rh674942.patch
Patch25: telnet-rh704604.patch
Patch26: telnet-rh825946.patch
Patch27: telnet-0.17-force-ipv6-ipv4.patch
Patch28: netkit-telnet-0.17-core-dump.patch
Patch29: netkit-telnet-0.17-gcc7.patch
Patch30: netkit-telnet-0.17-manpage.patch
Patch31: netkit-telnet-0.17-telnetrc.patch
Patch32: telnet-log-address.patch
Patch33: telnet-0.17-overflow-exploit.patch
Patch34: telnet-0.17-pty-retry.patch
Patch35: telnet-c99.patch

BuildRequires: make
BuildRequires: ncurses-devel systemd gcc gcc-c++
BuildRequires: perl-interpreter

%description
Telnet is a popular protocol for logging into remote systems over the
Internet. The package provides a command line Telnet client

%package server
Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Summary: The server program for the Telnet remote login protocol

%description server
Telnet is a popular protocol for logging into remote systems over the
Internet. The package includes a daemon that supports Telnet remote
logins into the host machine. The daemon is disabled by default.
You may enable the daemon by editing /etc/xinetd.d/telnet

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%setup -q -n netkit-telnet-%{version}

mv telnet telnet-NETKIT
%setup -T -D -q -a 2 -n netkit-telnet-%{version}

%patch -P1 -p0 -b .cvs
%patch -P5 -p0 -b .fix
%patch -P6 -p1 -b .env
%patch -P10 -p0 -b .pek
%patch -P7 -p1 -b .issue
%patch -P8 -p1 -b .sa-01-49
%patch -P11 -p1 -b .8bit
%patch -P12 -p1 -b .argv
%patch -P13 -p1 -b .confverb
%patch -P14 -p1 -b .cleanup_race 
%patch -P15 -p0 -b .pty_read
%patch -P16 -p1 -b .CAN-2005-468_469
#%patch17 -p1 -b .linemode
%patch -P18 -p1 -b .gethost
%patch -P19 -p1 -b .gethost2
%patch -P20 -p1 -b .nodns
%patch -P21 -p1 -b .errnosysbsd
%patch -P22 -p1 -b .reallynodns
%patch -P23 -p1 -b .rh678324
%patch -P24 -p1 -b .rh674942
%patch -P25 -p1 -b .rh704604
%patch -P26 -p1 -b .rh825946
%patch -P27 -p1 -b .ipv6-support
%patch -P28 -p1 -b .core-dump
%patch -P29 -p1 -b .gcc7
%patch -P30 -p1 -b .manpage
%patch -P31 -p1 -b .telnetrc
%patch -P32 -p1 -b .log-address
%patch -P33 -p1 -b .overflow
%patch -P34 -p1 -b .pty-retry
%patch -P35 -p1 -b .c99

%build
%ifarch s390 s390x
    export CC_FLAGS="$RPM_OPT_FLAGS -fPIE"
%else
    export CC_FLAGS="$RPM_OPT_FLAGS -fpie"
%endif

export LD_FLAGS="$RPM_LD_FLAGS -z now -pie"

sh configure --with-c-compiler=%{__cc} 
perl -pi -e '
    s,-O2,\$(CC_FLAGS),;
    s,LDFLAGS=.*,LDFLAGS=\$(LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG

# remove stripping
perl -pi -e 's|install[ ]+-s|install|g' \
    ./telnet/GNUmakefile \
    ./telnetd/Makefile \
    ./telnetlogin/Makefile \
    ./telnet-NETKIT/Makefile

%{make_build}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8

make INSTALLROOT=${RPM_BUILD_ROOT} install

install -D -p -m644 %SOURCE5 ${RPM_BUILD_ROOT}%{_unitdir}/telnet@.service
install -D -p -m644 %SOURCE6 ${RPM_BUILD_ROOT}%{_unitdir}/telnet.socket

%post server
%systemd_post telnet.socket

%preun server
%systemd_preun telnet.socket

%postun server
%systemd_postun_with_restart telnet.socket

%files
%doc README
%{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files server
%{_unitdir}/*
%{_sbindir}/in.telnetd
%{_mandir}/man5/issue.net.5*
%{_mandir}/man8/in.telnetd.8*
%{_mandir}/man8/telnetd.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17-96
- Prepare for Oreon 11 (RP1)
