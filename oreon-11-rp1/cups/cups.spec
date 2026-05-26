%global use_alternatives 1
%global lspp 1 

# {_exec_prefix}/lib/cups is correct, even on x86_64.
# It is not used for shared objects but for executables.
# It's more of a libexec-style ({_libexecdir}) usage,
# but we use lib for compatibility with 3rd party drivers (at upstream request).
%global cups_serverbin %{_exec_prefix}/lib/cups

#%%global prever rc1
#%%global VERSION %%{version}%%{prever}
%global VERSION %{version}

Summary: CUPS printing system
Name: cups
Epoch: 1
Version: 2.4.16
Release: 8%{?dist}
# backend/failover.c - BSD-3-Clause
# cups/md5* - Zlib
# scheduler/colorman.c - Apache-2.0 WITH LLVM-exception AND BSD-2-Clause
# * - Apache-2.0 WITH LLVM-exception
# the CUPS exception text is the same as LLVM exception, so using that name with
# agreement from legal team
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/A7GFSD6M3GYGSI32L2FC5KB22DUAEQI3/
License: Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND Zlib AND BSD-2-Clause
Url: https://openprinting.github.io/cups/
# Apple stopped uploading the new versions into github, use OpenPrinting fork
Source0: https://github.com/OpenPrinting/cups/releases/download/v%{VERSION}/cups-%{VERSION}-source.tar.gz
# Pixmap for desktop file
Source1: cupsprinter.png
# cups_serverbin macro definition for use during builds
Source2: macros.cups
# GPG signature for validating tarball
Source3: https://github.com/OpenPrinting/cups/releases/download/v%{VERSION}/cups-%{VERSION}-source.tar.gz.sig

# cups-config from devel package conflicted on multilib arches,
# fixed hack with pkg-config calling for gnutls' libdir variable
Patch1: cups-multilib.patch
# if someone makes a change to banner files, then there will <banner>.rpmnew
# with next update of cups-filters - this patch makes sure the banner file 
# changed by user is used and .rpmnew or .rpmsave is ignored
# Note: This could be rewrite with use a kind of #define and send to upstream
Patch2: cups-banners.patch
# don't export ssl libs to cups-config - can't find the reason.
Patch3: cups-no-export-ssllibs.patch
# enables old uri usb:/dev/usb/lp0 - leave it here for users of old printers
Patch4: cups-direct-usb.patch
# when system workload is high, timeout for cups-driverd can be reached -
# increase the timeout
Patch5: cups-driverd-timeout.patch
# usb backend didn't get any notification about out-of-paper because of kernel 
Patch6: cups-usb-paperout.patch
# uri compatibility with old Fedoras
Patch7: cups-uri-compat.patch
# use IP_FREEBIND, because cupsd cannot bind to not yet existing IP address
# by default
Patch8: cups-freebind.patch
# add support of multifile
Patch9: cups-ipp-multifile.patch
# prolongs web ui timeout
Patch10: cups-web-devices-timeout.patch
# failover backend for implementing failover functionality
# TODO: move it to the cups-filters upstream
Patch11: cups-failover-backend.patch
# add device id for dymo printer
Patch12: cups-dymo-deviceid.patch

%if %{lspp}
# selinux and audit enablement for CUPS - needs work and CUPS upstream wants
# to have these features implemented their way in the future
Patch100: cups-lspp.patch
%endif

#### UPSTREAM PATCHES (starts with 1000) ####
Patch1000: 0001-scheduler-Fix-possible-use_after_free-in-cupsdReadCl.patch
Patch1001: 0001-tls-gnutls.c-Do-not-check-for-errno-after-I-O-operat.patch
# oreon url source checksums begin
%global source0_sha256 0339587204b4f9428dd0592eb301dec0bf9ea6ea8dce5d9690d56be585aba92d
%global source0_file cups-2.4.16-source.tar.gz
# oreon url source checksums end


##### Patches removed because IMHO they aren't no longer needed
##### but still I'll leave them in git in case their removal
##### breaks something. 


# we need /etc/pam.d/password-auth or /etc/pam.d/system-auth in buildroot sooner or later,
# provided by authselect-libs atm
BuildRequires: authselect-libs
BuildRequires: automake
# gcc and gcc-c++ is no longer in buildroot by default
# gcc for most of files
BuildRequires: gcc
# gcc-c++ for ppdc and cups-driverd
Buildrequires: gcc-c++ 
BuildRequires: krb5-devel
BuildRequires: libacl-devel
# make is used for compilation
BuildRequires: make
BuildRequires: openldap-devel
BuildRequires: pam-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libusb-1.0)
# Make sure we get postscriptdriver tags.
BuildRequires: python3-cups
BuildRequires: systemd
# needed for systemd rpm macros according FPG
BuildRequires: systemd-rpm-macros
# needed for decompressing functions when reading from gzipped ppds
BuildRequires: zlib-devel

%if %{lspp}
BuildRequires: libselinux-devel
BuildRequires: audit-libs-devel
%endif

# /etc/cups/ssl was moved from main package to filesystem package
# remove once CentOS Stream 11 is released
Conflicts: %{name}-filesystem < 1:2.4.11-3

# getaddrinfo from glibc needs nss-mdns or systemd-resolved for resolving
# mdns .local addresses. Don't require a specific package for now and let
# the user to decide what to use
# just recommend nss-mdns for Fedora for now to have working default, but
# don't hardwire it for resolved users
%if 0%{?fedora}
Recommends: nss-mdns
%endif
# avahi is needed for mDNS discovery and sharing queues
Recommends: avahi
# for better migration - cups-browsed was part of cups-filters in the past,
# now it was splitted and no longer depends on cups-filters - the daemon will
# vanish during upgrade without a weak dependency at least
Recommends: cups-browsed
# for IPP-over-USB device support
Recommends: ipp-usb
# driverless stuff was splitted from cups-filters
Recommends: cups-filters-driverless

# we use password-auth or system-auth PAM modules for authentication,
# provided by authselect-libs
Requires: authselect-libs
# We ship udev rules which use setfacl.
Requires: acl
Requires: %{name}-client%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-filesystem = %{epoch}:%{version}-%{release}
# Make sure we have some filters for converting to raster format.
Requires: cups-filters
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: dbus
# uses user+group lp
Requires: setup
Requires: systemd

# Requires working PrivateTmp (bug #807672)
Requires(pre): systemd
Requires(post): systemd
Requires(post): grep, sed
Requires(preun): systemd
Requires(postun): systemd


%package client
Summary: CUPS printing system - client programs
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%if %{use_alternatives}
Provides: /usr/bin/lpq /usr/bin/lpr /usr/bin/lp /usr/bin/cancel /usr/bin/lprm /usr/bin/lpstat
Requires: /usr/sbin/alternatives
%endif
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
# /etc/cups/ssl was moved from main package to filesystem package
# remove once CentOS Stream 11 is released
Conflicts: %{name} < 1:2.4.11-3


%package lpd
Summary: CUPS printing system - lpd emulation
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides: lpd

%package ipptool
Summary: CUPS printing system - tool for performing IPP requests
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# ippfind needs avahi for printer discovery
Requires: avahi
# mdns address resolver (nss-mdns or systemd-resolved) is needed too,
# but don't require a specific package for now and let the user to choose
# what to use
# just recommend nss-mdns for Fedora for now to have working default, but
# don't hardwire it for resolved users
%if 0%{?fedora}
Recommends: nss-mdns
%endif

%package printerapp
Summary: CUPS printing system - tools for printer application
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# ippeveprinter needs avahi for registering and sharing printer
Requires: avahi
# mdns address resolver (nss-mdns or systemd-resolved) is needed too,
# but don't require a specific package for now and let the user to choose
# what to use
# just recommend nss-mdns for Fedora for now to have working default, but
# don't hardwire it for resolved users
%if 0%{?fedora}
Recommends: nss-mdns
%endif

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cups-2.4.16-source.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0339587204b4f9428dd0592eb301dec0bf9ea6ea8dce5d9690d56be585aba92d" || { echo "oreon: Source0 SHA256 mismatch for cups-2.4.16-source.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

%if %{lspp}
# LSPP support.
%patch -P 100 -p1 -b .lspp
%endif

# UPSTREAM PATCHES
%patch -P 1000 -p1 -b .osh-use-after-free
%patch -P 1001 -p1 -b .osh-use-after-free


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
# cups can use different compiler if it is installed, so set to GCC for to be sure
export CC=%{__cc}
export CXX=%{__cxx}
# add Fedora specific flags to DSOFLAGS
export DSOFLAGS="$DSOFLAGS $RPM_LD_FLAGS"
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS -DLDAP_DEPRECATED=1"
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS -DLDAP_DEPRECATED=1"
# --enable-debug to avoid stripping binaries
%configure --with-docdir=%{_datadir}/%{name}/www \
  --enable-debug \
  --enable-gssapi \
%if %{lspp}
  --enable-lspp \
%endif
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
%if 0%{?rhel}
  --without-idle-exit-timeout \
  --without-systemd-timeoutstartsec \
%endif
  --localedir=%{_datadir}/locale

# If we got this far, all prerequisite libraries must be here.
%make_build

%install
# %%make_install macro results into permission error during install phase,
# because it sets INSTALL env to 'install -p'.
# use the old make invocation for now, fix this upstream when upstream will
# have a time for github issues
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

%if %{use_alternatives}
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
%endif

mkdir -p %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_sysconfdir}/X11/sysconfig %{buildroot}%{_sysconfdir}/X11/applnk/System
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

# Ship an rpm macro for where to put driver executables.
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -m 0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d

# Ship a printers.conf file, and a client.conf file.  That way, they get
# their SELinux file contexts set correctly.
touch %{buildroot}%{_sysconfdir}/cups/printers.conf
touch %{buildroot}%{_sysconfdir}/cups/classes.conf
touch %{buildroot}%{_sysconfdir}/cups/client.conf
touch %{buildroot}%{_sysconfdir}/cups/subscriptions.conf
touch %{buildroot}%{_sysconfdir}/cups/lpoptions

# deny MD5 digest authentication by default in client.conf
cat > %{buildroot}%{_sysconfdir}/cups/client.conf <<EOF
# MD5 Digest authentication is turned off by default
# because MD5 is marked as insecure for authentication.
#
# If you need MD5 Digest authentication and you are aware of
# potential security risk, turn MD5 Digest authentication on
# by changing the directive value to 'None'.

DigestOptions DenyMD5
EOF

# LSB 3.2 printer driver directory
mkdir -p %{buildroot}%{_datadir}/ppd

# Remove unshipped files.
rm -rf %{buildroot}%{_mandir}/cat? %{buildroot}%{_mandir}/*/cat?
rm -f %{buildroot}%{_datadir}/applications/cups.desktop
rm -rf %{buildroot}%{_datadir}/icons
# there are pdf-banners shipped with cups-filters (#919489)
rm -rf %{buildroot}%{_datadir}/cups/banners
rm -f %{buildroot}%{_datadir}/cups/data/testprint

# install /usr/lib/tmpfiles.d/cups.conf (bug #656566, bug #893834)
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/cups.conf <<EOF
# See tmpfiles.d(5) for details

d %{_rundir}/cups 0755 root lp -
d %{_rundir}/cups/certs 0511 lp sys -

d /var/spool/cups/tmp - - - 30d

d /var/log/cups 0755 root lp -
EOF

# /usr/lib/tmpfiles.d/cups-lp.conf (bug #812641)
cat > %{buildroot}%{_tmpfilesdir}/cups-lp.conf <<EOF
# Legacy parallel port character device nodes, to trigger the
# auto-loading of the kernel module on access.
#
# See tmpfiles.d(5) for details

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

%post
# required for systemd units
%systemd_post %{name}.path %{name}.socket %{name}.service

%pre client
# remove alternatives workaround once C11S is released
%if 0%{?fedora} >= 42 || 0%{?rhel} > 10
  %if %{use_alternatives}
  # only run on upgrade (not fresh install)
  if [ $1 -gt 1 ] ; then
    %{_sbindir}/alternatives --remove-follower print %{_bindir}/lpr.cups print-lpc || :
  fi
  %endif
%endif

%post client
%if %{use_alternatives}
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

  # remove sbin symlink creation once C11S is released
  %if 0%{?fedora} >= 42 || 0%{?rhel} > 10
    %if "%{_sbindir}" == "%{_bindir}"
      # Make sure that the symlink in /usr/sbin/ is not missing, if /usr/sbin is a
      # directory. The symlink will only be created if there is no symlink
      # or file already.
      test -h /usr/sbin || ln -s ../bin/lpc /usr/sbin/lpc 2>/dev/null || :
    %endif
  %endif
%endif

%post lpd
%systemd_post cups-lpd.socket

%ldconfig_scriptlets libs

%preun
%systemd_preun %{name}.path %{name}.socket %{name}.service

%preun client
%if %{use_alternatives}
if [ $1 -eq 0 ] ; then
	/usr/sbin/alternatives --remove print %{_bindir}/lpr.cups || :
fi
%endif

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

%files -f %{name}.lang
%doc README.md CREDITS.md CHANGES.md
%{_bindir}/cupstestppd
%{_bindir}/ppdc
%{_bindir}/ppdhtml
%{_bindir}/ppdi
%{_bindir}/ppdmerge
%{_bindir}/ppdpo
%{_sbindir}/cupsaccept
%{_sbindir}/cupsctl
%{_sbindir}/cupsd
%{_sbindir}/cupsdisable
%{_sbindir}/cupsenable
%{_sbindir}/cupsfilter
%{_sbindir}/cupsreject
%{_sbindir}/lpadmin
%{_sbindir}/lpinfo
%{_sbindir}/lpmove
%dir %{cups_serverbin}/daemon
%{cups_serverbin}/daemon/cups-deviced
%{cups_serverbin}/daemon/cups-driverd
%{cups_serverbin}/daemon/cups-exec
%{cups_serverbin}/backend/dnssd
%{cups_serverbin}/backend/failover
%{cups_serverbin}/backend/http
%{cups_serverbin}/backend/https
%{cups_serverbin}/backend/ipp
%{cups_serverbin}/backend/ipps
%{cups_serverbin}/backend/lpd
%ghost %{cups_serverbin}/backend/smb
%{cups_serverbin}/backend/snmp
%{cups_serverbin}/backend/socket
%{cups_serverbin}/backend/usb
%dir %{cups_serverbin}/cgi-bin
%{cups_serverbin}/cgi-bin/admin.cgi
%{cups_serverbin}/cgi-bin/classes.cgi
%{cups_serverbin}/cgi-bin/help.cgi
%{cups_serverbin}/cgi-bin/jobs.cgi
%{cups_serverbin}/cgi-bin/printers.cgi
%{cups_serverbin}/filter/commandtops
%{cups_serverbin}/filter/gziptoany
%{cups_serverbin}/filter/pstops
%{cups_serverbin}/filter/rastertoepson
%{cups_serverbin}/filter/rastertohp
%{cups_serverbin}/filter/rastertolabel
%{cups_serverbin}/filter/rastertopwg
%dir %{cups_serverbin}/monitor
%{cups_serverbin}/monitor/bcp
%{cups_serverbin}/monitor/tbcp
%dir %{cups_serverbin}/notifier
%{cups_serverbin}/notifier/dbus
%{cups_serverbin}/notifier/mailto
%{cups_serverbin}/notifier/rss
%{_datadir}/cups/drv/sample.drv
%dir %{_datadir}/cups/examples
%{_datadir}/cups/examples/*.drv
%{_datadir}/cups/mime/mime.types
%{_datadir}/cups/mime/mime.convs
%{_datadir}/cups/ppdc/*.defs
%{_datadir}/cups/ppdc/*.h
%dir %{_datadir}/cups/templates
%{_datadir}/cups/templates/*.tmpl
%dir %{_datadir}/cups/templates/da
%{_datadir}/cups/templates/da/*.tmpl
%dir %{_datadir}/cups/templates/de
%{_datadir}/cups/templates/de/*.tmpl
%dir %{_datadir}/cups/templates/es
%{_datadir}/cups/templates/es/*.tmpl
%dir %{_datadir}/cups/templates/fr
%{_datadir}/cups/templates/fr/*.tmpl
%dir %{_datadir}/cups/templates/ja
%{_datadir}/cups/templates/ja/*.tmpl
%dir %{_datadir}/cups/templates/pt_BR
%{_datadir}/cups/templates/pt_BR/*.tmpl
%dir %{_datadir}/cups/templates/ru
%{_datadir}/cups/templates/ru/*.tmpl
%dir %{_datadir}/%{name}/usb
%{_datadir}/%{name}/usb/org.cups.usb-quirks
%dir %{_datadir}/%{name}/www
%{_datadir}/%{name}/www/images
%{_datadir}/%{name}/www/*.css
# 1658673 - html files cannot be docs, because CUPS web ui will not have
# introduction page on Fedora Docker image (because rpms are installed
# without docs there because of space reasons)
%{_datadir}/%{name}/www/index.html
%{_datadir}/%{name}/www/help
%{_datadir}/%{name}/www/robots.txt
%{_datadir}/%{name}/www/da/index.html
%{_datadir}/%{name}/www/de/index.html
%{_datadir}/%{name}/www/es/index.html
%{_datadir}/%{name}/www/fr/index.html
%{_datadir}/%{name}/www/ja/index.html
%{_datadir}/%{name}/www/ru/index.html
%{_datadir}/%{name}/www/pt_BR/index.html
%{_datadir}/%{name}/www/apple-touch-icon.png
%dir %{_datadir}/%{name}/www/da
%dir %{_datadir}/%{name}/www/de
%dir %{_datadir}/%{name}/www/es
%dir %{_datadir}/%{name}/www/fr
%dir %{_datadir}/%{name}/www/ja
%dir %{_datadir}/%{name}/www/pt_BR
%dir %{_datadir}/%{name}/www/ru
%{_datadir}/pixmaps/cupsprinter.png
%ghost %dir %attr(0770,root,lp) %{_localstatedir}/cache/cups
%ghost %dir %attr(0775,root,lp) %{_localstatedir}/cache/cups/rss
%dir %attr(1770,root,lp) %{_localstatedir}/spool/cups/tmp
%dir %attr(0710,root,lp) %{_localstatedir}/spool/cups
%dir %attr(0755,root,lp) %{_localstatedir}/log/cups
%{_mandir}/man1/cups.1.gz
%{_mandir}/man1/cupstestppd.1.gz
%{_mandir}/man1/ppdc.1.gz
%{_mandir}/man1/ppdhtml.1.gz
%{_mandir}/man1/ppdi.1.gz
%{_mandir}/man1/ppdmerge.1.gz
%{_mandir}/man1/ppdpo.1.gz
%{_mandir}/man5/classes.conf.5.gz
%{_mandir}/man5/client.conf.5.gz
%{_mandir}/man5/cups-files.conf.5.gz
%{_mandir}/man5/cups-snmp.conf.5.gz
%{_mandir}/man5/cupsd-logs.5.gz
%{_mandir}/man5/cupsd.conf.5.gz
%{_mandir}/man5/mailto.conf.5.gz
%{_mandir}/man5/mime.convs.5.gz
%{_mandir}/man5/mime.types.5.gz
%{_mandir}/man5/ppdcfile.5.gz
%{_mandir}/man5/printers.conf.5.gz
%{_mandir}/man5/subscriptions.conf.5.gz
%{_mandir}/man7/backend.7.gz
%{_mandir}/man7/filter.7.gz
%{_mandir}/man7/notifier.7.gz
%{_mandir}/man8/cups-deviced.8.gz
%{_mandir}/man8/cups-driverd.8.gz
%{_mandir}/man8/cups-exec.8.gz
%{_mandir}/man8/cups-snmp.8.gz
%{_mandir}/man8/cupsaccept.8.gz
%{_mandir}/man8/cupsctl.8.gz
%{_mandir}/man8/cupsd-helper.8.gz
%{_mandir}/man8/cupsd.8.gz
%{_mandir}/man8/cupsdisable.8.gz
%{_mandir}/man8/cupsenable.8.gz
%{_mandir}/man8/cupsfilter.8.gz
%{_mandir}/man8/cupsreject.8.gz
%{_mandir}/man8/lpadmin.8.gz
%{_mandir}/man8/lpinfo.8.gz
%{_mandir}/man8/lpmove.8.gz
%dir %attr(0755,root,lp) %{_rundir}/cups
%dir %attr(0511,lp,sys) %{_rundir}/cups/certs
%attr(0640,root,lp) %{_sysconfdir}/cups/cupsd.conf.default
%verify(not md5 size mtime) %config(noreplace) %attr(0640,root,lp) %{_sysconfdir}/cups/cupsd.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0640,root,lp) %{_sysconfdir}/cups/cups-files.conf
%attr(0640,root,lp) %{_sysconfdir}/cups/cups-files.conf.default
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/client.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0600,root,lp) %{_sysconfdir}/cups/classes.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0600,root,lp) %{_sysconfdir}/cups/printers.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/snmp.conf
%attr(0640,root,lp) %{_sysconfdir}/cups/snmp.conf.default
%verify(not md5 size mtime) %config(noreplace) %attr(0640,root,lp) %{_sysconfdir}/cups/subscriptions.conf
%verify(not md5 size mtime) %config(noreplace) %attr(0644,root,lp) %{_sysconfdir}/cups/lpoptions
%dir %attr(0755,root,lp) %{_sysconfdir}/cups/ppd
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/cups.conf
%config(noreplace) %{_sysconfdir}/pam.d/cups
%{_tmpfilesdir}/cups.conf
%{_tmpfilesdir}/cups-lp.conf
%attr(0644, root, root)%{_unitdir}/%{name}.service
%attr(0644, root, root)%{_unitdir}/system-%{name}.slice
%attr(0644, root, root)%{_unitdir}/%{name}.socket
%attr(0644, root, root)%{_unitdir}/%{name}.path

%files client
%{_bindir}/cancel.cups
%{_bindir}/lp.cups
%{_bindir}/lpoptions
%{_bindir}/lpq.cups
%{_bindir}/lpr.cups
%{_bindir}/lprm.cups
%{_bindir}/lpstat.cups
%{_sbindir}/lpc.cups
%ghost %{_bindir}/cancel
%ghost %{_bindir}/lp
%ghost %{_bindir}/lpq
%ghost %{_bindir}/lpr
%ghost %{_bindir}/lprm
%ghost %{_bindir}/lpstat
%ghost %{_mandir}/man1/cancel.1.gz
%ghost %{_mandir}/man1/lp.1.gz
%ghost %{_mandir}/man1/lpq.1.gz
%ghost %{_mandir}/man1/lpr.1.gz
%ghost %{_mandir}/man1/lprm.1.gz
%ghost %{_mandir}/man1/lpstat.1.gz
%ghost %{_mandir}/man8/lpc.8.gz
%ghost %{_sbindir}/lpc
%{_mandir}/man1/cancel-cups.1.gz
%{_mandir}/man1/lp-cups.1.gz
%{_mandir}/man1/lpoptions.1.gz
%{_mandir}/man1/lpq-cups.1.gz
%{_mandir}/man1/lpr-cups.1.gz
%{_mandir}/man1/lprm-cups.1.gz
%{_mandir}/man1/lpstat-cups.1.gz
%{_mandir}/man8/lpc-cups.8.gz

%files libs
%{license} LICENSE
%{license} NOTICE
%{_libdir}/libcups.so.2
%{_libdir}/libcupsimage.so.2

%files filesystem
%dir %{cups_serverbin}
%dir %{cups_serverbin}/backend
%dir %{cups_serverbin}/driver
%dir %{cups_serverbin}/filter
%dir %{_datadir}/cups
%dir %{_datadir}/cups/data
%dir %{_datadir}/cups/drv
%dir %{_datadir}/cups/mime
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/ppdc
%dir %{_datadir}/ppd
%dir %attr(0755,root,lp) %{_sysconfdir}/cups
%dir %attr(0700,root,lp) %{_sysconfdir}/cups/ssl

%files devel
%{_bindir}/cups-config
%{_includedir}/cups
%{_libdir}/*.so
%{_libdir}/pkgconfig/cups.pc
%{_mandir}/man1/cups-config.1.gz
%{_rpmconfigdir}/macros.d/macros.cups

%files lpd
%{cups_serverbin}/daemon/cups-lpd
%{_mandir}/man8/cups-lpd.8.gz
%attr(0644, root, root)%{_unitdir}/cups-lpd.socket
%attr(0644, root, root)%{_unitdir}/cups-lpd@.service

%files ipptool
%{_bindir}/ippfind
%{_bindir}/ipptool
%dir %{_datadir}/cups/ipptool
%{_datadir}/cups/ipptool/*
%{_mandir}/man1/ippfind.1.gz
%{_mandir}/man1/ipptool.1.gz
%{_mandir}/man5/ipptoolfile.5.gz

%files printerapp
%{_bindir}/ippeveprinter
%dir %{cups_serverbin}/command
%{cups_serverbin}/command/ippevepcl
%{cups_serverbin}/command/ippeveps
%{_mandir}/man1/ippeveprinter.1.gz
%{_mandir}/man7/ippevepcl.7.gz
%{_mandir}/man7/ippeveps.7.gz

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.16-8
- cups-libs Require avahi-libs (libcups pulls libavahi)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.16-7
- Prepare for Oreon 11 (RP1)
