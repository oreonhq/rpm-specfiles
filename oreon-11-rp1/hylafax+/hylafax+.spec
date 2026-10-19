%global source0_hash d696df653b1c59664fddd2c703edc77ed42766a16b2ce19c958933d76fd62287
%global faxspool    /var/spool/hylafax
%global _hardened_build 1
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%global lockdir    /var/lock/lockdev
%else
%global lockdir    /var/lock
%endif
Summary:        An enterprise-strength fax server
Name:      hylafax+
Version:   7.0.11
Release:        1%{?dist}
License:   libtiff AND LicenseRef-Callaway-BSD-with-advertising
URL:       http://hylafax.sourceforge.net
Source0:        http://downloads.sourceforge.net/hylafax/hylafax-%{version}.tar.gz
Source1:   hylafax+_rh.init
Source2:   hylafax+_daily.cron
Source3:   hylafax+_hourly.cron
Source4:   hylafax+_hfaxd_systemd.service
Source5:   hylafax+_faxq_systemd.service
Source6:   hylafax+_faxgetty_systemd.service
Source7:   hylafax+_sysconfig
Provides:    hylafax = %{version}-%{release}
Requires:    %{name}-client%{?_isa} = %{version}-%{release}
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%endif
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%endif
%if 0%{?fedora} >= 27 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
Requires: urw-base35-fonts
%else
Requires: ghostscript-fonts
%endif
Requires:    ghostscript, gawk, sharutils, mailx, crontabs, %{_bindir}/tiffcp
Requires:    openssl
Conflicts:   mgetty-sendfax
Obsoletes:   hylafax < 5.5.2-1
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
%endif
# oreon:deps
BuildRequires:  //bin/sendmail
BuildRequires:  //bin/tiffcp
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  jbigkit-devel
BuildRequires:  lcms-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  systemd-units
BuildRequires:  urw-base35-fonts
BuildRequires:  zlib-devel
# /oreon:deps
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
%global oreon_srcdir hylafax-%{version}
%oreon_prep
%build

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
make OPTIMIZER="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,cron.hourly} 
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{hylafax,sysconfig}
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
mkdir -p -m 755 $RPM_BUILD_ROOT%{_unitdir}
%else
mkdir -p -m 755 $RPM_BUILD_ROOT%{_initrddir}
%endif
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_libdir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_mandir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{faxspool}/config
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
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/hylafax-hfaxd.service
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/hylafax-faxq.service
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/hylafax-faxgetty@.service
%else
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/hylafax+
%endif
install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/hylafax+
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/hylafax+
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/hylafax+
rm -f $RPM_BUILD_ROOT%{_sbindir}/{faxsetup.irix,faxsetup.bsdi}
rm -f $RPM_BUILD_ROOT%{faxspool}/bin/{ps2fax.imp,ps2fax.dps}
rm -f $RPM_BUILD_ROOT%{faxspool}/etc/dpsprinter.ps
rm -f $RPM_BUILD_ROOT%{faxspool}/COPYRIGHT
%oreon_autofiles main
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%post

if [ -e %{faxspool}/etc/setup.cache ] && [ ! -e %{_sysconfdir}/hylafax/setup.cache ]; then
    ln %{faxspool}/etc/setup.cache %{_sysconfdir}/hylafax/setup.cache
fi
if [ -e %{faxspool}/etc/setup.modem ] && [ ! -e %{_sysconfdir}/hylafax/setup.modem ]; then
    ln %{faxspool}/etc/setup.modem %{_sysconfdir}/hylafax/setup.modem
fi
/sbin/ldconfig
if [ 0$1 -eq 1 ]; then
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
