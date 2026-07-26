%global source0_hash 038a580b6497bab516a3e0dca59dfa2fe8cf3c0151bef45d57572fb756c2a64c

Summary: A security tool which acts as a wrapper for TCP daemons
Name: tcp_wrappers
Version: 7.6
Release: 112%{?dist}

%global LIB_MAJOR 0
%global LIB_MINOR 7
%global LIB_REL 6

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source: https://github.com/tcp-wrappers/tarballs/blob/main/%{name}_%{version}-ipv6.4.tar.gz
URL: https://github.com/tcp-wrappers
Patch0: tcpw7.2-config.patch
Patch1: tcpw7.2-setenv.patch
Patch2: tcpw7.6-netgroup.patch
Patch3: tcp_wrappers-7.6-bug11881.patch
Patch4: tcp_wrappers-7.6-bug17795.patch
Patch5: tcp_wrappers-7.6-bug17847.patch
Patch6: tcp_wrappers-7.6-fixgethostbyname.patch
Patch7: tcp_wrappers-7.6-docu.patch
Patch8: tcp_wrappers-7.6-man.patch
Patch9: tcp_wrappers.usagi-ipv6.patch
Patch11: tcp_wrappers-7.6-shared.patch
Patch12: tcp_wrappers-7.6-sig.patch
Patch14: tcp_wrappers-7.6-ldflags.patch
Patch15: tcp_wrappers-7.6-fix_sig-bug141110.patch
Patch16: tcp_wrappers-7.6-162412.patch
Patch17: tcp_wrappers-7.6-220015.patch
Patch19: tcp_wrappers-7.6-siglongjmp.patch
Patch20: tcp_wrappers-7.6-sigchld.patch
Patch21: tcp_wrappers-7.6-196326.patch
Patch22: tcp_wrappers_7.6-249430.patch
Patch23: tcp_wrappers-7.6-inetdconf.patch
Patch24: tcp_wrappers-7.6-bug698464.patch
Patch26: tcp_wrappers-7.6-xgets.patch
Patch27: tcp_wrappers-7.6-initgroups.patch
Patch28: tcp_wrappers-7.6-warnings.patch
Patch29: tcp_wrappers-7.6-uchart_fix.patch
Patch30: tcp_wrappers-7.6-altformat.patch
# RFE: rhbz#1181815
Patch31: tcp_wrappers-7.6-aclexec.patch
Patch32: tcp_wrappers-inetcf-c99.patch
# required by sin_scope_id in ipv6 patch
# RFE: rhbz#2341423
Patch33: tcp_wrappers-7.6-gcc15-errors.patch
Patch34: tcp_wrappers-7.6-gcc15-warnings.patch
BuildRequires: make
BuildRequires: glibc-devel >= 2.2
BuildRequires: libnsl2-devel
BuildRequires: gcc
Requires: tcp_wrappers-libs%{?_isa} = %{version}-%{release}

%description
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, FTP, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

Install the tcp_wrappers program if you need a security tool for
filtering incoming network services requests.

This version also supports IPv6.

%package libs
Summary: Libraries for tcp_wrappers
Obsoletes: tcp_wrappers-devel <= 0:7.6-91

%description libs
tcp_wrappers-libs contains the libraries of the tcp_wrappers package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_%{version}-ipv6.4
%patch -P0 -p1 -b .config
%patch -P1 -p1 -b .setenv
%patch -P2 -p1 -b .netgroup
%patch -P3 -p1 -b .bug11881
%patch -P4 -p1 -b .bug17795
%patch -P5 -p1 -b .bug17847
%patch -P6 -p1 -b .fixgethostbyname
%patch -P7 -p1 -b .docu
%patch -P8 -p1 -b .man
%patch -P9 -p1 -b .usagi-ipv6
%patch -P11 -p1 -b .shared
%patch -P12 -p1 -b .sig
%patch -P14 -p1 -b .ldflags
%patch -P15 -p1 -b .fix_sig
%patch -P16 -p1 -b .162412
%patch -P17 -p1 -b .220015
%patch -P19 -p1 -b .siglongjmp
%patch -P20 -p1 -b .sigchld
%patch -P21 -p1 -b .196326
%patch -P22 -p1 -b .249430
%patch -P23 -p1 -b .inetdconf
%patch -P24 -p1 -b .698464
%patch -P26 -p1 -b .xgets
%patch -P27 -p1 -b .initgroups
%patch -P29 -p1 -b .uchart_fix
%patch -P30 -p1 -b .altformat
%patch -P28 -p1 -b .warnings
%patch -P31 -p1 -b .aclexec
%patch -P32 -p1
%patch -P33 -p1
%patch -P34 -p1

%build
make \
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR -DACLEXEC" \
LDFLAGS="$RPM_LD_FLAGS" \
MAJOR=%{LIB_MAJOR} MINOR=%{LIB_MINOR} REL=%{LIB_REL} linux %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
mkdir -p ${RPM_BUILD_ROOT}/%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{3,5,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

install -p -m644 hosts_access.3 ${RPM_BUILD_ROOT}%{_mandir}/man3
install -p -m644 hosts_access.5 hosts_options.5 ${RPM_BUILD_ROOT}%{_mandir}/man5
install -p -m644 tcpd.8 tcpdchk.8 tcpdmatch.8 safe_finger.8 try-from.8 ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -sf hosts_access.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/hosts.allow.5
ln -sf hosts_access.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/hosts.deny.5
#cp -a libwrap.a ${RPM_BUILD_ROOT}%{_libdirdir}
cp -a libwrap.so* ${RPM_BUILD_ROOT}/%{_libdir}
#install -p -m644 libwrap.so.0.7.6 ${RPM_BUILD_ROOT}/%{_libdir}
install -p -m644 tcpd.h ${RPM_BUILD_ROOT}%{_includedir}
install -m755 safe_finger ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 tcpd ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 try-from ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 tcpdmatch ${RPM_BUILD_ROOT}%{_sbindir}

# XXX remove utilities that expect /etc/inetd.conf (#16059).
#install -m755 tcpdchk ${RPM_BUILD_ROOT}%{_sbindir}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpdchk.*

# Remove the files from -devel subpackage
rm -f ${RPM_BUILD_ROOT}%{_includedir}/*
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.so
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man3/*

%ldconfig_scriptlets libs

%files
%{!?_licensedir:%global license %%doc}
%license DISCLAIMER
%doc BLURB CHANGES README* Banners.Makefile
%{_sbindir}/*
%{_mandir}/man8/*

%files libs
%{!?_licensedir:%global license %%doc}
%license DISCLAIMER
%doc BLURB CHANGES README* Banners.Makefile
%{_libdir}/*.so.*
%{_mandir}/man5/*

%changelog
%autochangelog
