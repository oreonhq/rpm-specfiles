%global source0_hash eae967bd49a5f879933b8c6ec88c30475a1c6646232135f37f05b55dbc4e3447

# By default build clamav subpackage on Fedora,
# do not build on RHEL
%if 0%{?rhel}
%bcond_with clamav
%else
%bcond_without clamav
%endif

# hardened build if not overridden
%{!?_hardened_build:%global _hardened_build 1}

Summary: The exim mail transfer agent
Name: exim
Version: 4.99.1
Release: 3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: https://www.exim.org/

Provides: MTA smtpd smtpdaemon server(smtp)
Requires(post): %{_sbindir}/restorecon %{_sbindir}/alternatives systemd
Requires(preun): %{_sbindir}/alternatives systemd
Requires(postun): %{_sbindir}/alternatives systemd
%if %{with clamav}
BuildRequires: clamd
%endif
Source: https://ftp.exim.org/pub/exim/exim4/exim-%{version}.tar.xz
Source1: https://ftp.exim.org/pub/exim/exim4/%{name}-%{version}.tar.xz.asc
Source2: https://downloads.exim.org/Exim-Maintainers-Keyring.asc

Source3: exim.sysconfig
Source4: exim.logrotate
Source5: exim-tidydb.sh
Source11: exim.pam
Source12: exim-clamav-tmpfiles.conf

Source20: exim-greylist.conf.inc
Source21: mk-greylist-db.sql
Source22: greylist-tidy.sh
Source23: trusted-configs
Source24: exim.service
Source25: exim-gen-cert
Source26: clamd.exim.service

Patch: exim-4.99-config.patch
Patch: exim-4.94-libdir.patch
Patch: exim-4.97-dlopen-localscan.patch
Patch: exim-4.99-pic.patch

Requires: /etc/pki/tls/certs /etc/pki/tls/private
Requires: /etc/aliases
Recommends: publicsuffix-list

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/sendmail
%endif

BuildRequires: gcc
BuildRequires: libdb-devel
BuildRequires: openssl-devel
BuildRequires: openldap-devel
BuildRequires: pam-devel
BuildRequires: pcre2-devel
BuildRequires: sqlite-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libspf2-devel
BuildRequires: libopendmarc-devel
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: mariadb-connector-c-devel
BuildRequires: libpq-devel
BuildRequires: libxcrypt-devel
BuildRequires: libXaw-devel
BuildRequires: libXmu-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXpm-devel
BuildRequires: libXt-devel
BuildRequires: systemd-units
BuildRequires: libgsasl-devel
# Workaround for NIS removal from glibc, bug 1534920
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel
BuildRequires: gnupg2
BuildRequires: grep
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-ExtUtils-Embed
BuildRequires: perl-experimental
BuildRequires: perl-File-FcntlLock
%if 0%{?rhel} == 8
BuildRequires:  epel-rpm-macros >= 8-5
%endif
BuildRequires: make

# i686 repo is broken, stop building it
ExcludeArch: %{ix86}

%description
Exim is a message transfer agent (MTA) developed at the University of
Cambridge for use on Unix systems connected to the Internet. It is
freely available under the terms of the GNU General Public Licence. In
style it is similar to Smail 3, but its facilities are more
general. There is a great deal of flexibility in the way mail can be
routed, and there are extensive facilities for checking incoming
mail. Exim can be installed in place of sendmail, although the
configuration of exim is quite different to that of sendmail.

%package mysql
Summary: MySQL lookup support for Exim
Requires: exim = %{version}-%{release}

%description mysql
This package contains the MySQL lookup module for Exim

%package pgsql
Summary: PostgreSQL lookup support for Exim
Requires: exim = %{version}-%{release}

%description pgsql
This package contains the PostgreSQL lookup module for Exim

%package mon
Summary: X11 monitor application for Exim

%description mon
The Exim Monitor is an optional supplement to the Exim package. It
displays information about Exim's processing in an X window, and an
administrator can perform a number of control actions from the window
interface.

%if %{with clamav}
%package clamav
Summary: Clam Antivirus scanner dæmon configuration for use with Exim
Requires: clamd exim
Obsoletes: clamav-exim <= 0.86.2

%description clamav
This package contains configuration files which invoke a copy of the
clamav dæmon for use with Exim. It can be activated by adding (or
uncommenting)

   av_scanner = clamd:%{_var}/run/clamd.exim/clamd.sock

in your exim.conf, and using the 'malware' condition in the DATA ACL,
as follows:

   deny message = This message contains malware ($malware_name)
      malware = *

For further details of Exim content scanning, see chapter 41 of the Exim
specification:
http://www.exim.org/exim-html-%{version}/doc/html/spec_html/ch41.html

%endif

%package greylist
Summary: Example configuration for greylisting using Exim
Requires: sqlite exim
Requires: crontabs

%description greylist
This package contains a simple example of how to do greylisting in Exim's
ACL configuration. It contains a cron job to remove old entries from the
greylisting database, and an ACL subroutine which needs to be included
from the main exim.conf file.

To enable greylisting, install this package and then uncomment the lines
in Exim's configuration /etc/exim.conf which enable it. You need to
uncomment at least two lines -- the '.include' directive which includes
the new ACL subroutine, and the line which invokes the new subroutine.

By default, this implementation only greylists mails which appears
'suspicious' in some way. During normal processing of the ACLs we collect
a list of 'offended' which it's committed, which may include having
SpamAssassin points, lacking a Message-ID: header, coming from a blacklisted
host, etc. There are examples of these in the default configuration file,
mostly commented out. These should be sufficient for you to you trigger
greylisting for whatever 'offences' you can dream of, or even to make
greylisting unconditional.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

cp src/EDITME Local/Makefile
sed -i 's@^# LOOKUP_MODULE_DIR=.*@LOOKUP_MODULE_DIR=%{_libdir}/exim/%{version}-%{release}/lookups@' Local/Makefile
sed -i 's@^# AUTH_LIBS=-lsasl2@AUTH_LIBS=-lsasl2@' Local/Makefile
sed -i 's@^# SUPPORT_SRS=yes@SUPPORT_SRS=yes@' Local/Makefile
cp exim_monitor/EDITME Local/eximon.conf

# Workaround for rhbz#1791878
pushd doc
for f in $(ls -dp cve-* | grep -v '/\|\(\.txt\)$'); do
  mv "$f" "$f.txt"
done
popd

# Create a sysusers.d config file
cat >exim.sysusers.conf <<EOF
u exim 93 - %{_var}/spool/exim -
m exim mail
EOF

%build
# https://bugs.exim.org/show_bug.cgi?id=3135
export CFLAGS="%{build_cflags} -std=gnu17"
%ifnarch s390 s390x sparc sparcv9 sparcv9v sparc64 sparc64v
	export PIE=-fpie
	export PIC=-fpic
%else
	export PIE=-fPIE
	export PIC=-fPIC
%endif

export LDFLAGS="%{?__global_ldflags} %{?_hardened_build:-pie -Wl,-z,relro,-z,now}"
make _lib=%{_lib} FULLECHO=

%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/exim

cd build-`scripts/os-type`-`scripts/arch-type`
install -m 4775 exim $RPM_BUILD_ROOT%{_sbindir}

for i in eximon eximon.bin exim_dumpdb exim_fixdb exim_tidydb \
	exinext exiwhat exim_dbmbuild exicyclog exim_lock \
	exigrep eximstats exipick exiqgrep exiqsumm \
	exim_checkaccess
do
	install -m 0755 $i $RPM_BUILD_ROOT%{_sbindir}
done

mkdir -p $RPM_BUILD_ROOT%{_libdir}/exim/%{version}-%{release}/lookups
for i in mysql pgsql
do 
	install -m755 lookups/${i}.so \
	 $RPM_BUILD_ROOT%{_libdir}/exim/%{version}-%{release}/lookups/${i}_lookup.so
done

cd ..

install -m 0644 src/configure.default $RPM_BUILD_ROOT%{_sysconfdir}/exim/exim.conf
install -m 0644 %SOURCE11 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/exim

mkdir -p $RPM_BUILD_ROOT/usr/lib
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/exim $RPM_BUILD_ROOT/usr/lib/sendmail.exim

ln -sf exim $RPM_BUILD_ROOT%{_sbindir}/sendmail.exim

ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/exim $RPM_BUILD_ROOT%{_bindir}/mailq.exim
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/exim $RPM_BUILD_ROOT%{_bindir}/runq.exim
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/exim $RPM_BUILD_ROOT%{_bindir}/rsmtp.exim
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/exim $RPM_BUILD_ROOT%{_bindir}/rmail.exim
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/exim $RPM_BUILD_ROOT%{_bindir}/newaliases.exim

install -d -m 0750 $RPM_BUILD_ROOT%{_var}/spool/exim
install -d -m 0750 $RPM_BUILD_ROOT%{_var}/spool/exim/db
install -d -m 0750 $RPM_BUILD_ROOT%{_var}/spool/exim/input
install -d -m 0750 $RPM_BUILD_ROOT%{_var}/spool/exim/msglog
install -d -m 0750 $RPM_BUILD_ROOT%{_var}/log/exim

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m644 doc/exim.8 $RPM_BUILD_ROOT%{_mandir}/man8/exim.8
pod2man --center=EXIM --section=8 \
	$RPM_BUILD_ROOT%{_sbindir}/eximstats \
	$RPM_BUILD_ROOT%{_mandir}/man8/eximstats.8

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 %SOURCE3 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/exim

# Systemd
mkdir -p %{buildroot}%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
install -m644 %{SOURCE24} %{buildroot}%{_unitdir}
install -m755 %{SOURCE25} %{buildroot}%{_libexecdir}

%if %{with clamav}
install -m644 %{SOURCE26} %{buildroot}%{_unitdir}
%endif

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 %SOURCE4 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/exim

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -m 0755 %SOURCE5 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/exim-tidydb

# generate ghost .pem file
mkdir -p $RPM_BUILD_ROOT/etc/pki/tls/{certs,private}
touch $RPM_BUILD_ROOT/etc/pki/tls/{certs,private}/exim.pem
chmod 600 $RPM_BUILD_ROOT/etc/pki/tls/{certs,private}/exim.pem

# generate alternatives ghosts
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
for i in %{_sbindir}/sendmail %{_bindir}/{mailq,runq,rsmtp,rmail,newaliases} \
	/usr/lib/sendmail %{_sysconfdir}/pam.d/smtp
do
	touch $RPM_BUILD_ROOT$i
done
gzip < /dev/null > $RPM_BUILD_ROOT%{_mandir}/man1/mailq.1.gz

%if %{with clamav}
# Munge the clamav init and config files from clamav-devel. This really ought
# to be a subpackage of clamav, but this hack will have to do for now.
function clamsubst() {
	 sed -e "s!<SERVICE>!$3!g;s!<USER>!$4!g;""$5" %{_docdir}/clamd/"$1" >"$RPM_BUILD_ROOT$2"
}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/clamd.d
clamsubst clamd.conf %{_sysconfdir}/clamd.d/exim.conf exim exim \
       's!^##*\(\(LogFile\|LocalSocket\|PidFile\|User\)\s\|\(StreamSaveToDisk\|ScanMail\|LogTime\|ScanArchive\)$\)!\1!;s!^Example!#Example!;'

clamsubst clamd.logrotate %{_sysconfdir}/logrotate.d/clamd.exim exim exim ''
cat <<EOF > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/clamd.exim
CLAMD_CONFIG='%_sysconfdir/clamd.d/exim.conf'
CLAMD_SOCKET=%{_var}/run/clamd.exim/clamd.sock
EOF
ln -sf clamd $RPM_BUILD_ROOT%{_sbindir}/clamd.exim

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE12} %{buildroot}%{_tmpfilesdir}/exim-clamav.conf
mkdir -p $RPM_BUILD_ROOT%{_var}/run/clamd.exim
mkdir -p $RPM_BUILD_ROOT%{_var}/log
touch $RPM_BUILD_ROOT%{_var}/log/clamd.exim

%endif

# Set up the greylist subpackage
install -m644 %{SOURCE20} $RPM_BUILD_ROOT/%_sysconfdir/exim/exim-greylist.conf.inc
install -m644 %{SOURCE21} $RPM_BUILD_ROOT/%_sysconfdir/exim/mk-greylist-db.sql
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/cron.daily
install -m755 %{SOURCE22} $RPM_BUILD_ROOT/%_sysconfdir/cron.daily/greylist-tidy.sh
install -m644 %{SOURCE23} $RPM_BUILD_ROOT/%_sysconfdir/exim/trusted-configs
touch $RPM_BUILD_ROOT/%_var/spool/exim/db/greylist.db

install -m0644 -D exim.sysusers.conf %{buildroot}%{_sysusersdir}/exim.conf

%check
build-`scripts/os-type`-`scripts/arch-type`/exim -C src/configure.default -bV

%pre
# Copy TLS certs from old location to new -- don't move them, because the
# config file may be modified and may be pointing to the old location.
if [ ! -f /etc/pki/tls/certs/exim.pem -a -f %{_datadir}/ssl/certs/exim.pem ] ; then
   cp %{_datadir}/ssl/certs/exim.pem /etc/pki/tls/certs/exim.pem
   cp %{_datadir}/ssl/private/exim.pem /etc/pki/tls/private/exim.pem
fi

exit 0

%post
%systemd_post %{name}.service

alternatives --install %{_sbindir}/sendmail mta %{_sbindir}/sendmail.exim 10 \
	--follower %{_bindir}/mailq mta-mailq %{_bindir}/mailq.exim \
	--follower %{_bindir}/runq mta-runq %{_bindir}/runq.exim \
	--follower %{_bindir}/rsmtp mta-rsmtp %{_bindir}/rsmtp.exim \
	--follower %{_bindir}/rmail mta-rmail %{_bindir}/rmail.exim \
	--follower /etc/pam.d/smtp mta-pam /etc/pam.d/exim \
	--follower %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.exim \
	--follower /usr/lib/sendmail mta-sendmail /usr/lib/sendmail.exim \
	--follower %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man8/exim.8.gz \
	--initscript exim

# Make sure that /usr/sbin/sendmail is not missing, if /usr/sbin is a
# directory. The symlink will only be created if there is no symlink
# or file already.
test -h /usr/sbin || ln -s ../bin/sendmail /usr/sbin/sendmail 2>/dev/null || :

%preun
%systemd_preun %{name}.service
if [ $1 = 0 ]; then
	alternatives --remove mta %{_sbindir}/sendmail.exim
fi

%postun
%systemd_postun_with_restart %{name}.service
if [ $1 -ge 1 ]; then
	mta=`readlink /etc/alternatives/mta`
	if [ "$mta" == "%{_sbindir}/sendmail.exim" ]; then
		alternatives --set mta %{_sbindir}/sendmail.exim
	fi
fi

%post greylist
if [ ! -r %{_var}/spool/exim/db/greylist.db ]; then
   sqlite3 %{_var}/spool/exim/db/greylist.db < %{_sysconfdir}/exim/mk-greylist-db.sql
   chown exim:exim %{_var}/spool/exim/db/greylist.db
   chmod 0660 %{_var}/spool/exim/db/greylist.db
fi

%files
%attr(4755,root,root) %{_sbindir}/exim
%{_sbindir}/exim_dumpdb
%{_sbindir}/exim_fixdb
%{_sbindir}/exim_tidydb
%{_sbindir}/exinext
%{_sbindir}/exiwhat
%{_sbindir}/exim_dbmbuild
%{_sbindir}/exicyclog
%{_sbindir}/exigrep
%{_sbindir}/eximstats
%{_sbindir}/exipick
%{_sbindir}/exiqgrep
%{_sbindir}/exiqsumm
%{_sbindir}/exim_lock
%{_sbindir}/exim_checkaccess
%{_sbindir}/sendmail.exim
%{_bindir}/mailq.exim
%{_bindir}/runq.exim
%{_bindir}/rsmtp.exim
%{_bindir}/rmail.exim
%{_bindir}/newaliases.exim
/usr/lib/sendmail.exim
%{_mandir}/man8/*
%dir %{_libdir}/exim
%dir %{_libdir}/exim/%{version}-%{release}
%dir %{_libdir}/exim/%{version}-%{release}/lookups

%defattr(-,exim,exim)
%dir %{_var}/spool/exim
%dir %{_var}/spool/exim/db
%dir %{_var}/spool/exim/input
%dir %{_var}/spool/exim/msglog
%dir %{_var}/log/exim

%defattr(-,root,root)
%dir %{_sysconfdir}/exim
%config(noreplace) %{_sysconfdir}/exim/exim.conf
%config(noreplace) %{_sysconfdir}/exim/trusted-configs
%config(noreplace) %{_sysconfdir}/sysconfig/exim
%{_unitdir}/exim.service
%{_libexecdir}/exim-gen-cert
%config(noreplace) %{_sysconfdir}/logrotate.d/exim
%config(noreplace) %{_sysconfdir}/pam.d/exim
%{_sysconfdir}/cron.daily/exim-tidydb

%license LICENCE NOTICE
%doc ACKNOWLEDGMENTS README.UPDATING README
%doc doc util/unknownuser.sh

%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) /etc/pki/tls/certs/exim.pem
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) /etc/pki/tls/private/exim.pem

%attr(0755,root,root) %ghost %{_sbindir}/sendmail
%attr(0755,root,root) %ghost %{_bindir}/mailq
%attr(0755,root,root) %ghost %{_bindir}/runq
%attr(0755,root,root) %ghost %{_bindir}/rsmtp
%attr(0755,root,root) %ghost %{_bindir}/rmail
%attr(0755,root,root) %ghost %{_bindir}/newaliases
%attr(0755,root,root) %ghost /usr/lib/sendmail
%ghost %{_sysconfdir}/pam.d/smtp
%ghost %{_mandir}/man1/mailq.1.gz
%{_sysusersdir}/exim.conf

%files mysql
%{_libdir}/exim/%{version}-%{release}/lookups/mysql_lookup.so

%files pgsql
%{_libdir}/exim/%{version}-%{release}/lookups/pgsql_lookup.so

%files mon
%{_sbindir}/eximon
%{_sbindir}/eximon.bin

%if %{with clamav}
%post clamav
mkdir -pm 0750 %{_var}/run/clamd.exim
chown exim:exim %{_var}/run/clamd.exim
touch %{_var}/log/clamd.exim
chown exim:exim %{_var}/log/clamd.exim
restorecon %{_var}/log/clamd.exim
if [ $1 -eq 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun clamav
if [ $1 = 0 ]; then
  systemctl --no-reload clamd.exim.service > /dev/null 2>&1 || :
  systemctl stop clamd.exim.service > /dev/null 2>&1 || :
fi

%postun clamav
systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    systemctl try-restart clamd.exim.service >/dev/null 2>&1 || :
fi

%files clamav
%{_sbindir}/clamd.exim
%{_unitdir}/clamd.exim.service
%config(noreplace) %verify(not mtime) %{_sysconfdir}/clamd.d/exim.conf
%config(noreplace) %verify(not mtime) %{_sysconfdir}/sysconfig/clamd.exim
%config(noreplace) %verify(not mtime) %{_sysconfdir}/logrotate.d/clamd.exim
%{_tmpfilesdir}/exim-clamav.conf
%ghost %attr(0750,exim,exim) %dir %{_var}/run/clamd.exim
%ghost %attr(0644,exim,exim) %{_var}/log/clamd.exim
%endif

%files greylist
%config %{_sysconfdir}/exim/exim-greylist.conf.inc
%ghost %{_var}/spool/exim/db/greylist.db
%{_sysconfdir}/exim/mk-greylist-db.sql
%{_sysconfdir}/cron.daily/greylist-tidy.sh

%changelog
%autochangelog
