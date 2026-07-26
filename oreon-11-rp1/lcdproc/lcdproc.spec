%global source0_hash 782af149a446e0fb2b99ee3dd0bd51a468b4a0e2bd7848efd3f8599c9bd7a002

%global commit 5c21e8c75fbab53574275c8007f5af746e333144
%global commitdate 20210209
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:        Display real-time system information on a 20x4 back-lit LCD
Name:           lcdproc
Version:        0.5.9
Release:        27.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
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
# lcdconf.conf tweaks:
# 1. Enable ProcSize, this is quite useful to have
# 2. Disable TimeDate, its info is duplicate with the MiniClock and it is ugly
# 3. Disable network interface screen by default, since Fedora uses predictable
#    network interface names, having a simple default like Interface0=eth0 does
#    not work
Patch99:        lcdproc-conf.patch

BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
BuildRequires:  doxygen
BuildRequires:  graphviz

BuildRequires:  freetype-devel
%ifnarch s390 s390x
BuildRequires:  libhid-devel
%endif
BuildRequires:  libusb1-devel
BuildRequires:  lirc-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  xmlto
BuildRequires:  docbook-dtds
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libftdi-devel
BuildRequires:  libg15render-devel
BuildRequires:  mx5000tools-devel
BuildRequires:  libtool autoconf automake
BuildRequires:  gcc make

%{?systemd_requires}

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
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful in a LTO
# build.  We can force code generation with the -ffat-lto-objects to make
# the test work as expected.
#
# -ffat-lto-objects is the default for F33, but will not be for F34, so we
# make it explicit here.
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
# remove non useful (and not "lcd" prefixed) perl example scripts
rm $RPM_BUILD_ROOT%{_bindir}/fortune.pl
rm $RPM_BUILD_ROOT%{_bindir}/iosock.pl
rm $RPM_BUILD_ROOT%{_bindir}/tail.pl
rm $RPM_BUILD_ROOT%{_bindir}/x11amp.pl

# docs
make install-html-guides DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/*-guide/*.proc
install -pm 0644 CREDITS.md ChangeLog.md README.md \
  $RPM_BUILD_ROOT%{_docdir}/%{name}

# init
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

#Disable default configuration
#Thoses are only provided as an example since ncurses isn't a suitable default configuration.
for f in LCDd.conf lcdproc.conf ; do
  mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${f} \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${f}.example
done

%post
%systemd_post LCDd.service lcdproc.service

%preun
%systemd_preun LCDd.service lcdproc.service

%postun
%systemd_postun_with_restart LCDd.service lcdproc.service

%files
%doc %{_docdir}/%{name}
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/lcdproc/
%{_mandir}/man?/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*.conf
%config %{_sysconfdir}/%{name}/*.conf.example
%{_unitdir}/*
%{_udevrulesdir}/90-%{name}.rules
%{_sysusersdir}/lcdproc.conf

%changelog
%autochangelog
