%global source0_hash 934757e178e771686b33d4ec030a55845ec9be2867887d8d2282bdb94b50daaa

%define _hardened_build 1
%define _default_patch_fuzz 2
# $Id: squidGuard.spec,v 1.22 2009/10/26 13:30:17 limb Exp $

# GCC 10 uses -fno-common by default, turn it off for now
%define _legacy_common_support 1

%define			_dbtopdir		%{_var}/%{name}
%define			_dbhomedir		%{_var}/%{name}/blacklists
%define			_cgibin			/var/www/cgi-bin

Name:			squidGuard
Version:		1.4
Release:		52%{?dist}
Summary:		Filter, redirector and access controller plugin for squid

License:		GPL-2.0-only

Source0:		http://www.squidguard.org/Downloads/squidGuard-%{version}.tar.gz
Source1:		squidGuard.logrotate
Source2:		http://squidguard.mesd.k12.or.us/blacklists.tgz
Source3:		http://cuda.port-aransas.k12.tx.us/squid-getlist.html
Source4:		squidGuard-1.4-patch-20150201.tar.gz

# K12LTSP stuff
Source100:		squidGuard.conf
Source101:		update_squidguard_blacklists
#Source102:		squidguard
#Source103:		transparent-proxying
Source104:		squidGuard.service
Source105:		transparent-proxying.service
Source106:		squidGuard-helper
Source107:		transparent-proxying-helper

# SELinux (taken from K12LTSP package)
#Source200:		squidGuard.te
#Source201:		squidGuard.fc

#Patch0:			squidGuard-upstream.patch
#Patch1:			squidGuard-paths.patch
Patch2:			squid-getlist.html.patch
Patch3:			squidGuard-perlwarning.patch
#Patch4:			squidGuard-sed.patch
Patch5:			squidGuard-makeinstall.patch
#Patch6:			squidGuard-1.3-SG-2008-06-13.patch
Patch7:			squidGuard-1.4-20091015.patch
Patch8:			squidGuard-1.4-20091019.patch
Patch9:			squidGuard-1.4-db5.patch
Patch10:		squidGuard-1.4-helper-protocol.patch
Patch11:                squidGuard-1.4-setuserinfo.patch
Patch12:                squidGuard-configure-c99.patch
Patch13:                squidGuard-htunescape-c99.patch
Patch14:                squidGuard-1.4-declarations.patch

URL:			http://www.squidguard.org/

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	bison, byacc, openldap-devel, flex, libdb-devel
BuildRequires:	perl-generators
BuildRequires:	systemd

Requires:		squid
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
squidGuard can be used to 
- limit the web access for some users to a list of accepted/well known
  web servers and/or URLs only.
- block access to some listed or blacklisted web servers and/or URLs
  for some users.
- block access to URLs matching a list of regular expressions or words
  for some users.
- enforce the use of domainnames/prohibit the use of IP address in
  URLs.
- redirect blocked URLs to an "intelligent" CGI based info page.
- redirect unregistered user to a registration form.
- redirect popular downloads like Netscape, MSIE etc. to local copies.
- redirect banners to an empty GIF.
- have different access rules based on time of day, day of the week,
  date etc.
- have different rules for different user groups.
- and much more.. 

Neither squidGuard nor Squid can be used to
- filter/censor/edit text inside documents 
- filter/censor/edit embeded scripting languages like JavaScript or
  VBscript inside HTML

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{__cp} %{SOURCE3} .
#%patch0 -p1
#%patch1 -p1 -b .paths
%patch -P2 -p0
%patch -P3 -p2
#%patch4 -p1
%patch -P5	-p1
#%patch6 -p0
%patch -P7 -p0
%patch -P8 -p0
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1

%{__cp} %{SOURCE100} ./squidGuard.conf.k12ltsp.template
%{__cp} %{SOURCE101} ./update_squidguard_blacklists.k12ltsp.sh

%build
# LDAP_DEPRECATED ensures that ldap_init is declared in <ldap.h>.
%set_build_flags
CFLAGS="$CFLAGS -DLDAP_DEPRECATED"

%configure \
	--with-sg-config=%{_sysconfdir}/squid/squidGuard.conf \
	--with-sg-logdir=%{_var}/log/squidGuard \
	--with-sg-dbhome=%{_dbhomedir} \
	--with-ldap=yes
	
#%{__make} %{?_smp_mflags}
%{__make}

pushd contrib
%{__make} %{?_smp_mflags}
popd

#Apply squidGuard-1.4-patch-20150201.tar.gz
tar -xzf %{SOURCE4} --overwrite -C samples/ --strip-components=1

%install
%{__rm} -rf $RPM_BUILD_ROOT

#%{__make} DESTDIR=$RPM_BUILD_ROOT install
# This broke as of 1.2.1.
%{__install} -p -D -m 0755 src/squidGuard $RPM_BUILD_ROOT%{_bindir}/squidGuard

%{__install} -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/squidGuard
%{__install} -p -D -m 0644 samples/sample.conf $RPM_BUILD_ROOT%{_sysconfdir}/squid/squidGuard.conf
%{__install} -p -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_dbtopdir}/blacklists.tar.gz

# Don't use SOURCE3, but use the allready patched one #165689
%{__install} -p -D -m 0755 squid-getlist.html $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/squidGuard

#%{__install} -p -D %{SOURCE200} $RPM_BUILD_ROOT%{_sysconfdir}/selinux/targeted/src/policy/domains/program/squidGuard.te
#%{__install} -p -D %{SOURCE201} $RPM_BUILD_ROOT%{_sysconfdir}/selinux/targeted/src/policy/file_contexts/program/squidGuard.fc

%{__install} -p -d $RPM_BUILD_ROOT%{_cgibin}
%{__install} samples/squid*cgi $RPM_BUILD_ROOT%{_cgibin}

%{__install} contrib/hostbyname/hostbyname $RPM_BUILD_ROOT%{_bindir}
%{__install} contrib/sgclean/sgclean $RPM_BUILD_ROOT%{_bindir}

#%{__install} -p -D -m 0755 %{SOURCE102} $RPM_BUILD_ROOT%{_initrddir}/squidGuard
#%{__install} -p -D -m 0755 %{SOURCE103} $RPM_BUILD_ROOT%{_initrddir}/transparent-proxying

%{__install} -p -D -m 0644 %{SOURCE104} $RPM_BUILD_ROOT%{_unitdir}/squidGuard.service
%{__install} -p -D -m 0644 %{SOURCE105} $RPM_BUILD_ROOT%{_unitdir}/transparent-proxying.service

%{__install} -p -D -m 0744 %{SOURCE106} $RPM_BUILD_ROOT%{_bindir}/squidGuard-helper
%{__install} -p -D -m 0744 %{SOURCE107} $RPM_BUILD_ROOT%{_bindir}/transparent-proxying-helper

#pushd $RPM_BUILD_ROOT%{_dbhomedir}
tar xfz $RPM_BUILD_ROOT%{_dbtopdir}/blacklists.tar.gz
#popd

sed -i "s,dest/adult/,blacklists/porn/,g" $RPM_BUILD_ROOT%{_sysconfdir}/squid/squidGuard.conf

%{__install} -p -D -m 0644 samples/babel.* $RPM_BUILD_ROOT%{_cgibin}

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/squidGuard
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/squid
ln -s ../squidGuard/squidGuard.log  $RPM_BUILD_ROOT%{_localstatedir}/log/squid/squidGuard.log

%post
# fix SELinux bits
#%{_bindir}/chcon -R system_u:object_r:squid_cache_t /var/squidGuard >/dev/null 2>&1
#%{_bindir}/chcon -R system_u:object_r:squid_log_t /var/log/squidGuard >/dev/null 2>&1

## do we need a new config file?
#if [ -s %{_sysconfdir}/squid/squidGuard.conf ]; then
#	CONFFILE="%{_sysconfdir}/squid/squidGuard.conf.rpmnew"
#    echo "/etc/squid/squidGuard.conf created as /etc/squid/squidGuard.conf.rpmnew"
#else
#	CONFFILE="/etc/squid/squidGuard.conf"
#fi
#cat %{_docdir}/%{name}-%{version}/squidGuard.conf.k12ltsp.template | \
#	sed s/SERVERNAME/$HOSTNAME/g > $CONFFILE

#/sbin/chkconfig --add squidGuard
#/sbin/chkconfig --add transparent-proxying
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

# reload SELinux policies
#echo "Loading new SELinux policy"
#pushd %{_sysconfdir}/selinux/targeted/src/policy/
#%{__make} load &> /dev/null
#popd

#### End of %post

%preun
#if [ $1 = 0 ] ; then
#    service squidGuard stop >/dev/null 2>&1
#    /sbin/chkconfig --del squidGuard
#	/sbin/chkconfig --del transparent-proxying
#fi
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable squidGuard.service > /dev/null 2>&1 || :
    /bin/systemctl stop squidGuard.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable transparent-proxying.service > /dev/null 2>&1 || :
    /bin/systemctl stop transparent-proxying.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart squidGuard.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart transparent-proxying.service >/dev/null 2>&1 || :
fi

%triggerun -- squidGuard < 1.4-13
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply squidGuard
# and systemd-sysv-convert --apply transparent-proxying
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save squidGuard >/dev/null 2>&1 ||:
/usr/bin/systemd-sysv-convert --save transparent-proxying >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del squidGuard >/dev/null 2>&1 || :
/sbin/chkconfig --del transparent-proxying >/dev/null 2>&1 || :
/bin/systemctl try-restart squidGuard.service >/dev/null 2>&1 || :
/bin/systemctl try-restart transparent-proxying.service >/dev/null 2>&1 || :

%files
%doc samples/*.conf
%doc samples/*.cgi
%doc samples/dest/blacklists.tar.gz
%doc COPYING GPL 
%doc doc/*.txt doc/*.html doc/*.gif
%doc squidGuard.conf.k12ltsp.template
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/squid/squidGuard.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/squidGuard
%config(noreplace) %{_sysconfdir}/cron.daily/squidGuard
%{_dbtopdir}/
%attr(0755,root,root) %{_cgibin}/*.cgi
%config(noreplace) %{_cgibin}/squidGuard.cgi
%{_cgibin}/babel.*
%{_unitdir}/squidGuard.service
%{_unitdir}/transparent-proxying.service
%attr(0755,squid,squid) %{_localstatedir}/log/squidGuard
%attr(0755,squid,squid) %{_localstatedir}/log/squid/squidGuard.log

%changelog
%autochangelog
