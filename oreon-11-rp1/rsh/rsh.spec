%global source0_hash 9bcf9986eb9637d1b8e8ab62a61c80f3422d628e837e72c6ad8c2e38604ccaf4

%global _hardened_build 1

Summary: Clients for remote access commands (rsh, rlogin, rcp)
Name: rsh
Version: 0.17
Release: 113%{?dist}
License: BSD-4-Clause-UC

BuildRequires: make
BuildRequires: perl-interpreter, ncurses-devel, pam-devel, audit-libs-devel, systemd, gcc

URL: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit
Source0: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/netkit-rsh-%{version}.tar.gz
Source1: rexec.pam
Source2: rlogin.pam
Source3: rsh.pam
# Source is no longer publicly available.
Source4: rexec-1.5.tar.gz
Source5: rsh@.service
Source6: rsh.socket
Source7: rlogin@.service
Source8: rlogin.socket
Source9: rexec@.service
Source10: rexec.socket

Patch1: netkit-rsh-0.17-sectty.patch
# Make rexec installation process working
Patch2: netkit-rsh-0.17-rexec.patch
Patch3: netkit-rsh-0.10-stdarg.patch
# Improve installation process
Patch4: netkit-rsh-0.16-jbj.patch
# Link rshd against libpam
Patch8: netkit-rsh-0.16-jbj4.patch
Patch9: netkit-rsh-0.16-prompt.patch
Patch10: netkit-rsh-0.16-rlogin=rsh.patch
# Improve documentation
Patch11: netkit-rsh-0.16-nokrb.patch
# Remove spurious double-reporting of errors
Patch12: netkit-rsh-0.17-pre20000412-jbj5.patch
# RH #42880
Patch13: netkit-rsh-0.17-userandhost.patch
# Don't strip binaries during installation
Patch14: netkit-rsh-0.17-strip.patch
# RH #67362
Patch15: netkit-rsh-0.17-lfs.patch
# RH #57392
Patch16: netkit-rsh-0.17-chdir.patch
# RH #63806
Patch17: netkit-rsh-0.17-pam-nologin.patch
# RH #135643
Patch19: netkit-rsh-0.17-rexec-netrc.patch
# RH #68590
Patch20: netkit-rsh-0.17-pam-sess.patch
# RH #67361
Patch21: netkit-rsh-0.17-errno.patch
# RH #118630
Patch22: netkit-rsh-0.17-rexec-sig.patch
# RH #135827
Patch23: netkit-rsh-0.17-nohost.patch
# RH #122315
Patch24: netkit-rsh-0.17-ignchld.patch
# RH #146464
Patch25: netkit-rsh-0.17-checkdir.patch
Patch26: netkit-rsh-0.17-pam-conv.patch
# RH #174045
Patch27: netkit-rsh-0.17-rcp-largefile.patch
# RH #174146
Patch28: netkit-rsh-0.17-pam-rhost.patch
# RH #178916
Patch29: netkit-rsh-0.17-rlogin-linefeed.patch
Patch30: netkit-rsh-0.17-ipv6.patch
Patch31: netkit-rsh-0.17-pam_env.patch
Patch33: netkit-rsh-0.17-dns.patch
Patch34: netkit-rsh-0.17-nohostcheck-compat.patch
# RH #448904
Patch35: netkit-rsh-0.17-audit.patch
Patch36: netkit-rsh-0.17-longname.patch
# RH #440867
Patch37: netkit-rsh-0.17-arg_max.patch
Patch38: netkit-rsh-0.17-rh448904.patch
Patch39: netkit-rsh-0.17-rh461903.patch
Patch40: netkit-rsh-0.17-rh473492.patch
Patch41: netkit-rsh-0.17-rh650119.patch
Patch42: netkit-rsh-0.17-rh710987.patch
Patch43: netkit-rsh-0.17-rh784467.patch
Patch44: netkit-rsh-0.17-rh896583.patch
Patch45: netkit-rsh-0.17-rh947213.patch
Patch46: 0001-rshd-use-sockaddr_in-for-non-native-IPv6-clients.patch
Patch47: 0002-rlogind-use-sockaddr_in-for-non-native-IPv6-client.patch
Patch48: netkit-rsh-0.17-ipv6-rexec.patch
Patch49: 0001-rshd-include-missing-header-file.patch
Patch50: 0001-rshd-use-upper-bound-for-cmdbuflen.patch   
Patch51: 0001-rcp-don-t-advance-pointer-returned-from-rcp_basename.patch
Patch52: netkit-rsh-0.17-union-wait.patch
Patch53: netkit-rsh-0.17-cmdbuflen.patch
Patch54: netkit-rsh-0.17-CVE-2019-7282.patch
Patch55: netkit-rsh-0.17-c99.patch
Patch56: netkit-rsh-0.17-c99-2.patch

%description
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp).  All three of these commands
use rhosts style authentication.  This package contains the clients
needed for all of these services.
The rsh package should be installed to enable remote access to other
machines

%package server
Summary: Servers for remote access commands (rsh, rlogin, rcp)
Requires: pam, /etc/pam.d/system-auth
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description server
The rsh-server package contains a set of programs which allow users
to run commands on remote machines, login to other machines and copy
files between machines (rsh, rlogin and rcp).  All three of these
commands use rhosts style authentication.  This package contains the
servers needed for all of these services.  It also contains a server
for rexec, an alternate method of executing remote commands.
All of these servers are run by systemd and configured using
systemd units and PAM.

The rsh-server package should be installed to enable remote access
from other machines

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n netkit-rsh-%{version} -a 4
%patch -P1 -p1 -b .sectty
%patch -P2 -p1 -b .rexec
%patch -P3 -p1 -b .stdarg
%patch -P4 -p1 -b .jbj
%patch -P8 -p1 -b .jbj4
%patch -P9 -p1 -b .prompt
%patch -P10 -p1 -b .rsh
%patch -P11 -p1 -b .rsh.nokrb
%patch -P12 -p1 -b .jbj5
%patch -P13 -p1 -b .userandhost
%patch -P14 -p1 -b .strip
%patch -P15 -p1 -b .lfs
%patch -P16 -p1 -b .chdir
%patch -P17 -p1 -b .pam-nologin
%patch -P19 -p1 -b .rexec-netrc
%patch -P20 -p1 -b .pam-sess
%patch -P21 -p1 -b .errno
%patch -P22 -p1 -b .rexec-sig
%patch -P23 -p1 -b .nohost
%patch -P24 -p1 -b .ignchld
%patch -P25 -p1 -b .checkdir
%patch -P26 -p1 -b .pam-conv
%patch -P27 -p1 -b .largefile
%patch -P28 -p1 -b .pam-rhost
%patch -P29 -p1 -b .linefeed
%patch -P30 -p1 -b .ipv6
%patch -P31 -p1 -b .pam_env
%patch -P33 -p1 -b .dns
%patch -P34 -p1 -b .compat
%patch -P35 -p1 -b .audit
%patch -P36 -p1 -b .longname
%patch -P37 -p1 -b .arg_max
%patch -P38 -p1 -b .rh448904
%patch -P39 -p1 -b .rh461903
%patch -P40 -p1 -b .rh473492
%patch -P41 -p1 -b .rh650119
%patch -P42 -p1 -b .rh710987
%patch -P43 -p1 -b .rh784467
%patch -P44 -b .rh896583
%patch -P45 -p1 -b .rh947213
%patch -P46 -p1
%patch -P47 -p1
%patch -P48 -p1 -b .ipv6-rexec
%patch -P49 -p1 -b .waitpid
%patch -P50 -p1
%patch -P51 -p1
%patch -P52 -p1 -b .union-wait
%patch -P53 -p1 -b .cmdbuflen
%patch -P54 -p1 -b .cve-2019-7282
%patch -P55 -p1 -b .c99
%patch -P56 -p1 -b .c99-2

# No, I don't know what this is doing in the tarball.
rm -f rexec/rexec

%build
sh configure --with-c-compiler=%{__cc}
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%ifarch s390 s390x
%{__perl} -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS) -fPIC -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE,;
    s,^LDFLAGS=,LDFLAGS=\$(RPM_LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG
%else
%{__perl} -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS) -fpic -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE,;
    s,^LDFLAGS=,LDFLAGS=\$(RPM_LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG
%endif
%{make_build}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
mkdir -p %{buildroot}%{_sysconfdir}/pam.d

%{make_install} INSTALLROOT=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir}

install -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/pam.d/rexec
install -m 644 %SOURCE2 %{buildroot}%{_sysconfdir}/pam.d/rlogin
install -m 644 %SOURCE3 %{buildroot}%{_sysconfdir}/pam.d/rsh

mkdir -p %{buildroot}%{_unitdir}
install -m644 %SOURCE5 %{buildroot}%{_unitdir}/rsh@.service
install -m644 %SOURCE6 %{buildroot}%{_unitdir}/rsh.socket
install -m644 %SOURCE7 %{buildroot}%{_unitdir}/rlogin@.service
install -m644 %SOURCE8 %{buildroot}%{_unitdir}/rlogin.socket
install -m644 %SOURCE9 %{buildroot}%{_unitdir}/rexec@.service
install -m644 %SOURCE10 %{buildroot}%{_unitdir}/rexec.socket

%post server
%systemd_post rsh.socket
%systemd_post rlogin.socket
%systemd_post rexec.socket

%preun server
%systemd_preun rsh.socket
%systemd_preun rlogin.socket
%systemd_preun rexec.socket

%postun server
%systemd_postun_with_restart rsh.socket
%systemd_postun_with_restart rlogin.socket
%systemd_postun_with_restart rexec.socket

%files
%doc README BUGS
%attr(0755,root,root) %caps(cap_net_bind_service=pe) %{_bindir}/rcp
%{_bindir}/rexec
%attr(0755,root,root) %caps(cap_net_bind_service=pe) %{_bindir}/rlogin
%attr(0755,root,root) %caps(cap_net_bind_service=pe) %{_bindir}/rsh
%{_mandir}/man1/*.1*

%files server
%config(noreplace) %{_sysconfdir}/pam.d/rsh
%config(noreplace) %{_sysconfdir}/pam.d/rlogin
%config(noreplace) %{_sysconfdir}/pam.d/rexec
%{_sbindir}/in.rexecd
%{_sbindir}/in.rlogind
%{_sbindir}/in.rshd
%{_unitdir}/*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
