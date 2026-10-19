%global source0_hash 782af149a446e0fb2b99ee3dd0bd51a468b4a0e2bd7848efd3f8599c9bd7a002
%global commit 5c21e8c75fbab53574275c8007f5af746e333144
%global commitdate 20210209
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Summary:        Display real-time system information on a 20x4 back-lit LCD
Name:           lcdproc
Version:        0.5.9
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            http://lcdproc.org
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        lcdproc.service
Source2:        lcdproc.target
Source3:        LCDd.service
Source4:        LCDd-hwdetect.service
Source5:        LCDd-hwdetect.sh
Source6:        90-lcdproc.rules
Source7:        lcdproc.sysusers
Patch1:         0001-server-drivers-g15-Add-support-for-the-LCD-on-Logite.patch
Patch99:        lcdproc-conf.patch
%ifnarch s390 s390x
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-dtds
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libftdi-devel
BuildRequires:  libg15render-devel
BuildRequires:  libhid-devel
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  lirc-devel
BuildRequires:  make
BuildRequires:  mx5000tools-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
# /oreon:deps
%description
LCDproc is a client/server suite including drivers for all
kinds of nifty LCD displays. The server supports several
serial devices: Matrix Orbital, Crystal Fontz, Bayrad, LB216,
LCDM001 (http://kernelconcepts.de), Wirz-SLI and PIC-an-LCD; and some
devices connected to the LPT port: HD44780, STV5730, T6963,
SED1520 and SED1330. Various clients are available that display
things like CPU load, system load, memory usage, up-time, and a lot more.
See also http://lcdproc.omnipotent.net.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}
# Fixup DriverPath
sed -i -e 's|server/drivers|%{_libdir}/lcdproc|' LCDd.conf
touch -r TODO LCDd.conf

%build

%define _lto_cflags -flto=auto -ffat-lto-objects
autoreconf -vif
%configure \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --enable-libusb \
  --enable-drivers=all \
  --enable-lcdproc-menus \
  --enable-stat-nfs \
  --enable-stat-smbfs \
  --with-lcdport=13666 \
  --with-pidfile-dir=/run
%make_build
%install
%make_install INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_bindir}/fortune.pl
rm $RPM_BUILD_ROOT%{_bindir}/iosock.pl
rm $RPM_BUILD_ROOT%{_bindir}/tail.pl
rm $RPM_BUILD_ROOT%{_bindir}/x11amp.pl
make install-html-guides DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/*-guide/*.proc
install -pm 0644 CREDITS.md ChangeLog.md README.md \
  $RPM_BUILD_ROOT%{_docdir}/%{name}
install -d $RPM_BUILD_ROOT%{_unitdir}
install -d $RPM_BUILD_ROOT%{_unitdir}/lcdproc.target.wants
install -d $RPM_BUILD_ROOT%{_udevrulesdir}
install -d $RPM_BUILD_ROOT%{_sysusersdir}
install -pm 0644 %{SOURCE1}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0644 %{SOURCE2}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0644 %{SOURCE3}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0644 %{SOURCE4}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0755 %{SOURCE5}  $RPM_BUILD_ROOT%{_sbindir}/LCDd-hwdetect
install -pm 0644 %{SOURCE6}  $RPM_BUILD_ROOT%{_udevrulesdir}
install -pm 0644 %{SOURCE7}  $RPM_BUILD_ROOT%{_sysusersdir}/lcdproc.conf
for i in lcdproc.service LCDd.service LCDd-hwdetect.service; do
  ln -s ../$i $RPM_BUILD_ROOT%{_unitdir}/lcdproc.target.wants
done
for f in LCDd.conf lcdproc.conf ; do
  mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${f} \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${f}.example
done
%oreon_autofiles main

%post

%systemd_post LCDd.service lcdproc.service
%preun

%systemd_preun LCDd.service lcdproc.service
%postun

%systemd_postun_with_restart LCDd.service lcdproc.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
