%global source0_hash d696df653b1c59664fddd2c703edc77ed42766a16b2ce19c958933d76fd62287

%global faxspool    /var/spool/hylafax
%global _hardened_build 1
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%global lockdir    /var/lock/lockdev
%else
%global lockdir    /var/lock
%endif

Summary:   An enterprise-strength fax server
Name:      hylafax+
Version:   7.0.11
Release:   5%{?dist}
# Automatically converted from old format: libtiff and BSD with advertising - review is highly recommended.
License:   libtiff AND LicenseRef-Callaway-BSD-with-advertising
URL:       http://hylafax.sourceforge.net

Source0:   http://downloads.sourceforge.net/hylafax/hylafax-%{version}.tar.gz
Source1:   hylafax+_rh.init
Source2:   hylafax+_daily.cron
Source3:   hylafax+_hourly.cron
Source4:   hylafax+_hfaxd_systemd.service
Source5:   hylafax+_faxq_systemd.service
Source6:   hylafax+_faxgetty_systemd.service
Source7:   hylafax+_sysconfig

Provides:    hylafax = %{version}-%{release}
Requires:    %{name}-client%{?_isa} = %{version}-%{release}

BuildRequires: libjpeg-devel, libtiff-devel, zlib-devel, pam-devel, openldap-devel, %{_bindir}/tiffcp
BuildRequires: openssl-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires: %{_sbindir}/sendmail, ghostscript
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
BuildRequires: jbigkit-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: lcms2-devel
%else
BuildRequires: lcms-devel
%endif
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
BuildRequires: systemd-units
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires: systemd
%endif
%if 0%{?fedora} >= 27 || 0%{?rhel} > 7
BuildRequires: urw-base35-fonts
Requires: urw-base35-fonts
%else
BuildRequires: ghostscript-fonts
Requires: ghostscript-fonts
%endif
Requires:    ghostscript, gawk, sharutils, mailx, crontabs, %{_bindir}/tiffcp
Requires:    openssl
Conflicts:   mgetty-sendfax
Obsoletes:   hylafax < 5.5.2-1

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
%endif

%description
HylaFAX(tm) is a enterprise-strength fax server supporting
Class 1 and 2 fax modems on UNIX systems. It provides spooling
services and numerous supporting fax management tools. 
The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms including 
windows.

%package client
Summary:     Client programs for HylaFAX fax servers
Provides:    hylafax-client = %{version}-%{release}
Obsoletes:   hylafax-client < 5.5.2-1
Requires:    %{_sbindir}/sendmail

%description client
HylaFAX(tm) is a enterprise-strength fax server supporting
Class 1 and 2 fax modems on UNIX systems. This package provides
fax clients which may reside on machines different from the server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hylafax-%{version}

%build
# - Can't use the configure macro because HylaFAX configure script does
#   not understand the config options used by that macro
STRIP=':' \
./configure \
        --with-FAXUID=daemon \
        --with-FAXGID=daemon \
        --with-DIR_BIN=%{_bindir} \
        --with-DIR_SBIN=%{_sbindir} \
        --with-DIR_LIB=%{_libdir} \
        --with-DIR_LIBEXEC=%{_sbindir} \
        --with-DIR_LIBDATA=%{_sysconfdir}/hylafax \
        --with-DIR_LOCKS=%{lockdir} \
        --with-LIBDIR=%{_libdir} \
        --with-TIFFBIN=%{_bindir} \
        --with-DIR_MAN=%{_mandir} \
        --with-PATH_GSRIP=%{_bindir}/gs \
        --with-TIFFINC=-L%{_includedir} \
        --with-LIBTIFF="-ltiff" \
        --with-DIR_SPOOL=%{faxspool} \
        --with-AFM=no \
        --with-AWK=%{_bindir}/gawk \
        --with-PATH_VGETTY=/sbin/vgetty \
        --with-PATH_GETTY=/sbin/mgetty \
        --with-PAGESIZE=A4 \
        --with-PATH_DPSRIP=%{faxspool}/bin/ps2fax \
        --with-PATH_IMPRIP="" \
        --with-SYSVINIT=%{_initrddir}/hylafax+ \
        --with-INTERACTIVE=no

# can't use %{?_smp_mflags} because it breaks libfaxutil dso building
make OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

# install: make some dirs...
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,cron.hourly} 
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{hylafax,sysconfig}
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
mkdir -p -m 755 $RPM_BUILD_ROOT%{_unitdir}
%else
mkdir -p -m 755 $RPM_BUILD_ROOT%{_initrddir}
%endif
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_libdir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_mandir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{faxspool}/config

# install: binaries and man pages 
# FAXUSER, FAXGROUP, SYSUSER and SYSGROUP are set to the current user to
# avoid warnings about chown/chgrp if the user building the SRPM is not root; 
# they are set to the correct values with the RPM attr macro
make install -e \
        FAXUSER=`id -u` \
        FAXGROUP=`id -g` \
        SYSUSER=`id -u` \
        SYSGROUP=`id -g` \
        BIN=$RPM_BUILD_ROOT%{_bindir} \
        SBIN=$RPM_BUILD_ROOT%{_sbindir} \
        LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
        LIBDATA=$RPM_BUILD_ROOT%{_sysconfdir}/hylafax \
        LIBEXEC=$RPM_BUILD_ROOT%{_sbindir} \
        SPOOL=$RPM_BUILD_ROOT%{faxspool} \
        MAN=$RPM_BUILD_ROOT%{_mandir} \
        INSTALL_ROOT=$RPM_BUILD_ROOT

# install: remaining files
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/hylafax-hfaxd.service
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/hylafax-faxq.service
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/hylafax-faxgetty@.service
%else
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/hylafax+
%endif
install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/hylafax+
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/hylafax+
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/hylafax+

# Prepare docdir by removing non-doc files
# Remove files that are not needed on Linux
rm -f $RPM_BUILD_ROOT%{_sbindir}/{faxsetup.irix,faxsetup.bsdi}
rm -f $RPM_BUILD_ROOT%{faxspool}/bin/{ps2fax.imp,ps2fax.dps}
rm -f $RPM_BUILD_ROOT%{faxspool}/etc/dpsprinter.ps

rm -f $RPM_BUILD_ROOT%{faxspool}/COPYRIGHT

%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%post
if [ -e %{faxspool}/etc/setup.cache ] && [ ! -e %{_sysconfdir}/hylafax/setup.cache ]; then
    ln %{faxspool}/etc/setup.cache %{_sysconfdir}/hylafax/setup.cache
fi
if [ -e %{faxspool}/etc/setup.modem ] && [ ! -e %{_sysconfdir}/hylafax/setup.modem ]; then
    ln %{faxspool}/etc/setup.modem %{_sysconfdir}/hylafax/setup.modem
fi
/sbin/ldconfig
if [ 0$1 -eq 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post client -p /sbin/ldconfig

%preun
if [ 0$1 -eq 0 ]; then
    /bin/systemctl --no-reload disable hylafax-hfaxd.service > /dev/null 2>&1 || :
    /bin/systemctl stop hylafax-hfaxd.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable hylafax-faxq.service > /dev/null 2>&1 || :
    /bin/systemctl stop hylafax-faxq.service > /dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ 0$1 -ge 1 ]; then
    /bin/systemctl try-restart hylafax-hfaxd.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart hylafax-faxq.service >/dev/null 2>&1 || :
fi

%postun client -p /sbin/ldconfig

%else
%post
if [ -e %{faxspool}/etc/setup.cache ] && [ ! -e %{_sysconfdir}/hylafax/setup.cache ]; then
    ln %{faxspool}/etc/setup.cache %{_sysconfdir}/hylafax/setup.cache
fi
if [ -e %{faxspool}/etc/setup.modem ] && [ ! -e %{_sysconfdir}/hylafax/setup.modem ]; then
    ln %{faxspool}/etc/setup.modem %{_sysconfdir}/hylafax/setup.modem
fi
/sbin/ldconfig
if [ 0$1 -eq 1 ]; then
    /sbin/chkconfig --add hylafax+
fi

%post client -p /sbin/ldconfig

%preun
if [ 0$1 -eq 0 ]; then
    /sbin/chkconfig --del hylafax+
    /sbin/service hylafax+ stop >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ 0$1 -ge 1 ]; then
    /sbin/service hylafax+ condrestart >/dev/null 2>&1 || :
fi

%postun client -p /sbin/ldconfig
%endif

%files
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%{_unitdir}/hylafax-faxgetty@.service
%{_unitdir}/hylafax-hfaxd.service
%{_unitdir}/hylafax-faxq.service
%else
%{_initrddir}/hylafax+
%endif
%doc CHANGES CONTRIBUTORS COPYRIGHT README TODO VERSION
%{_libdir}/libfaxserver*
%{_mandir}/man5/doneq.5f.gz
%{_mandir}/man5/hosts.hfaxd.5f.gz
%{_mandir}/man5/hylafax-config.5f.gz
%{_mandir}/man5/hylafax-info.5f.gz
%{_mandir}/man5/hylafax-log.5f.gz
%{_mandir}/man5/hylafax-server.5f.gz
%{_mandir}/man5/hylafax-shutdown.5f.gz
%{_mandir}/man5/pagermap.5f.gz
%{_mandir}/man5/recvq.5f.gz
%{_mandir}/man5/sendq.5f.gz
%{_mandir}/man5/status.5f.gz
%{_mandir}/man5/tsi.5f.gz
%{_mandir}/man5/xferfaxlog.5f.gz
%{_mandir}/man8/choptest.8c.gz
%{_mandir}/man8/cqtest.8c.gz
%{_mandir}/man8/faxabort.8c.gz
%{_mandir}/man8/faxaddmodem.8c.gz
%{_mandir}/man8/faxadduser.8c.gz
%{_mandir}/man8/faxanswer.8c.gz
%{_mandir}/man8/faxconfig.8c.gz
%{_mandir}/man8/faxcron.8c.gz
%{_mandir}/man8/faxdeluser.8c.gz
%{_mandir}/man8/faxgetty.8c.gz
%{_mandir}/man8/faxlock.8c.gz
%{_mandir}/man8/faxmodem.8c.gz
%{_mandir}/man8/faxq.8c.gz
%{_mandir}/man8/faxqclean.8c.gz
%{_mandir}/man8/faxquit.8c.gz
%{_mandir}/man8/faxrcvd.8c.gz
%{_mandir}/man8/faxsend.8c.gz
%{_mandir}/man8/faxstate.8c.gz
%{_mandir}/man8/hfaxd.8c.gz
%{_mandir}/man8/jobcontrol.8c.gz
%{_mandir}/man8/mkcover.8c.gz
%{_mandir}/man8/notify.8c.gz
%{_mandir}/man8/pagesend.8c.gz
%{_mandir}/man8/pollrcvd.8c.gz
%{_mandir}/man8/ps2fax.8c.gz
%{_mandir}/man8/recvstats.8c.gz
%{_mandir}/man8/tagtest.8c.gz
%{_mandir}/man8/tsitest.8c.gz
%{_mandir}/man8/wedged.8c.gz
%{_mandir}/man8/xferfaxstats.8c.gz
%{_mandir}/man8/faxmsg.8c.gz
%{_mandir}/man8/hylafax.8c.gz
%{_mandir}/man8/lockname.8c.gz
%{_mandir}/man8/ondelay.8c.gz
%{_mandir}/man8/probemodem.8c.gz
%dir %{_sysconfdir}/hylafax
%config(noreplace) %{_sysconfdir}/hylafax/hfaxd.conf
%dir %{faxspool}/config
%dir %{faxspool}/dev
%{faxspool}/config/*
%{faxspool}/bin/dict/*
%{faxspool}/bin/auto-rotate.ps
%{faxspool}/etc/cover.templ
%{faxspool}/etc/lutRS18.pcf
%{faxspool}/etc/LiberationSans-25.pcf
%config(noreplace) %{_sysconfdir}/sysconfig/hylafax+
%defattr(755,root,root,-)
%{_sysconfdir}/cron.daily/hylafax+
%{_sysconfdir}/cron.hourly/hylafax+
%{_sbindir}/choptest
%{_sbindir}/cqtest
%{_sbindir}/faxabort
%{_sbindir}/faxaddmodem
%{_sbindir}/faxadduser
%{_sbindir}/faxanswer
%{_sbindir}/faxconfig
%{_sbindir}/faxcron
%{_sbindir}/faxdeluser
%{_sbindir}/faxgetty
%{_sbindir}/faxlock
%{_sbindir}/faxmodem
%{_sbindir}/faxmsg
%{_sbindir}/faxq
%{_sbindir}/faxqclean
%{_sbindir}/faxquit
%{_sbindir}/faxsend
%{_sbindir}/faxstate
%{_sbindir}/hfaxd
%{_sbindir}/hylafax
%{_sbindir}/lockname
%{_sbindir}/ondelay
%{_sbindir}/pagesend
%{_sbindir}/probemodem
%{_sbindir}/recvstats
%{_sbindir}/tagtest
%{_sbindir}/tsitest
%{_sbindir}/xferfaxstats
%{faxspool}/bin/archive
%{faxspool}/bin/dictionary
%{faxspool}/bin/faxrcvd
%{faxspool}/bin/mkcover
%{faxspool}/bin/notify
%{faxspool}/bin/pollrcvd
%{faxspool}/bin/qp-encode.awk
%{faxspool}/bin/rfc2047-encode.awk
%{faxspool}/bin/wedged
%defattr(-,daemon,daemon,-)
%dir %{faxspool}
%dir %{faxspool}/client
%dir %{faxspool}/etc
%dir %{faxspool}/info
%dir %{faxspool}/log
%dir %{faxspool}/recvq
%dir %{faxspool}/status
%config(noreplace) %{faxspool}/etc/xferfaxlog
%attr(700,daemon,daemon) %dir %{faxspool}/docq
%attr(700,daemon,daemon) %dir %{faxspool}/doneq
%attr(700,daemon,daemon) %dir %{faxspool}/archive
%attr(700,daemon,daemon) %dir %{faxspool}/sendq
%attr(700,daemon,daemon) %dir %{faxspool}/tmp
%attr(700,daemon,daemon) %dir %{faxspool}/pollq
%defattr(600,daemon,daemon,-)
%config(noreplace) %{faxspool}/etc/hosts.hfaxd

%files client
%doc CHANGES CONTRIBUTORS COPYRIGHT README TODO VERSION
%{_libdir}/libfaxutil*
%{_mandir}/man1/*
%{_mandir}/man5/dialrules.5f.gz
%{_mandir}/man5/pagesizes.5f.gz
%{_mandir}/man5/typerules.5f.gz
%{_mandir}/man8/dialtest.8c.gz
%{_mandir}/man8/faxinfo.8c.gz
%{_mandir}/man8/faxwatch.8c.gz
%{_mandir}/man8/faxsetup.8c.gz
%{_mandir}/man8/pdf2fax.8c.gz
%{_mandir}/man8/tiff2fax.8c.gz
%{_mandir}/man8/tiffcheck.8c.gz
%{_mandir}/man8/faxfetch.8c.gz
%{_mandir}/man8/faxsetup.linux.8c.gz
%{_mandir}/man8/typetest.8c.gz
%dir %{_sysconfdir}/hylafax
%dir %{_sysconfdir}/hylafax/faxmail
%dir %{_sysconfdir}/hylafax/faxmail/application
%dir %{_sysconfdir}/hylafax/faxmail/image
%config(noreplace) %{_sysconfdir}/hylafax/faxcover.ps
%config(noreplace) %{_sysconfdir}/hylafax/faxmail.ps
%config(noreplace) %{_sysconfdir}/hylafax/pagesizes
%config(noreplace) %{_sysconfdir}/hylafax/typerules
%{faxspool}/bin/genfontmap.ps
%config(noreplace) %{faxspool}/etc/dialrules*
%defattr(755,root,root,-)
%{_bindir}/*
%{_sbindir}/dialtest
%{_sbindir}/edit-faxcover
%{_sbindir}/faxfetch
%{_sbindir}/faxinfo
%{_sbindir}/faxsetup
%{_sbindir}/faxsetup.linux
%{_sbindir}/faxwatch
%{_sbindir}/textfmt
%{_sbindir}/tiffcheck
%{_sbindir}/typetest
%{faxspool}/bin/common-functions
%{faxspool}/bin/pcl2fax
%{faxspool}/bin/pdf2fax.gs
%{faxspool}/bin/ps2fax.gs
%{faxspool}/bin/tiff2fax
%{faxspool}/bin/tiff2pdf
%{_sysconfdir}/hylafax/faxmail/application/binary
%{_sysconfdir}/hylafax/faxmail/application/pdf
%{_sysconfdir}/hylafax/faxmail/application/octet-stream
%{_sysconfdir}/hylafax/faxmail/image/tiff
%defattr(-,daemon,daemon,-)
%dir %{faxspool}
%dir %{faxspool}/etc

%changelog
%autochangelog
