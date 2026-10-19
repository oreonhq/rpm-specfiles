%global source0_hash 2853e41d9cdd61db28ec1e690912e1e5f596e047e3242841a07da1b30d89e2c1
%global source12_hash bb010722c2cd5d919945a929f1ee9ade18658791d12db53f8010351d91eed32d
%global _hardened_build 1
Name:    ppp
Version: 2.5.4
Release:        1%{?dist}
Summary:        The Point-to-Point Protocol daemon
License: bsd-3-clause AND zlib AND licenseref-fedora-public-domain AND bsd-attribution-hpnd-disclaimer AND bsd-4.3tahoe AND bsd-4-clause-uc AND apache-2.0 AND lgpl-2.0-or-later AND (gpl-2.0-or-later OR bsd-2-clause OR bsd-3-clause OR bsd-4-clause) AND gpl-2.0-or-later AND xlock AND gpl-1.0-or-later AND mackerras-3-clause-acknowledgment AND mackerras-3-clause AND hpnd-fenneberg-Livingston AND sun-ppp AND hpnd-inria-imag AND sun-ppp-2000
URL:     http://www.samba.org/ppp
Source0:        https://github.com/paulusmack/ppp/archive/v%{version}/ppp-%{version}.tar.gz
Source1:        ppp-pam.conf
Source2:        ppp-logrotate.conf
Source3:        ppp-tmpfiles.conf
Source4:        ip-down
Source5:        ip-down.ipv6to4
Source6:        ip-up
Source7:        ip-up.ipv6to4
Source8:        ipv6-down
Source9:        ipv6-up
Source12:        ppp-watch.tar.xz
Source13:        ipv6-up.initscripts
Source14:        ipv6-down.initscripts
%if %{defined rhel} || (0%{?oreon} >= 11)
Provides: bundled(linux-atm) = 2.4.1
%else
%endif
Requires: glibc >= 2.0.6
Requires: /etc/pam.d/system-auth
Requires: libpcap >= 14:0.8.3-6
Requires: systemd
Obsoletes: network-scripts-ppp < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  linux-atm-libs-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

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
install -d %{buildroot}%{_localstatedir}/log/ppp
install -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/ppp
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/ppp
install -d %{buildroot}%{_tmpfilesdir}
install -m 644 -p %{SOURCE3} %{buildroot}%{_tmpfilesdir}/ppp.conf
install -d %{buildroot}%{_sysconfdir}/ppp
install -p %{SOURCE4} %{buildroot}%{_sysconfdir}/ppp/ip-down
install -p %{SOURCE5} %{buildroot}%{_sysconfdir}/ppp/ip-down.ipv6to4
install -p %{SOURCE6} %{buildroot}%{_sysconfdir}/ppp/ip-up
install -p %{SOURCE7} %{buildroot}%{_sysconfdir}/ppp/ip-up.ipv6to4
install -p %{SOURCE8} %{buildroot}%{_sysconfdir}/ppp/ipv6-down
install -p %{SOURCE9} %{buildroot}%{_sysconfdir}/ppp/ipv6-up
install -p %{SOURCE13} %{buildroot}%{_sysconfdir}/ppp/ipv6-down.initscripts
install -p %{SOURCE14} %{buildroot}%{_sysconfdir}/ppp/ipv6-up.initscripts
mkdir -p %{buildroot}%{_rundir}/pppd/lock
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%tmpfiles_create ppp.conf
%files -f %{oreon_filedir}/main.list
%files -n ppp-devel -f %{oreon_filedir}/ppp-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.1-7
- Import
