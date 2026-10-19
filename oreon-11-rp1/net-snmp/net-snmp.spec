%global source0_hash 16707719f833184a4b72835dac359ae188123b06b5e42817c00790d7dc1384bf
%{!?netsnmp_check: %global netsnmp_check 1}
%global multilib_arches %{ix86} ia64 ppc ppc64 s390 s390x x86_64 sparc sparcv9 sparc64 aarch64
%global soname  45
Summary:        A collection of SNMP protocol tools and libraries
Name:       net-snmp
Version:    5.9.5.2
Release:        4%{?dist}
Epoch:      1
License:    MIT-CMU AND BSD-3-Clause AND MIT
URL:        http://net-snmp.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/net-snmp/net-snmp/%{version}/net-snmp-%{version}.tar.gz
Source1:    net-snmp.redhat.conf
Source2:    net-snmp-config.h
Source3:    net-snmp-config
Source4:    net-snmp-trapd.redhat.conf
Source5:    net-snmpd.sysconfig
Source6:    net-snmptrapd.sysconfig
Source7:    net-snmp-tmpfs.conf
Source8:    snmpd.service
Source9:    snmptrapd.service
Source10:   IETF-MIB-LICENSE.txt
Patch1:     net-snmp-5.9-pie.patch
Patch2:     net-snmp-5.9-dir-fix.patch
Patch3:     net-snmp-5.9-multilib.patch
Patch4:     net-snmp-5.9-test-debug.patch
Patch5:     net-snmp-5.7.2-cert-path.patch
Patch6:     net-snmp-5.9-cflags.patch
Patch7:     net-snmp-5.8-Remove-U64-typedef.patch
Patch8:     net-snmp-5.7.3-iterator-fix.patch
Patch9:     net-snmp-5.9-autofs-skip.patch
Patch11:    net-snmp-5.8-expand-SNMPCONFPATH.patch
Patch12:    net-snmp-5.8-duplicate-ipAddress.patch
Patch13:    net-snmp-5.9-memory-reporting.patch
Patch15:    net-snmp-5.8-ipAddress-faster-load.patch
Patch17:    net-snmp-5.9-aes-config.patch
Patch18:    net-snmp-5.8-clientaddr-error-message.patch
Patch19:    net-snmp-5.9-intermediate-certs.patch
Patch20:    net-snmp-5.9.1-remove-des.patch
Patch21:    net-snmp-libs-misunderstanding.patch
Patch22:    net-snmp-5.9-ipv6-disable-leak.patch
Patch26:    net-snmp-5.9.4-tls.patch
Patch27:    net-snmp-5.9.4-revert-n-snmptrapd-log.patch
Patch101:   net-snmp-5.8-modern-rpm-api.patch
Patch102:   net-snmp-5.9-python3.patch
Patch103:   net-snmp-5.9-mail-sender.patch
Requires:        %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:        %{name}-agent-libs%{?_isa} = %{epoch}:%{version}-%{release}
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  chrpath
BuildRequires:  elfutils-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  libselinux-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(blib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  procps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  rpm-devel
BuildRequires:  systemd
# /oreon:deps
%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management. The NET-SNMP project includes various SNMP tools:
an extensible agent, an SNMP library, tools for requesting or setting
information from SNMP agents, tools for generating and handling SNMP
traps, a version of the netstat command which uses SNMP, and a Tk/Perl
mib browser. This package contains the snmpd and snmptrapd daemons,
documentation, etc.

You will probably also want to install the net-snmp-utils package,
which contains NET-SNMP utilities.

%package utils
Summary:  Network management utilities using SNMP, from the NET-SNMP project
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description utils
The net-snmp-utils package contains various utilities for use with the
NET-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You will also need to install the net-snmp
package.

%package devel
Summary:  The development environment for the NET-SNMP project
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-agent-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: elfutils-devel, rpm-devel, elfutils-libelf-devel, openssl-devel
Requires: redhat-rpm-config
Requires: libnl3-devel
Requires: lm_sensors-devel
Requires: perl-devel%{?_isa}
%description devel
The net-snmp-devel package contains the development libraries and
header files for use with the NET-SNMP project's network management
tools.

Install the net-snmp-devel package if you would like to develop
applications for use with the NET-SNMP project's network management
tools. You'll also need to have the net-snmp and net-snmp-utils
packages installed.

%package perl-module
Summary:       The perl NET-SNMP module
Requires:      %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}, perl-interpreter
BuildRequires: perl-interpreter
BuildRequires: perl-generators
%description perl-module
The net-snmp-perl package contains the perl files to use SNMP from within
Perl.

Install the net-snmp-perl package, if you want to use SNMP with perl.
	

%package perl
Summary:       The perl-based utilities and the mib2c tool
Requires:      %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}, perl-interpreter
Requires:      %{name}-agent-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
BuildRequires: perl-interpreter
BuildRequires: perl-generators
%description perl
The net-snmp-perl package contains the utilities written in perl.

Install the net-snmp-perl package, if you want to use mib2c or other
perl utilities. Use the net-snmp-perl-module package instead to get the
SNMP perl module.

%package gui
Summary:  An interactive graphical MIB browser for SNMP
Requires: perl-Tk, %{name}-perl-module%{?_isa} = %{epoch}:%{version}-%{release}
BuildRequires: perl-interpreter
BuildRequires: perl-generators
%description gui
The net-snmp-gui package contains tkmib utility, which is a graphical user 
interface for browsing the Message Information Bases (MIBs). It is also 
capable of sending or retrieving the SNMP management information to/from 
the remote agents interactively.

Install the net-snmp-gui package, if you want to use this interactive utility.

%package libs
Summary: The NET-SNMP runtime client libraries
%description libs
The net-snmp-libs package contains the runtime client libraries for shared
binaries and applications.

%package agent-libs
Summary:   The NET-SNMP runtime agent libraries
Requires:  %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description agent-libs
The net-snmp-agent-libs package contains the runtime agent libraries for shared
binaries and applications.

%package -n python3-net-snmp
%{?python_provide:%python_provide python3-net-snmp}
Provides:  %{name}-python = %{version}-%{release}
Provides:  %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:   The Python 'netsnmp' module for the Net-SNMP
Requires:  %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description -n python3-net-snmp
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3, 
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
cp %{SOURCE10} .

%ifnarch ia64
%patch 1 -p1 -b .pie
%endif

%patch 2 -p1 -b .dir-fix
%patch 3 -p1 -b .multilib
%patch 4 -p1
%patch 5 -p1 -b .cert-path
%patch 6 -p1 -b .cflags
%patch 7 -p1 -b .u64-remove
%patch 8 -p1 -b .iterator-fix
%patch 9 -p1 -b .autofs-skip
%patch 11 -p1 -b .expand-SNMPCONFPATH
%patch 12 -p1 -b .duplicate-ipAddress
%patch 13 -p1 -b .memory-reporting
%patch 15 -p1 -b .ipAddress-faster-load
%patch 17 -p1 -b .aes-config
%patch 18 -p1 -b .clientaddr-error-message
%patch 19 -p1 -b .intermediate-certs
%patch 20 -p1 -b .remove-des
%patch 21 -p1
%patch 22 -p1 -b .ipv6-disable-leak
%patch 26 -p1 -b .tls
%patch 27 -p1 -b .revert-n-snmptrapd-log

%patch 101 -p1 -b .modern-rpm-api
%patch 102 -p1
%if 0%{?rhel} || (0%{?oreon} >= 11)
%patch 103 -p1
%endif

# disable failing test - see https://bugzilla.redhat.com/show_bug.cgi?id=680697
rm testing/fulltests/default/T200*

%build

autoreconf
MIBS="host agentx smux \
     ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
     ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
     ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
     ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
     ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
     sctp-mib rmon-mib etherlike-mib ucd-snmp/lmsensorsMib"
%configure \
    --disable-static --enable-shared \
    --enable-as-needed \
    --enable-blumenthal-aes \
    --enable-embedded-perl \
    --enable-ipv6 \
    --enable-local-smux \
    --enable-mfd-rewrites \
    --enable-ucd-snmp-compatibility \
    --disable-des \
    --sysconfdir=%{_sysconfdir} \
    --with-cflags="$RPM_OPT_FLAGS -fPIE" \
    --with-ldflags="$RPM_LD_FLAGS -lm" \
    --with-logfile="/var/log/snmpd.log" \
    --with-mib-modules="$MIBS" \
    --with-mysql \
    --with-openssl \
    --with-persistent-directory="/var/lib/net-snmp" \
    --with-perl-modules="INSTALLDIRS=vendor" \
    --with-pic \
    --with-security-modules=tsm  \
    --with-sys-location="Unknown" \
    --with-systemd \
    --with-temp-file-pattern=/run/net-snmp/snmp-tmp-XXXXXX \
    --with-transports="DTLSUDP TLSTCP" \
    --with-sys-contact="root@localhost" \
    --without-pcre <<EOF
EOF
cp libtool libtool.orig
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make}
find perl/blib -type f -name "*.so" -print -exec chrpath --delete {} \;
pushd python
%{__python3} setup.py --basedir="../" build
popd
%install
make install DESTDIR=%{buildroot}
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif
%ifarch %{multilib_arches}
mv %{buildroot}/%{_bindir}/net-snmp-config %{buildroot}/%{_bindir}/net-snmp-config-${basearch}
install -m 755 %SOURCE3 %{buildroot}/%{_bindir}/net-snmp-config
mv %{buildroot}/%{_includedir}/net-snmp/net-snmp-config.h %{buildroot}/%{_includedir}/net-snmp/net-snmp-config-${basearch}.h
install -m644 %SOURCE2 %{buildroot}/%{_includedir}/net-snmp/net-snmp-config.h
%endif
install -d %{buildroot}%{_sysconfdir}/snmp
install -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/snmp/snmpd.conf
install -m 644 %SOURCE4 %{buildroot}%{_sysconfdir}/snmp/snmptrapd.conf
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 %SOURCE5 %{buildroot}%{_sysconfdir}/sysconfig/snmpd
install -m 644 %SOURCE6 %{buildroot}%{_sysconfdir}/sysconfig/snmptrapd
install -d %{buildroot}%{_localstatedir}/lib/net-snmp
install -d %{buildroot}%{_localstatedir}/lib/net-snmp/mib_indexes
install -d %{buildroot}%{_localstatedir}/lib/net-snmp/cert_indexes
install -d %{buildroot}%{_localstatedir}/run/net-snmp
rm -f %{buildroot}%{_bindir}/snmpinform
ln -s snmptrap %{buildroot}/usr/bin/snmpinform
rm -f %{buildroot}%{_bindir}/snmpcheck
rm -f %{buildroot}/%{_bindir}/fixproc
rm -f %{buildroot}/%{_mandir}/man1/fixproc*
rm -f %{buildroot}/%{_bindir}/ipf-mod.pl
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/libsnmp*
rm -f %{buildroot}/%{_libdir}/perl5/vendor_perl/Bundle/MakefileSubs.pm
find %{buildroot} -name perllocal.pod \
    -o -name .packlist \
    -o -name "*.bs" \
    -o -name Makefile.subs.pl \
    | xargs -ri rm -f {}
rm -f README.aix README.hpux11 README.osX README.Panasonic_AM3X.txt README.solaris README.win32
install -m 644 local/mib2c.*.conf %{buildroot}%{_datadir}/snmp
pushd python
%{__python3} setup.py --basedir=.. install -O1 --skip-build --root %{buildroot} 
popd
find %{buildroot} -name '*.so' | xargs chmod 0755
dd bs=1024 count=250 if=ChangeLog of=ChangeLog.trimmed
for file in README COPYING; do
    iconv -f 8859_1 -t UTF-8 <$file >$file.utf8
    mv $file.utf8 $file
done
chmod 644 local/passtest local/ipf-mod.pl
install -m 755 -d %{buildroot}/%{_tmpfilesdir}
install -m 644 %SOURCE7 %{buildroot}/%{_tmpfilesdir}/net-snmp.conf
install -m 755 -d %{buildroot}/%{_unitdir}
install -m 644 %SOURCE8 %SOURCE9 %{buildroot}/%{_unitdir}/
%oreon_autofiles python3-net-snmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{netsnmp_check}
%ifarch ppc ppc64
rm -vf testing/fulltests/default/T200snmpv2cwalkall_simple
%endif
cp -f libtool.orig libtool
chmod 755 local/passtest
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} make test
%endif
%post

%systemd_post snmpd.service snmptrapd.service
%preun

%systemd_preun snmpd.service snmptrapd.service
%postun

%systemd_postun_with_restart snmpd.service snmptrapd.service
%ldconfig_scriptlets libs
%ldconfig_scriptlets agent-libs
%files -f %{oreon_filedir}/main.list
%files -n net-snmp-utils -f %{oreon_filedir}/net-snmp-utils.list
%files -n net-snmp-devel -f %{oreon_filedir}/net-snmp-devel.list
%files -n net-snmp-perl-module -f %{oreon_filedir}/net-snmp-perl-module.list
%files -n net-snmp-perl -f %{oreon_filedir}/net-snmp-perl.list
%files -n net-snmp-gui -f %{oreon_filedir}/net-snmp-gui.list
%files -n net-snmp-libs -f %{oreon_filedir}/net-snmp-libs.list
%files -n net-snmp-agent-libs -f %{oreon_filedir}/net-snmp-agent-libs.list
%files -n python3-net-snmp -f %{oreon_filedir}/python3-net-snmp.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:5.9.5.2-4
- Import
