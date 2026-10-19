%global source0_hash 1f4693394d7c19f979343367215a9a9b84261ff6152429d2d7b28a883f524e73
%bcond_without gnuplot
%define _libexecdir %{_libdir}
%define defconfig DailySet1
%define indexserver amandahost
%define tapeserver %{indexserver}
%define amanda_user amandabackup
%define amanda_group disk
%global _hardened_build 1
Summary:        A network-capable tape backup solution
Name:          amanda
Version:       3.5.4
Release:        1%{?dist}
Source0:        https://github.com/zmanda/amanda/archive/refs/tags/tag-community-%{version}.tar.gz#/amanda-%{version}.tar.gz
Source1:       amanda.crontab
Source4:       disklist
Source8:       amandahosts
Source9:       amanda.socket
Source10:      amanda@.service
Source11:      activate-devpay.1.gz
Source12:      killpgrp.8
Source13:      amanda-udp.socket
Source14:      amanda-udp.service
Source15:      kamanda.socket
Source16:      kamanda@.service
Patch1:        amanda-3.1.1-xattrs.patch
Patch2:        amanda-3.1.1-tcpport.patch
Patch3:        amanda-3.2.0-config-dir.patch
Patch4:        amanda-3.4.5-no-xinetd.patch
Patch5:        patch-tirpc
Patch6:        patch-xfsrestore-housekeeping
Patch7: amanda-configure-c99.patch
Patch8: amanda-c99.patch
Patch9:        https://github.com/zmanda/amanda/pull/273.patch
Patch10:       https://github.com/zmanda/amanda/pull/270.patch
License:       BSD-3-Clause AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-2.0-only
URL:           http://www.amanda.org
%if %{with gnuplot}
%endif
Requires:      grep tar /usr/bin/mail
Requires:      amanda-libs%{?_isa} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%{?systemd_requires}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)
%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{perl_vendorarch}/auto/.*\\.so$
%global __requires_exclude ^perl\\(Dancer2\\)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cups
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gnuplot
BuildRequires:  grep
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  mt-st
BuildRequires:  mtx
BuildRequires:  openssh-clients
BuildRequires:  openssl-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  procps-ng
BuildRequires:  readline-devel
BuildRequires:  rpcgen
BuildRequires:  rsh
BuildRequires:  samba-client
BuildRequires:  swig
BuildRequires:  systemd
BuildRequires:  tar
BuildRequires:  xfsdump
# /oreon:deps
%description
AMANDA, the Advanced Maryland Automatic Network Disk Archiver, is a
backup system that allows the administrator of a LAN to set up a
single master backup server to back up multiple hosts to one or more
tape drives or disk files.  AMANDA uses native dump and/or GNU tar
facilities and can back up a large number of workstations running
multiple versions of Unix.  Newer versions of AMANDA (including this
version) can use SAMBA to back up Microsoft(TM) Windows95/NT hosts.
The amanda package contains the core AMANDA programs and will need to
be installed on both AMANDA clients and AMANDA servers.  Note that you
will have to install the amanda-client and/or amanda-server packages as
well.

%package libs
Summary:       Amanda libraries
Requires:      grep
%description libs
This package contains basic Amanda libraries, which are used by all
Amanda programs.

%package client
Summary:       The client component of the AMANDA tape backup system
Requires:      grep
Requires(pre): amanda = %{version}-%{release}
Requires:      amanda-libs%{?_isa} = %{version}-%{release}
%description client
The Amanda-client package should be installed on any machine that will
be backed up by AMANDA (including the server if it also needs to be
backed up).  You will also need to install the amanda package on each
AMANDA client machine.

%package server
Summary:       The server side of the AMANDA tape backup system
Requires:      grep
Requires:      perl(Amanda::DB) perl(Amanda::Recovery) perl(Amanda::Service)
Requires(pre): amanda = %{version}-%{release}
Requires:      amanda-libs%{?_isa} = %{version}-%{release}
%description server
The amanda-server package should be installed on the AMANDA server,
the machine attached to the device(s) (such as a tape drive) where backups
will be written. You will also need to install the amanda package on
the AMANDA server machine.  And, if the server is also to be backed up, the
server also needs to have the amanda-client package installed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-tag-community-%{version}

# Create a sysusers.d config file
cat >amanda.sysusers.conf <<EOF
u amandabackup 33:%amanda_group 'Amanda user' %{_localstatedir}/lib/amanda /bin/bash
m amandabackup tape
EOF

%build

./autogen
export MAILER=/usr/bin/mail CFLAGS="$RPM_OPT_FLAGS -fPIE -std=c17" LDFLAGS="$RPM_LD_FLAGS -pie"
%configure --enable-shared \
           --enable-manpage-build \
           --disable-rpath \
           --disable-static \
           --disable-dependency-tracking \
           --disable-installperms \
           --with-amdatadir=%{_localstatedir}/lib/amanda \
           --with-amlibdir=%{_libdir} \
           --with-amperldir=%{perl_vendorarch} \
           --with-index-server=%{indexserver} \
           --with-tape-server=%{tapeserver} \
           --with-config=%{defconfig} \
           --with-gnutar-listdir=%{_localstatedir}/lib/amanda/gnutar-lists \
           --with-smbclient=%{_bindir}/smbclient \
           --with-amandates=%{_localstatedir}/lib/amanda/amandates \
           --with-amandahosts \
           --with-user=%amanda_user \
           --with-group=%amanda_group \
           --with-tmpdir=/var/log/amanda \
           --with-gnutar=/bin/tar \
%if %{without gnuplot}
           --without-gnuplot \
%endif
           --with-ssh-security \
           --with-rsh-security \
           --with-bsdtcp-security \
           --with-bsdudp-security \
           --with-krb5-security
pushd perl
make maintainer-clean-am
popd
%make_build
%install
%make_install BINARY_OWNER=%(id -un) SETUID_GROUP=%(id -gn)
mkdir -p $RPM_BUILD_ROOT/etc/amanda
mkdir -p $RPM_BUILD_ROOT/var/log/amanda/amandad
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda
install -m 600 %SOURCE8 $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda/.amandahosts
install -p -m 644 -D %{SOURCE9} %{buildroot}%{_unitdir}/amanda.socket
install -p -m 644 -D %{SOURCE10} %{buildroot}%{_unitdir}/amanda@.service
install -p -m 644 -D %{SOURCE13} %{buildroot}%{_unitdir}/amanda-udp.socket
install -p -m 644 -D %{SOURCE14} %{buildroot}%{_unitdir}/amanda-udp.service
install -p -m 644 -D %{SOURCE15} %{buildroot}%{_unitdir}/kamanda.socket
install -p -m 644 -D %{SOURCE16} %{buildroot}%{_unitdir}/kamanda@.service
install -D %{SOURCE11}  %{buildroot}/%{_mandir}/man1/activate-devpay.1.gz
install -D %{SOURCE12}  %{buildroot}/%{_mandir}/man8/killpgrp.8
install -m 644 %{buildroot}/etc/amanda/amanda-security.conf %{buildroot}/etc/amanda-security.conf
ln -s %{_libexecdir}/amanda/amandad $RPM_BUILD_ROOT%{_sbindir}/amandad
ln -s amrecover.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/amoldrecover.8
pushd ${RPM_BUILD_ROOT}
  mv .%{_localstatedir}/lib/amanda/example .%{_sysconfdir}/amanda/%defconfig
  cp ${RPM_SOURCE_DIR}/amanda.crontab .%{_sysconfdir}/amanda/crontab.sample
  cp ${RPM_SOURCE_DIR}/disklist .%{_sysconfdir}/amanda/%defconfig
  cp ${RPM_SOURCE_DIR}/disklist .%{_sysconfdir}/amanda/%defconfig
  rm -f .%{_sysconfdir}/amanda/%defconfig/xinetd*
  rm -f .%{_sysconfdir}/amanda/%defconfig/inetd*
  mkdir -p .%{_localstatedir}/lib/amanda/gnutar-lists
  mkdir -p .%{_localstatedir}/lib/amanda/%defconfig/index
  touch .%{_localstatedir}/lib/amanda/amandates
popd
rm -rf $RPM_BUILD_ROOT/usr/share/amanda
find $RPM_BUILD_ROOT -name \*.la | xargs rm
pushd $RPM_BUILD_ROOT/usr/bin
rm amandad
ln -s ../%_lib/amanda/amandad
popd
install -m0644 -D amanda.sysusers.conf %{buildroot}%{_sysusersdir}/amanda.conf
%oreon_autofiles amanda-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles amanda-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles amanda-server usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%post

%{?ldconfig}
%systemd_post amanda.socket amanda-udp.socket kamanda.socket
%preun

%systemd_preun amanda.socket amanda-udp.socket kamanda.socket
%postun

%{?ldconfig}
%systemd_postun_with_restart amanda.socket amanda-udp.socket kamanda.socket
%ldconfig_scriptlets client
%ldconfig_scriptlets server
%files -f %{oreon_filedir}/main.list
%files -n amanda-libs -f %{oreon_filedir}/amanda-libs.list
%files -n amanda-client -f %{oreon_filedir}/amanda-client.list
%files -n amanda-server -f %{oreon_filedir}/amanda-server.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.4-1
- Prepare for Oreon 11 (RP1)
