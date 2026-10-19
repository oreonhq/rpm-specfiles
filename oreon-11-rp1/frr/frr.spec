%global source0_hash 5c56b27756854b8d0a62b3e152d3f9ea08091851b2d686e140fdfb95cd88f612
%global frr_libdir %{_libexecdir}/frr
%global _hardened_build 1
%global selinuxtype targeted
%define _legacy_common_support 1
%bcond grpc %{undefined rhel}
%bcond selinux 1
Name:           frr
Version:        10.7.0
Release:        1%{?dist}
Summary:        Routing daemon
License:        GPL-2.0-or-later AND ISC AND LGPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND (GPL-2.0-or-later  OR ISC) AND MIT
URL:            http://www.frrouting.org
Source0:        https://github.com/FRRouting/frr/archive/refs/tags/%{name}-%{version}.tar.gz#/frr-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Source2:        %{name}-sysusers.conf
Source3:        frr.fc
Source4:        frr.te
Source5:        frr.if
Source6:        remove-babeld-ldpd.sh
Patch0000:      0000-remove-babeld-and-ldpd.patch
Patch0002:      0002-enable-openssl.patch
Patch0003:      0003-disable-eigrp-crypto.patch
Patch0004:      0004-fips-mode.patch
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:       %{ix86}
%endif
%if %{with grpc}
%endif
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
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  c-ares-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  groff
BuildRequires:  grpc-devel
BuildRequires:  grpc-plugins
BuildRequires:  json-c-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libyang-devel
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pam-devel
BuildRequires:  patch
BuildRequires:  pcre2-devel
BuildRequires:  perl-XML-LibXML
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(systemd)
BuildRequires:  protobuf-c-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  readline-devel
BuildRequires:  rtrlib-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n frr-frr-%{version}
#Selinux
mkdir selinux
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} selinux

%build

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
%make_build -C doc info
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
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_libdir}/frr/*.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post frr.service
if [ ! -e %{_sysconfdir}/frr/frr.conf ]; then
    echo "hostname `hostname`" > %{_sysconfdir}/frr/frr.conf
    chown frr:frr %{_sysconfdir}/frr/frr.conf
    chmod 640 %{_sysconfdir}/frr/frr.conf
fi
if [ ! -e %{_sysconfdir}/frr/vtysh.conf ]; then
    touch %{_sysconfdir}/frr/vtysh.conf
    chmod 640 %{_sysconfdir}/frr/vtysh.conf
    chown frr:frrvty %{_sysconfdir}/frr/vtysh.conf
fi
%postun

%systemd_postun_with_restart frr.service
%preun

%systemd_preun frr.service
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
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

rm tests/lib/*grpc*
%make_build check PYTHON=%{__python3}
%files -f %{oreon_filedir}/main.list
%files -n frr-headers -f %{oreon_filedir}/frr-headers.list
%files -n frr-rpki -f %{oreon_filedir}/frr-rpki.list
%files -n frr-selinux -f %{oreon_filedir}/frr-selinux.list

%changelog

%autochangelog
