# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a84b973e713349dca09e2009f33dc499564f2e9faba01c0d3cba9204802b0cd5
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global frr_libdir %{_libexecdir}/frr

%global _hardened_build 1
%global selinuxtype targeted
%define _legacy_common_support 1

%bcond grpc %{undefined rhel}
%bcond selinux 1

Name:           frr
Version:        10.5.0
Release:        8%{?dist}
Summary:        Routing daemon
License:        GPL-2.0-or-later AND ISC AND LGPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND (GPL-2.0-or-later  OR ISC) AND MIT
URL:            http://www.frrouting.org
Source0:        https://github.com/FRRouting/frr/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Source2:        %{name}-sysusers.conf
#Decentralized SELinux policy
Source3:        frr.fc
Source4:        frr.te
Source5:        frr.if

Source6:        remove-babeld-ldpd.sh

Patch0000:      0000-remove-babeld-and-ldpd.patch
Patch0002:      0002-enable-openssl.patch
Patch0003:      0003-disable-eigrp-crypto.patch
Patch0004:      0004-fips-mode.patch
Patch0005:      0005-remove-grpc-test.patch

# 
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:       %{ix86}
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison >= 2.7
BuildRequires:  c-ares-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  groff
%if %{with grpc}
BuildRequires:  grpc-devel
BuildRequires:  grpc-plugins
%endif
BuildRequires:  json-c-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libyang-devel >= 2.1.128
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pam-devel
BuildRequires:  patch
BuildRequires:  pcre2-devel
BuildRequires:  perl-XML-LibXML
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo
BuildRequires:  protobuf-c-devel
# RPKI support
BuildRequires:  rtrlib-devel

Requires:       ncurses
Requires:       net-snmp
Requires(post): hostname
Requires(post): systemd
Requires(postun): systemd
Requires(preun): systemd

%if 0%{?with_selinux}
Requires: (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif

Obsoletes:      quagga < 1.2.4-17
Provides:       routingdaemon = %{version}-%{release}

%description
FRRouting is free software that manages TCP/IP based routing protocols. It takes
a multi-server and multi-threaded approach to resolve the current complexity
of the Internet.

FRRouting supports BGP4, OSPFv2, OSPFv3, ISIS, RIP, RIPng, PIM, NHRP, PBR,
EIGRP and BFD.

FRRouting is a fork of Quagga.

%package headers
Summary: Build headers for FRR
BuildArch: noarch
Requires: json-c-devel
Requires: libyang-devel

%description headers
Build headers for FRR required to generate out of tree dplane plugins

%package rpki
Summary: BGP RPKI support (rtrlib)
Group: System Environment/Daemons
BuildRequires:  rtrlib-devel >= 0.8
Requires: %{name}%{_isa} = %{version}-%{release}

%description rpki
Adds RPKI support to FRR's bgpd, allowing validation of BGP routes
against cryptographic information stored in WHOIS databases.  This is
used to prevent hijacking of networks on the wider internet.  It is only
relevant to internet service providers using their own autonomous system
number.

%if 0%{?with_selinux}
%package selinux
Summary:  Selinux policy for FRR
BuildArch:  noarch
Requires:  selinux-policy-%{selinuxtype}
Requires(post):  selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description selinux
SELinux policy modules for FRR package

%endif

%prep
%oreon_verify_sources
%autosetup -S git
#Selinux
mkdir selinux
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} selinux

%build
# C++17 or later needed for abseil-cpp-20250814
export CXXFLAGS="%{optflags} -std=gnu++17"
export CFLAGS="%{optflags} -DINET_NTOP_NO_OVERRIDE"
autoreconf -ivf

%configure \
    --sbindir=%{frr_libdir} \
    --sysconfdir=%{_sysconfdir} \
    --libdir=%{_libdir}/frr \
    --libexecdir=%{_libexecdir}/frr \
    --localstatedir=/var \
    --enable-multipath=64 \
    --enable-vtysh=yes \
    --enable-ospfclient \
    --enable-ospfapi \
    --enable-snmp=agentx \
    --enable-user=frr \
    --enable-group=frr \
    --enable-vty-group=frrvty \
    --enable-rtadv \
    --enable-static=no \
    --disable-ldpd \
    --disable-babeld \
    --with-pkgconfigdir=%{_datadir}/pkgconfig \
    --with-moduledir=%{_libdir}/frr/modules \
    --with-yangmodelsdir=%{_datadir}/frr-yang/ \
    --with-crypto=openssl \
    --enable-fpm \
    --enable-pcre2posix \
    --enable-rpki \
    --enable-sharpd \
    %{?with_grpc:--enable-grpc}

%make_build MAKEINFO="makeinfo --no-split" PYTHON=%{__python3}

# Build info documentation
%make_build -C doc info

#SELinux policy
%if 0%{?with_selinux}
make -C selinux -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 selinux/%{name}.pp
%endif

%install
mkdir -p %{buildroot}%{_sysconfdir}/{frr,rc.d/init.d,sysconfig,logrotate.d,pam.d,default} \
         %{buildroot}%{_infodir} %{buildroot}%{_unitdir}

mkdir -p -m 0755 %{buildroot}%{_libdir}/frr
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_sysusersdir}

%make_install

# Remove this file, as it is uninstalled and causes errors when building on RH9
rm -rf %{buildroot}%{_infodir}/dir

install -p -m 644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
install -p -m 644 tools/etc/frr/daemons %{buildroot}%{_sysconfdir}/frr/daemons
install -p -m 644 tools/frr.service %{buildroot}%{_unitdir}/frr.service
install -p -m 755 tools/frrinit.sh %{buildroot}%{frr_libdir}/frr
install -p -m 755 tools/frrcommon.sh %{buildroot}%{frr_libdir}/frrcommon.sh
install -p -m 755 tools/watchfrr.sh %{buildroot}%{frr_libdir}/watchfrr.sh

install -p -m 644 redhat/frr.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/frr
install -p -m 644 redhat/frr.pam %{buildroot}%{_sysconfdir}/pam.d/frr
install -d -m 775 %{buildroot}/run/frr

%if 0%{?with_selinux}
install -D -m 644 selinux/%{name}.pp.bz2 \
  %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -m 644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

# Delete libtool archives
find %{buildroot} -type f -name "*.la" -delete -print

# Upstream does not maintain a stable API
rm %{buildroot}%{_libdir}/frr/*.so


%post
%systemd_post frr.service

# Create dummy files if they don't exist so basic functions can be used.
if [ ! -e %{_sysconfdir}/frr/frr.conf ]; then
    echo "hostname `hostname`" > %{_sysconfdir}/frr/frr.conf
    chown frr:frr %{_sysconfdir}/frr/frr.conf
    chmod 640 %{_sysconfdir}/frr/frr.conf
fi

#still used by vtysh, this way no error is produced when using vtysh
if [ ! -e %{_sysconfdir}/frr/vtysh.conf ]; then
    touch %{_sysconfdir}/frr/vtysh.conf
    chmod 640 %{_sysconfdir}/frr/vtysh.conf
    chown frr:frrvty %{_sysconfdir}/frr/vtysh.conf
fi

%postun
%systemd_postun_with_restart frr.service

%preun
%systemd_preun frr.service

#SELinux
%if 0%{?with_selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
#/var/tmp and /var/run need to be relabeled as well if FRR is running before upgrade
if [ $1 == 2 ]; then
    %{_sbindir}/restorecon -R /var/tmp/frr &> /dev/null || :
    %{_sbindir}/restorecon -R /var/run/frr &> /dev/null || :
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi

%endif

%check
#this should be temporary, the grpc test is just badly designed
rm tests/lib/*grpc*
%make_build check PYTHON=%{__python3}

%files
%license COPYING
%doc doc/mpls
%dir %attr(750,frr,frr) %{_sysconfdir}/frr
%dir %attr(755,frr,frr) /run/frr
%{_infodir}/*info*
%{_mandir}/man1/frr.1*
%{_mandir}/man1/vtysh.1*
%{_mandir}/man8/frr-*.8*
%{_mandir}/man8/mtracebis.8*
%dir %{frr_libdir}/
%{frr_libdir}/*
%{_bindir}/mtracebis
%{_bindir}/vtysh
%dir %{_libdir}/frr
%{_libdir}/frr/*.so.*
%dir %{_libdir}/frr/modules
%{_libdir}/frr/modules/*
%exclude %{_libdir}/frr/modules/bgpd_rpki.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logrotate.d/frr
%config(noreplace) %attr(644,frr,frr) %{_sysconfdir}/frr/daemons
%config(noreplace) %{_sysconfdir}/pam.d/frr
%{_unitdir}/*.service
%dir %{_datadir}/frr-yang
%{_datadir}/frr-yang/*.yang
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf

%files headers
%dir %{_includedir}/frr/
%{_includedir}/frr/*
%{_datadir}/pkgconfig/frr.pc

%files rpki
%{_libdir}/frr/modules/bgpd_rpki.so

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.5.0-8
- Import
