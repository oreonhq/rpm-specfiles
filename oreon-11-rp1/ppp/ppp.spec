%global _hardened_build 1

Name:    ppp
# Please be careful when bumping the ppp version. Several packages
# have version-tied dependencies on it, including NetworkManager-ppp
# (from NetworkManager) and NetworkManager-pptp , which are core
# packages. They may need code changes to build against new ppp
# versions. Please only bump ppp on a side tag and ensure it also
# contains rebuilds of at least those two packages before merging.
# Several other less important packages are also tied to the ppp
# version, as of 2023-04-19 the list is:
# NetworkManager-fortisslvpn
# NetworkManager-l2tp
# NetworkManager-ppp
# NetworkManager-pptp
# NetworkManager-sstp
# sstp-client
# These all need to be patched (if necessary) and rebuilt for new
# versions of ppp.
Version: 2.5.1
Release: 7%{?dist}
Summary: The Point-to-Point Protocol daemon
License: bsd-3-clause AND zlib AND licenseref-fedora-public-domain AND bsd-attribution-hpnd-disclaimer AND bsd-4.3tahoe AND bsd-4-clause-uc AND apache-2.0 AND lgpl-2.0-or-later AND (gpl-2.0-or-later OR bsd-2-clause OR bsd-3-clause OR bsd-4-clause) AND gpl-2.0-or-later AND xlock AND gpl-1.0-or-later AND mackerras-3-clause-acknowledgment AND mackerras-3-clause AND hpnd-fenneberg-Livingston AND sun-ppp AND hpnd-inria-imag AND sun-ppp-2000
URL:     http://www.samba.org/ppp

Source0: https://github.com/paulusmack/ppp/archive/ppp-%{version}.tar.gz
Source1: ppp-pam.conf
Source2: ppp-logrotate.conf
Source3: ppp-tmpfiles.conf
Source4: ip-down
Source5: ip-down.ipv6to4
Source6: ip-up
Source7: ip-up.ipv6to4
Source8: ipv6-down
Source9: ipv6-up
Source12: ppp-watch.tar.xz
Source13: ipv6-up.initscripts
Source14: ipv6-down.initscripts

# Fedora-specific
Patch0: ppp-2.5.0-use-change-resolv-function.patch
# Fix build with GCC 15
Patch1: ppp-2.5.1-gcc15.patch
# oreon url source checksums begin
%global source0_sha256 c0537067bdff5f0b5d7a2fd1cca13c220f6dadc89183f23739a2cf9df49c68ca
%global source0_file ppp-2.5.1.tar.gz
# oreon url source checksums end

BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: gcc
BuildRequires: pam-devel
BuildRequires: libpcap-devel
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: glib2-devel
BuildRequires: openssl-devel
BuildRequires: libxcrypt-devel
%if %{defined rhel} || 0%{?oreon}
Provides: bundled(linux-atm) = 2.4.1
%else
BuildRequires: linux-atm-libs-devel
%endif

Requires: glibc >= 2.0.6
Requires: /etc/pam.d/system-auth
Requires: libpcap >= 14:0.8.3-6
Requires: systemd

# Subpackage removed and obsoleted in F40
Obsoletes: network-scripts-ppp < %{version}-%{release}

%description
The ppp package contains the PPP (Point-to-Point Protocol) daemon and
documentation for PPP support. The PPP protocol provides a method for
transmitting datagrams over serial point-to-point links. PPP is
usually used to dial in to an ISP (Internet Service Provider) or other
organization over a modem and phone line.

%package devel
Summary: Headers for ppp plugin development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconf-pkg-config

%description devel
This package contains the header files for building plugins for ppp.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ppp-2.5.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c0537067bdff5f0b5d7a2fd1cca13c220f6dadc89183f23739a2cf9df49c68ca" || { echo "oreon: Source0 SHA256 mismatch for ppp-2.5.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{name}-%{name}-%{version}

tar -xJf %{SOURCE12}

# Create a sysusers.d config file
cat >ppp.sysusers.conf <<EOF
g dip 40
EOF

%build
autoreconf -fi
export CFLAGS="%{build_cflags} -fno-strict-aliasing"
%configure --enable-systemd --enable-cbcp --with-pam --disable-openssl-engine
%make_build
%make_build -C ppp-watch LDFLAGS="%{?build_ldflags} -pie"

%install
%make_install
find scripts -type f | xargs chmod a-x
make ROOT=%{buildroot} -C ppp-watch install

# create log files dir
install -d %{buildroot}%{_localstatedir}/log/ppp

# install pam config
install -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/ppp

# install logrotate script
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/ppp

# install tmpfiles drop-in
install -d %{buildroot}%{_tmpfilesdir}
install -m 644 -p %{SOURCE3} %{buildroot}%{_tmpfilesdir}/ppp.conf

# install scripts (previously owned by initscripts package)
install -d %{buildroot}%{_sysconfdir}/ppp
install -p %{SOURCE4} %{buildroot}%{_sysconfdir}/ppp/ip-down
install -p %{SOURCE5} %{buildroot}%{_sysconfdir}/ppp/ip-down.ipv6to4
install -p %{SOURCE6} %{buildroot}%{_sysconfdir}/ppp/ip-up
install -p %{SOURCE7} %{buildroot}%{_sysconfdir}/ppp/ip-up.ipv6to4
install -p %{SOURCE8} %{buildroot}%{_sysconfdir}/ppp/ipv6-down
install -p %{SOURCE9} %{buildroot}%{_sysconfdir}/ppp/ipv6-up
install -p %{SOURCE13} %{buildroot}%{_sysconfdir}/ppp/ipv6-down.initscripts
install -p %{SOURCE14} %{buildroot}%{_sysconfdir}/ppp/ipv6-up.initscripts

# ghosts
mkdir -p %{buildroot}%{_rundir}/pppd/lock

# fix configuration files suffix
pushd %{buildroot}%{_sysconfdir}/ppp
for f in `ls *.example`
do
  mv "$f" "${f%%.example}"
done
popd

%if "%{_sbindir}" == "%{_bindir}"
mv %{buildroot}/usr/sbin/ppp-watch %{buildroot}%{_bindir}/
%endif

install -m0644 -D ppp.sysusers.conf %{buildroot}%{_sysusersdir}/ppp.conf


%post
%tmpfiles_create ppp.conf

%files
%doc FAQ README README.cbcp README.linux README.MPPE README.MSCHAP80 README.MSCHAP81 README.pwfd README.pppoe scripts sample README.eap-tls
%{_sbindir}/chat
%{_sbindir}/pppd
%{_sbindir}/pppdump
%{_sbindir}/pppoe-discovery
%{_sbindir}/pppstats
%{_sbindir}/ppp-watch
%dir %{_sysconfdir}/ppp
%{_sysconfdir}/ppp/ip-up
%{_sysconfdir}/ppp/ip-down
%{_sysconfdir}/ppp/ip-up.ipv6to4
%{_sysconfdir}/ppp/ip-down.ipv6to4
%{_sysconfdir}/ppp/ipv6-up
%{_sysconfdir}/ppp/ipv6-up.initscripts
%{_sysconfdir}/ppp/ipv6-down
%{_sysconfdir}/ppp/ipv6-down.initscripts
%{_sysconfdir}/ppp/openssl.cnf
%{_mandir}/man8/chat.8*
%{_mandir}/man8/pppd.8*
%{_mandir}/man8/pppdump.8*
%{_mandir}/man8/pppd-radattr.8*
%{_mandir}/man8/pppd-radius.8*
%{_mandir}/man8/pppstats.8*
%{_mandir}/man8/pppoe-discovery.8*
%{_mandir}/man8/ppp-watch.8*
%{_libdir}/pppd
%ghost %dir %{_rundir}/pppd
%ghost %dir %{_rundir}/pppd/lock
%dir %{_sysconfdir}/logrotate.d
%attr(700, root, root) %dir %{_localstatedir}/log/ppp
%config(noreplace) %{_sysconfdir}/ppp/eaptls-client
%config(noreplace) %{_sysconfdir}/ppp/eaptls-server
%config(noreplace) %{_sysconfdir}/ppp/chap-secrets
%config(noreplace) %{_sysconfdir}/ppp/options
%config(noreplace) %{_sysconfdir}/ppp/pap-secrets
%config(noreplace) %{_sysconfdir}/pam.d/ppp
%config(noreplace) %{_sysconfdir}/logrotate.d/ppp
%{_tmpfilesdir}/ppp.conf
%{_sysusersdir}/ppp.conf

%files devel
%{_includedir}/pppd
%doc PLUGINS
%{_libdir}/pkgconfig/pppd.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.1-7
- Import
