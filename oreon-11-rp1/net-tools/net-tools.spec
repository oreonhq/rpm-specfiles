%global source0_hash 4c2653b5f16b277dd6f1459e3e56c55e8bb19ed8cf2b5e60f6174ead3bbede0e
%global checkout 20160912git
%if !0%{?fedora} || 0%{?fedora} >= 44 || (0%{?oreon} >= 11)
%bcond remove_german_man8 1
%bcond remove_french_man8 1
%else
%bcond remove_german_man8 0
%bcond remove_french_man8 0
%endif
Summary:        Basic networking tools
Name: net-tools
Version: 2.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://sourceforge.net/projects/net-tools/
Source0:        %{name}-%{version}.%{checkout}.tar.xz
Source1:        net-tools-config.h
Source2:        net-tools-config.make
Source3:        ether-wake.c
Source4:        ether-wake.8
Source5:        mii-diag.c
Source6:        mii-diag.8
Source7:        iptunnel.8
Source8:        ipmaddr.8
Source9:        arp-ethers.service
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
%{?systemd_requires}
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/ifconfig
%endif
# oreon:deps
BuildRequires:  bluez-libs-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libselinux
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
The net-tools package contains basic networking tools,
including ifconfig, netstat, route, and others.
Most of them are obsolete. For replacement check iproute package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%post

%systemd_post arp-ethers.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0-0.77.20160912git
- Import
