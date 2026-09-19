%global source0_hash f5a671a62a11dc8114fa98eade19542ed1c3aa3c832b0e572ca0eb1a5a4faee8

%define  cvs 20051105
Name:    hping3
Version: 0.0.%{cvs}
Release: 47%{?dist}
Summary: TCP/IP stack auditing and much more

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://www.hping.org/
Source0: http://www.hping.org/hping3-20051105.tar.gz
Patch0: hping3-include.patch
Patch1: hping3-bytesex.patch
Patch2: hping3-getifnamedebug.patch
Patch3: hping3-cflags.patch
Patch4: hping3-man.patch
Patch5: hping3-20051105-typo.patch
Patch6: hping3-common.patch
BuildRequires:  gcc
BuildRequires: libpcap-devel, tcl-devel
BuildRequires: make
Obsoletes: hping2
Provides: hping2

%description
hping3 is a network tool able to send custom TCP/IP packets and to
display target replies like ping do with ICMP replies. hping3 can handle
fragmentation, and almost arbitrary packet size and content, using the
command line interface.
Since version 3, hping implements scripting capabilties

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q  -n hping3-20051105
%patch -P0 -p0 -b .include
%patch -P1 -p0 -b .bytesex
%patch -P2 -p1 -b .getifnamedebug
%patch -P3 -p0 -b .cflags
%patch -P4 -p0 -b .man
%patch -P5 -p1
%patch -P6 -p1 -b .common

%build
%configure --force-libpcap
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install -m0755 hping3 $RPM_BUILD_ROOT%{_sbindir}
install -m0644 docs/hping3.8 $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf hping3 $RPM_BUILD_ROOT%{_sbindir}/hping
ln -sf hping3 $RPM_BUILD_ROOT%{_sbindir}/hping2

%files
%doc COPYING *BUGS CHANGES README TODO docs/AS-BACKDOOR docs/HPING2-HOWTO.txt
%doc docs/HPING2-IS-OPEN docs/MORE-FUN-WITH-IPID docs/SPOOFED_SCAN.txt
%doc docs/HPING3.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%changelog
%autochangelog
