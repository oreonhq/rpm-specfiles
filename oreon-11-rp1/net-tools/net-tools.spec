# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4c2653b5f16b277dd6f1459e3e56c55e8bb19ed8cf2b5e60f6174ead3bbede0e
%global source1_hash 29b272ddfc73c34a091845b6cc4dfebdd2599dec9401c74d9b2f670c4a744115
%global source2_hash 6cc8e674198cd95904365fbb6b7f9e88df3e9bb0f104a9ef1a57ca718fb721bd
%global source3_hash f6fa7fb86f55d4b7a6c4da437b6fb521efe8a4614b4b8c52c7b5159a07ae21ad
%global source4_hash 1885eea165db28c3b28e3a7e5d57facf55c2d765688231446d68fc1d18633b4c
%global source5_hash 455383ee16d3b1ef7f2313f3a6868d251f88eec958202c0a8c53ecf5de09baf0
%global source6_hash 88c8c0c7294cd98fb9b58ebdaf099659653f0eda1fd2b6c5497ad784eed692fe
%global source7_hash 767a6868755cbd12e32800e98515593adbef7c14d93b417e8d1b12633808b57c
%global source8_hash bafe132ea74fd8c502769cf28ad6175ac514d55f65fab633b26b9c143350e183
%global source9_hash b0540261fd06e9e2d8e3387c492eafe24cfb67e8897a1b12813ee27ca31df2be
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global checkout 20160912git

%if !0%{?fedora} || 0%{?fedora} >= 44
%bcond remove_german_man8 1
%bcond remove_french_man8 1
%else
%bcond remove_german_man8 0
%bcond remove_french_man8 0
%endif

Summary: Basic networking tools
Name: net-tools
Version: 2.0
Release: 0.79.%{checkout}%{?dist}
License: GPL-2.0-or-later
URL: http://sourceforge.net/projects/net-tools/

Source0: net-tools-%{version}.%{checkout}.tar.xz
Source1: net-tools-config.h
Source2: net-tools-config.make
Source3: ether-wake.c
Source4: ether-wake.8
Source5: mii-diag.c
Source6: mii-diag.8
Source7: iptunnel.8
Source8: ipmaddr.8
Source9: arp-ethers.service

Patch1: net-tools-cycle.patch

Patch2: net-tools-man.patch

Patch3: net-tools-linux48.patch

Patch20: ether-wake-interfaces.patch

Patch21: net-tools-ifconfig-EiB.patch
Patch22: net-tools-timer-man.patch
Patch23: net-tools-interface-name-len.patch
Patch24: net-tools-correct-exit-code.patch
Patch25: net-tools-spelling-error.patch
Patch26: net-tools-route-inet6-output.patch
Patch27: net-tools-iface-name-too-long.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: bluez-libs-devel
BuildRequires: gettext
BuildRequires: libselinux
BuildRequires: libselinux-devel
BuildRequires: systemd
%{?systemd_requires}

%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/ifconfig
%endif

%description
The net-tools package contains basic networking tools,
including ifconfig, netstat, route, and others.
Most of them are obsolete. For replacement check iproute package.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
echo '%{source6_hash}  %{SOURCE6}' | sha256sum -c -
echo '%{source7_hash}  %{SOURCE7}' | sha256sum -c -
echo '%{source8_hash}  %{SOURCE8}' | sha256sum -c -
echo '%{source9_hash}  %{SOURCE9}' | sha256sum -c -
%setup -q -c
%patch -P1 -p1 -b .cycle
%patch -P2 -p1 -b .man
%patch -P3 -p1 -b .linux48

cp %SOURCE1 ./config.h
cp %SOURCE2 ./config.make
cp %SOURCE3 .
cp %SOURCE4 ./man/en_US
cp %SOURCE5 .
cp %SOURCE6 ./man/en_US
cp %SOURCE7 ./man/en_US
cp %SOURCE8 ./man/en_US

%patch -P20 -p1 -b .interfaces
%patch -P21 -p1 -b .ifconfig-EiB
%patch -P22 -p1 -b .timer-man
%patch -P23 -p1 -b .interface-name-len
%patch -P24 -p1 -b .exit-codes
%patch -P25 -p1 -b .spelling
%patch -P26 -p1 -b .inet6-output
%patch -P27 -p1 -b .iface-name-too-long

touch ./config.h

%build
%ifarch sparcv9 sparc64 s390 s390x
export CFLAGS="${RPM_OPT_FLAGS} -fPIE"
%else
export CFLAGS="${RPM_OPT_FLAGS} -fpie"
%endif
export LDFLAGS="${RPM_LD_FLAGS} -pie -Wl,-z,now"

make
make ether-wake
gcc ${RPM_OPT_FLAGS} ${RPM_LD_FLAGS} -o mii-diag mii-diag.c

%install
mv man/de_DE man/de
mv man/fr_FR man/fr
mv man/pt_BR man/pt

make BASEDIR=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir} install

%if "%{_sbindir}" != "%{_bindir}"
mv %{buildroot}%{_bindir}/ifconfig %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/route %{buildroot}%{_sbindir}
%endif

install -p -m 755 ether-wake %{buildroot}%{_sbindir}
install -p -m 755 mii-diag %{buildroot}%{_sbindir}

rm %{buildroot}%{_sbindir}/rarp
rm %{buildroot}%{_mandir}/man8/rarp.8*
rm %{buildroot}%{_mandir}/de/man8/rarp.8*
rm %{buildroot}%{_mandir}/fr/man8/rarp.8*
rm %{buildroot}%{_mandir}/pt/man8/rarp.8*

rm -rf %{buildroot}%{_mandir}/de/man1
rm -rf %{buildroot}%{_mandir}/fr/man1
rm -rf %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}%{_mandir}/pt/man1
rm -rf %{buildroot}%{_mandir}/pt/man5

%if %{with remove_german_man8}
rm -rf %{buildroot}%{_mandir}/de/man8
%endif

%if %{with remove_french_man8}
rm -rf %{buildroot}%{_mandir}/fr/man8
%endif

install -D -p -m 644 %{SOURCE9} %{buildroot}%{_unitdir}/arp-ethers.service

%find_lang %{name} --all-name --with-man

%post
%systemd_post arp-ethers.service

%files -f %{name}.lang
%license COPYING
%{_bindir}/netstat
%{_sbindir}/ifconfig
%{_sbindir}/route
%{_sbindir}/arp
%{_sbindir}/ether-wake
%{_sbindir}/ipmaddr
%{_sbindir}/iptunnel
%{_sbindir}/mii-diag
%{_sbindir}/mii-tool
%{_sbindir}/nameif
%{_sbindir}/plipconfig
%{_sbindir}/slattach
%{_mandir}/man[58]/*

%attr(0644,root,root)   %{_unitdir}/arp-ethers.service

%changelog
%autochangelog
