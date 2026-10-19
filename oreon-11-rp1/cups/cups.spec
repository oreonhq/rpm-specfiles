%global source3_hash 27e8a3bb39b1b0754913601ca3974d5266025515becdc674ad8429805fe16852
%global source0_hash 820984b12a67f98705785aae2dd1347fe0ac097828001d4583ff64574aed6389
%global use_alternatives 1
%global lspp 1 
%global cups_serverbin %{_exec_prefix}/lib/cups
%global VERSION %{version}
Summary:        CUPS printing system
Name: cups
Epoch: 1
Version: 2.4.19
Release:        1%{?dist}
License: Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND Zlib AND BSD-2-Clause
Url: https://openprinting.github.io/cups/
Source0:        https://github.com/OpenPrinting/%{name}/releases/download/v%{version}/%{name}-%{version}-source.tar.gz
Source1: cupsprinter.png
Source2: macros.cups
Source3:        https://github.com/OpenPrinting/cups/releases/download/v%{VERSION}/cups-%{VERSION}-source.tar.gz.sig
Patch1: cups-multilib.patch
Patch2: cups-banners.patch
Patch3: cups-no-export-ssllibs.patch
Patch4: cups-direct-usb.patch
Patch5: cups-driverd-timeout.patch
Patch6: cups-usb-paperout.patch
Patch7: cups-uri-compat.patch
Patch8: cups-freebind.patch
Patch9: cups-ipp-multifile.patch
Patch10: cups-web-devices-timeout.patch
Patch11: cups-failover-backend.patch
Patch12: cups-dymo-deviceid.patch
Patch100: cups-lspp.patch
Conflicts: %{name}-filesystem < 1:2.4.11-3
Recommends: avahi
Recommends: cups-browsed
Recommends: ipp-usb
Recommends: cups-filters-driverless
Requires: authselect-libs
Requires: acl
Requires: %{name}-client%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-filesystem = %{epoch}:%{version}-%{release}
Requires: cups-filters
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: dbus
Requires: setup
Requires: systemd
Requires(pre): systemd
Requires(post): systemd
Requires(post): grep, sed
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  authselect-libs
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  python3-cups
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%package client
Summary: CUPS printing system - client programs
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides: /usr/bin/lpq /usr/bin/lpr /usr/bin/lp /usr/bin/cancel /usr/bin/lprm /usr/bin/lpstat
Requires: /usr/sbin/alternatives
Provides: lpr
%package devel
Summary: CUPS printing system - development environment
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gnutls-devel
Requires: krb5-devel
Requires: pkgconf-pkg-config
Requires: zlib-devel
%package libs
Summary: CUPS printing system - libraries
Requires: %{name}-filesystem = %{epoch}:%{version}-%{release}
Requires: avahi-libs%{?_isa}
%package filesystem
Summary: CUPS printing system - directory layout
BuildArch: noarch
Conflicts: %{name} < 1:2.4.11-3
%package lpd
Summary: CUPS printing system - lpd emulation
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides: lpd
%package ipptool
Summary: CUPS printing system - tool for performing IPP requests
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: avahi
%package printerapp
Summary: CUPS printing system - tools for printer application
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: avahi
%description
CUPS printing system provides a portable printing layer for
UNIX® operating systems. It has been developed by Apple Inc.
to promote a standard printing solution for all UNIX vendors and users.
CUPS provides the System V and Berkeley command-line interfaces.

%description client
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This package contains command-line client
programs.

%description devel
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This is the development package for creating
additional printer drivers, and other CUPS services.

%description libs
CUPS printing system provides a portable printing layer for
UNIX® operating systems. It has been developed by Apple Inc.
to promote a standard printing solution for all UNIX vendors and users.
CUPS provides the System V and Berkeley command-line interfaces.
The cups-libs package provides libraries used by applications to use CUPS
natively, without needing the lp/lpr commands.

%description filesystem
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This package provides some directories which are
required by other packages that add CUPS drivers (i.e. filters, backends etc.).

%description lpd
CUPS printing system provides a portable printing layer for
UNIX® operating systems. This is the package that provides standard
lpd emulation.

%description ipptool
Sends IPP requests to the specified URI and tests and/or displays the results.

%description printerapp
Provides IPP everywhere printer application ippeveprinter and tools for printing
PostScript and HP PCL document formats - ippevepcl and ippeveps. The printer
application enables older printers for IPP everywhere standard - so if older printer
is installed with a printer application, its print queue acts as IPP everywhere printer
to CUPS daemon. This solution will substitute printer drivers and raw queues in the future.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n cups-%{VERSION}
# Prevent multilib conflict in cups-config script.
%patch -P 1 -p1 -b .multilib
# Ignore rpm save/new files in the banners directory.
%patch -P 2 -p1 -b .banners
# Don't export SSLLIBS to cups-config.
%patch -P 3 -p1 -b .no-export-ssllibs
# Allow file-based usb device URIs.
%patch -P 4 -p1 -b .direct-usb
# Increase driverd timeout to 70s to accommodate foomatic (bug #744715).
%patch -P 5 -p1 -b .driverd-timeout
# Support for errno==ENOSPACE-based USB paper-out reporting.
%patch -P 6 -p1 -b .usb-paperout
# Allow the usb backend to understand old-style URI formats.
%patch -P 7 -p1 -b .uri-compat
# Use IP_FREEBIND socket option when binding listening sockets (bug #970809).
%patch -P 8 -p1 -b .freebind
# Fixes for jobs with multiple files and multiple formats.
%patch -P 9 -p1 -b .ipp-multifile
# Increase web interface get-devices timeout to 10s (bug #996664).
%patch -P 10 -p1 -b .web-devices-timeout
# Add failover backend (bug #1689209)
%patch -P 11 -p1 -b .failover
# Added IEEE 1284 Device ID for a Dymo device (bug #747866).
%patch -P 12 -p1 -b .dymo-deviceid

# LSPP support.
%patch -P 100 -p1 -b .lspp

# UPSTREAM PATCHES

# Log to the system journal by default (bug #1078781, bug #1519331).
sed -i -e 's,^ErrorLog .*$,ErrorLog syslog,' conf/cups-files.conf.in
sed -i -e 's,^AccessLog .*$,AccessLog syslog,' conf/cups-files.conf.in
sed -i -e 's,^PageLog .*,PageLog syslog,' conf/cups-files.conf.in

# Let's look at the compilation command lines.
perl -pi -e "s,^.SILENT:,," Makedefs.in

# remove this once we don't have any patches changing configure stuff
aclocal -I config-scripts
autoconf -f -I config-scripts

%build

export CC=%{__cc}
export CXX=%{__cxx}
export DSOFLAGS="$DSOFLAGS $RPM_LD_FLAGS"
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS -DLDAP_DEPRECATED=1"
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS -DLDAP_DEPRECATED=1"
%configure --with-docdir=%{_datadir}/%{name}/www \
  --enable-debug \
  --enable-gssapi \
  --enable-lspp \
  --enable-page-logging \
  --enable-relro \
  --enable-sync-on-close \
  --enable-webif \
  --with-access-log-level=actions \
  --with-cupsd-file-perm=0755 \
  --with-dbusdir=%{_sysconfdir}/dbus-1 \
  --with-dnssd=avahi \
  --with-log-file-perm=0600 \
  --with-ondemand=systemd \
  --with-pkgconfpath=%{_libdir}/pkgconfig \
  --with-rundir=%{_rundir}/cups \
  --with-tls=gnutls \
  --with-xinetd=no \
  --localedir=%{_datadir}/locale
%make_build
%install
make install DESTDIR=%{buildroot}
rm -rf	%{buildroot}%{_initddir} \
	%{buildroot}%{_sysconfdir}/init.d \
	%{buildroot}%{_sysconfdir}/rc?.d
mkdir -p %{buildroot}%{_unitdir}
find %{buildroot}%{_datadir}/cups/model -name "*.ppd" |xargs gzip -n9f
pushd %{buildroot}%{_datadir}/%{name}/ipptool
for file in color.jpg document-a4.pdf document-a4.ps document-letter.pdf document-letter.ps gray.jpg onepage-a4.pdf onepage-a4.ps onepage-letter.pdf onepage-letter.ps testfile.jpg testfile.pcl testfile.pdf testfile.ps testfile.txt
do
  mv $file{,.gz}
done
popd
pushd %{buildroot}%{_bindir}
for i in cancel lp lpq lpr lprm lpstat; do
	mv $i $i.cups
done
cd %{buildroot}%{_sbindir}
mv lpc lpc.cups
cd %{buildroot}%{_mandir}/man1
for i in cancel lp lpq lpr lprm lpstat; do
	mv $i.1 $i-cups.1
done
cd %{buildroot}%{_mandir}/man8
mv lpc.8 lpc-cups.8
popd
mkdir -p %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_sysconfdir}/X11/sysconfig %{buildroot}%{_sysconfdir}/X11/applnk/System
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -m 0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d
touch %{buildroot}%{_sysconfdir}/cups/printers.conf
touch %{buildroot}%{_sysconfdir}/cups/classes.conf
touch %{buildroot}%{_sysconfdir}/cups/client.conf
touch %{buildroot}%{_sysconfdir}/cups/subscriptions.conf
touch %{buildroot}%{_sysconfdir}/cups/lpoptions
cat > %{buildroot}%{_sysconfdir}/cups/client.conf <<EOF
DigestOptions DenyMD5
EOF
mkdir -p %{buildroot}%{_datadir}/ppd
rm -rf %{buildroot}%{_mandir}/cat? %{buildroot}%{_mandir}/*/cat?
rm -f %{buildroot}%{_datadir}/applications/cups.desktop
rm -rf %{buildroot}%{_datadir}/icons
rm -rf %{buildroot}%{_datadir}/cups/banners
rm -f %{buildroot}%{_datadir}/cups/data/testprint
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/cups.conf <<EOF
d %{_rundir}/cups 0755 root lp -
d %{_rundir}/cups/certs 0511 lp sys -
d /var/spool/cups/tmp - - - 30d
d /var/log/cups 0755 root lp -
EOF
cat > %{buildroot}%{_tmpfilesdir}/cups-lp.conf <<EOF
c /dev/lp0 0660 root lp - 6:0
c /dev/lp1 0660 root lp - 6:1
c /dev/lp2 0660 root lp - 6:2
c /dev/lp3 0660 root lp - 6:3
EOF
find %{buildroot} -type f -o -type l | sed '
s:.*\('%{_datadir}'/\)\([^/_]\+\)\(.*\.po$\):%lang(\2) \1\2\3:
/^%lang(C)/d
/^\([^%].*\)/d
' > %{name}.lang
%oreon_autofiles cups-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cups-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cups-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cups-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cups-lpd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cups-ipptool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cups-printerapp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.path %{name}.socket %{name}.service
%pre client

%if 0%{?fedora} >= 42 || 0%{?rhel} > 10 || 0%{?oreon} >= 11
  if [ $1 -gt 1 ] ; then
    %{_sbindir}/alternatives --remove-follower print %{_bindir}/lpr.cups print-lpc || :
  fi
%endif
%post client

  %{_sbindir}/alternatives --install %{_bindir}/lpr print %{_bindir}/lpr.cups 40 \
	  --follower %{_bindir}/lp print-lp %{_bindir}/lp.cups \
	  --follower %{_bindir}/lpq print-lpq %{_bindir}/lpq.cups \
	  --follower %{_bindir}/lprm print-lprm %{_bindir}/lprm.cups \
	  --follower %{_bindir}/lpstat print-lpstat %{_bindir}/lpstat.cups \
	  --follower %{_bindir}/cancel print-cancel %{_bindir}/cancel.cups \
	  --follower %{_sbindir}/lpc print-lpc %{_sbindir}/lpc.cups \
	  --follower %{_mandir}/man1/cancel.1.gz print-cancelman %{_mandir}/man1/cancel-cups.1.gz \
	  --follower %{_mandir}/man1/lp.1.gz print-lpman %{_mandir}/man1/lp-cups.1.gz \
	  --follower %{_mandir}/man8/lpc.8.gz print-lpcman %{_mandir}/man8/lpc-cups.8.gz \
	  --follower %{_mandir}/man1/lpq.1.gz print-lpqman %{_mandir}/man1/lpq-cups.1.gz \
	  --follower %{_mandir}/man1/lpr.1.gz print-lprman %{_mandir}/man1/lpr-cups.1.gz \
	  --follower %{_mandir}/man1/lprm.1.gz print-lprmman %{_mandir}/man1/lprm-cups.1.gz \
	  --follower %{_mandir}/man1/lpstat.1.gz print-lpstatman %{_mandir}/man1/lpstat-cups.1.gz || :
  %if 0%{?fedora} >= 42 || 0%{?rhel} > 10 || 0%{?oreon} >= 11
    %if "%{_sbindir}" == "%{_bindir}"
      test -h /usr/sbin || ln -s ../bin/lpc /usr/sbin/lpc 2>/dev/null || :
    %endif
  %endif
%post lpd

%systemd_post cups-lpd.socket
%ldconfig_scriptlets libs
%preun

%systemd_preun %{name}.path %{name}.socket %{name}.service
%preun client

if [ $1 -eq 0 ] ; then
	/usr/sbin/alternatives --remove print %{_bindir}/lpr.cups || :
fi
%preun lpd

%systemd_preun cups-lpd.socket
%postun

%systemd_postun_with_restart %{name}.path %{name}.socket %{name}.service
%postun lpd

%systemd_postun_with_restart cups-lpd.socket
%triggerin -- samba-client

ln -sf %{_libexecdir}/samba/cups_backend_smb %{cups_serverbin}/backend/smb || :
%triggerun -- samba-client

[ $2 = 0 ] || exit 0
rm -f %{cups_serverbin}/backend/smb
%files -f %{oreon_filedir}/main.list
%files -n cups-client -f %{oreon_filedir}/cups-client.list
%files -n cups-devel -f %{oreon_filedir}/cups-devel.list
%files -n cups-libs -f %{oreon_filedir}/cups-libs.list
%files -n cups-filesystem -f %{oreon_filedir}/cups-filesystem.list
%files -n cups-lpd -f %{oreon_filedir}/cups-lpd.list
%files -n cups-ipptool -f %{oreon_filedir}/cups-ipptool.list
%files -n cups-printerapp -f %{oreon_filedir}/cups-printerapp.list

%changelog

%autochangelog
