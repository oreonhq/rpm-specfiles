%global source0_hash a9803a7a02ddfe5fb9704ce86f0ffc48453c321e88db85810db411ba0841152a

Summary:        Tools for network auditing and penetration testing
Name:           dsniff
Version:        2.4
Release:        0.48.b1%{?dist}
# dsniff itself is BSD-3-Clause but uses other source codes, breakdown:
# BSD-4-Clause-UC: missing/{err.[ch],{memcmp,strsep}.c,sys/queue.h}
# ISC: base64.[ch]
# LicenseRef-Fedora-Public-Domain: missing/md5.[ch]
# MIT: remote.c
License:        BSD-3-Clause AND BSD-4-Clause-UC AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.monkey.org/~dugsong/%{name}/
Source0:        https://www.monkey.org/~dugsong/%{name}/beta/%{name}-%{version}b1.tar.gz
Patch0:         dsniff-2.4-time_h.patch
Patch1:         dsniff-2.4-mailsnarf_corrupt.patch
Patch2:         dsniff-2.4-pcap_read_dump.patch
Patch3:         dsniff-2.4-multiple_intf.patch
Patch4:         dsniff-2.4-amd64_fix.patch
Patch5:         dsniff-2.4-urlsnarf_zeropad.patch
Patch6:         dsniff-2.4-libnet_11.patch
Patch7:         dsniff-2.4-checksum.patch
Patch8:         dsniff-2.4-openssl_098.patch
Patch9:         dsniff-2.4-sshcrypto.patch
Patch10:        dsniff-2.4-sysconf_clocks.patch
Patch11:        dsniff-2.4-urlsnarf_escape.patch
Patch12:        dsniff-2.4-string_header.patch
Patch13:        dsniff-2.4-arpa_inet_header.patch
Patch14:        dsniff-2.4-pop_with_version.patch
Patch15:        dsniff-2.4-obsolete_time.patch
Patch16:        dsniff-2.4-checksum_libnids.patch
Patch17:        dsniff-2.4-fedora_dirs.patch
Patch18:        dsniff-2.4-glib2.patch
Patch19:        dsniff-2.4-link_layer_offset.patch
Patch20:        dsniff-2.4-tds_decoder.patch
Patch21:        dsniff-2.4-msgsnarf_segfault.patch
Patch22:        dsniff-2.4-urlsnarf_timestamp.patch
Patch23:        dsniff-2.4-arpspoof_reverse.patch
Patch24:        dsniff-2.4-arpspoof_multiple.patch
Patch25:        dsniff-2.4-arpspoof_hwaddr.patch
Patch26:        dsniff-2.4-modernize_pop.patch
Patch27:        dsniff-2.4-libnet_name2addr4.patch
Patch28:        dsniff-2.4-pntohl_shift.patch
Patch29:        dsniff-2.4-rpc_segfault.patch
Patch30:        dsniff-2.4-openssl_110.patch
Patch31:        dsniff-2.4-remote_typo.patch
Patch32:        dsniff-2.4-smp_mflags.patch
Patch33:        dsniff-2.4-libtirpc.patch
Patch34:        dsniff-2.4-pcap_init.patch
Patch35:        dsniff-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  libnet-devel
BuildRequires:  openssl-devel
BuildRequires:  libnids-devel
BuildRequires:  glib2-devel
BuildRequires:  libpcap-devel
BuildRequires:  libdb-devel
BuildRequires:  libXmu-devel
BuildRequires:  rpcgen
BuildRequires:  libtirpc-devel
BuildRequires:  libnsl2-devel
BuildRequires:  make

%description
A collection of tools for network auditing and penetration testing. Dsniff,
filesnarf, mailsnarf, msgsnarf, urlsnarf and webspy allow to passively monitor
a network for interesting data (passwords, e-mail, files). Arpspoof, dnsspoof
and macof facilitate the interception of network traffic normally unavailable
to an attacker (e.g, due to layer-2 switching). Sshmitm and webmitm implement
active monkey-in-the-middle attacks against redirected SSH and HTTPS sessions
by exploiting weak bindings in ad-hoc PKI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure
%make_build

%install
%make_install install_prefix=$RPM_BUILD_ROOT

%files
%license LICENSE
%doc CHANGES README TODO
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/arpspoof
%{_sbindir}/dnsspoof
%{_sbindir}/%{name}
%{_sbindir}/filesnarf
%{_sbindir}/macof
%{_sbindir}/mailsnarf
%{_sbindir}/msgsnarf
%{_sbindir}/sshmitm
%{_sbindir}/sshow
%{_sbindir}/tcpkill
%{_sbindir}/tcpnice
%{_sbindir}/urlsnarf
%{_sbindir}/webmitm
%{_sbindir}/webspy
%{_mandir}/man8/arpspoof.8*
%{_mandir}/man8/dnsspoof.8*
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/filesnarf.8*
%{_mandir}/man8/macof.8*
%{_mandir}/man8/mailsnarf.8*
%{_mandir}/man8/msgsnarf.8*
%{_mandir}/man8/sshmitm.8*
%{_mandir}/man8/sshow.8*
%{_mandir}/man8/tcpkill.8*
%{_mandir}/man8/tcpnice.8*
%{_mandir}/man8/urlsnarf.8*
%{_mandir}/man8/webmitm.8*
%{_mandir}/man8/webspy.8*

%changelog
%autochangelog
