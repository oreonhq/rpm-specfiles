%global source0_hash 1a085faa8ace52cffde2f5e9bc611bdb5f81481caaabf46f0437b719ca089d2f
%bcond_with db
%if %{with db}
%global db_suffix	db
%else
%global db_suffix	cdb
%endif
%global with_tls	yes
%global with_sasl2	yes
%global with_milter	yes
%global with_ldap	yes
%global with_smtputf8	yes
%global with_nis	no
%global enable_pie	yes
%global sendmailcf %{_datadir}/sendmail-cf
%global stdir %{_localstatedir}/log/mail
%global smshell /sbin/nologin
%global spooldir %{_localstatedir}/spool
%global maildir %{_sysconfdir}/mail
%global sslcert %{_sysconfdir}/pki/tls/certs/sendmail.pem
%global sslkey %{_sysconfdir}/pki/tls/private/sendmail.key
%{!?_hardened_build:%global _hardened_build 1}
%if "%{with_nis}" == "yes"
%global nis_cflags	-DNIS
%global nis_ldadd	-lnsl
%endif
Summary:        A widely used Mail Transport Agent (MTA)
Name: sendmail
Version: 8.18.2
Release:        1%{?dist}
License: sendmail-8.23 AND MIT AND MIT-CMU AND BSD-3-Clause AND CDDL-1.0 AND BSD-4-Clause AND BSD-4-Clause-UC AND PostgreSQL AND ISC AND HPND-sell-variant AND mailprio
URL: http://www.sendmail.org/
Source0:        https://ftp.sendmail.org/sendmail.%{version}.tar.gz
Source1: sendmail.service
Source2: sendmail.nm-dispatcher
Source3: sendmail.etc-mail-make
Source4: sendmail.sysconfig
Source5: sendmail.etc-mail-Makefile
Source6: sendmail-redhat.mc
Source7: sm-client.service
Source8: sendmail.pam
Source11: Sendmail-sasl2.conf
Source12: sendmail-etc-mail-access
Source13: sendmail-etc-mail-domaintable
Source14: sendmail-etc-mail-local-host-names
Source15: sendmail-etc-mail-mailertable
Source16: sendmail-etc-mail-trusted-users
Source17: sendmail-etc-mail-virtusertable
Patch3: sendmail-8.17.2-makemapman.patch
Patch4: sendmail-8.16.1-smrsh_paths.patch
Patch7: sendmail-8.14.9-pid.patch
Patch10: sendmail-8.17.1-manpage.patch
Patch11: sendmail-8.17.1-dynamic.patch
Patch12: sendmail-8.13.0-cyrus.patch
Patch13: sendmail-8.18.2-aliases_dir.patch
Patch14: sendmail-8.14.9-vacation.patch
Patch15: sendmail-8.17.2-noversion.patch
Patch16: sendmail-8.18.2-localdomain.patch
Patch17: sendmail-8.18.1-sharedmilter.patch
Patch18: sendmail-8.17.1-switchfile.patch
Patch23: sendmail-8.18.2-sasl2-in-etc.patch
Patch25: sendmail-8.18.2-qos.patch
Patch26: sendmail-8.17.1-libmilter-socket-activation.patch
%{?with_db:BuildRequires: libdb-devel}
%if "%{with_nis}" == "yes"
%endif
Provides: MTA smtpdaemon server(smtp)
Requires(post): systemd coreutils %{_sbindir}/alternatives %{_bindir}/openssl
Requires(preun): systemd %{_sbindir}/alternatives
Requires(postun): systemd coreutils %{_sbindir}/alternatives
Requires: procmail
Requires: bash >= 2.0
Requires: setup >= 2.5.31-1
%if "%{with_tls}" == "yes"
%endif
%if "%{with_sasl2}" == "yes"
Requires: /usr/sbin/saslauthd
%endif
%if "%{with_ldap}" == "yes"
%endif
%if "%{with_smtputf8}" == "yes"
%endif
Conflicts: NetworkManager < 1.20
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/sendmail
%endif
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  libicu-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  setup
BuildRequires:  systemd
BuildRequires:  tinycdb-devel
# /oreon:deps
%description
The Sendmail program is a very widely used Mail Transport Agent (MTA).
MTAs send mail from one machine to another. Sendmail is not a client
program, which you use to read your email. Sendmail is a
behind-the-scenes program which actually moves your email over
networks or the Internet to where you want it to go.

If you ever need to reconfigure Sendmail, you will also need to have
the sendmail-cf package installed. If you need documentation on
Sendmail, you can install the sendmail-doc package.

%package doc
Summary: Documentation about the Sendmail Mail Transport Agent program
BuildArch: noarch
Requires: sendmail = %{version}-%{release}
%description doc
This package contains the Sendmail Installation and Operation Guide (PDF),
text files containing configuration documentation, plus a number of
contributed scripts and tools for use with Sendmail.

%package milter-devel
Summary: Development files for the sendmail milter library
Requires: sendmail-milter%{?_isa} = %{version}-%{release}
Provides: sendmail-devel%{?_isa} = %{version}-%{release}
Provides: sendmail-devel = %{version}-%{release}
Obsoletes: sendmail-devel < 8.15.2-8
%description milter-devel
Include files and devel libraries for the milter add-ons as part of sendmail.

%package cf
Summary: The files needed to reconfigure Sendmail
Requires: sendmail = %{version}-%{release}
BuildArch: noarch
Requires: m4
%description cf
This package includes the configuration files you need to generate the
sendmail.cf file distributed with the sendmail package. You will need
the sendmail-cf package if you ever need to reconfigure and rebuild
your sendmail.cf file.

%package milter
Summary: The sendmail milter library
%description milter
The sendmail Mail Filter API (Milter) is designed to allow third-party
programs access to mail messages as they are being processed in order to
filter meta-information and content.

This package includes the milter shared library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%patch -P3 -p1 -b .makemapman
%patch -P4 -p1 -b .smrsh_paths
%patch -P7 -p1 -b .pid
%patch -P10 -p1 -b .manpage
%patch -P11 -p1 -b .dynamic
%patch -P12 -p1 -b .cyrus
%patch -P13 -p1 -b .aliases_dir
%patch -P14 -p1 -b .vacation
%patch -P15 -p1 -b .noversion
%patch -P16 -p1 -b .localdomain

cp devtools/M4/UNIX/{,shared}library.m4
%patch -P17 -p1 -b .sharedmilter

%patch -P18 -p1 -b .switchfile
%patch -P23 -p1 -b .sasl2-in-etc
%patch -P25 -p1 -b .qos
%patch -P26 -p1 -b .libmilter-socket-activation

for f in RELEASE_NOTES contrib/etrn.0; do
	iconv -f iso8859-1 -t utf8 -o ${f}{_,} &&
		touch -r ${f}{,_} && mv -f ${f}{_,}
done

sed -i 's|/usr/local/bin/perl|%{_bindir}/perl|' contrib/*.pl

# Create a sysusers.d config file
cat >sendmail.sysusers.conf <<EOF
u mailnull 47 - %{spooldir}/mqueue %{smshell}
u smmsp 51 - %{spooldir}/mqueue %{smshell}
EOF

%build

%set_build_flags
cat > redhat.config.m4 << EOF
define(\`confMAPDEF', \`%{?with_db:-DNEWDB }-DCDB %{?nis_cflags} -DMAP_REGEX -DSOCKETMAP -DNAMED_BIND=1')
define(\`confOPTIMIZE', \`\`\`\`${CFLAGS}'''')
define(\`confENVDEF', \`%{?with_db:-I%{_includedir}/libdb }-I%{_prefix}/kerberos/include -Wall -DXDEBUG=0 -DNETINET6 -DHES_GETMAILHOST -DUSE_VENDOR_CF_PATH=1 -D_FFR_LINUX_MHNL -D_FFR_QOS -D_FILE_OFFSET_BITS=64 -DHAS_GETHOSTBYNAME2 -DHASFLOCK')
define(\`confLIBDIRS', \`-L%{_prefix}/kerberos/%{_lib}')
define(\`confLIBS', \`%{?nis_ldadd} -lcrypt %{?with_db:-ldb }-lcdb -lresolv')
%{?_hardened_build:define(\`confLDOPTS', \`${LDFLAGS}')}
define(\`confMANOWN', \`root')
define(\`confMANGRP', \`root')
define(\`confMANMODE', \`644')
define(\`confMAN1SRC', \`1')
define(\`confMAN5SRC', \`5')
define(\`confMAN8SRC', \`8')
define(\`confSTDIR', \`%{stdir}')
define(\`STATUS_FILE', \`%{stdir}/statistics')
define(\`confLIBSEARCH', \`%{?with_db:db }cdb resolv 44bsd')
define(\`confCC', \`${CC}')
EOF
cat >> redhat.config.m4 << EOF
%ifarch ppc %{power64} s390x
APPENDDEF(\`confOPTIMIZE', \`-DSM_CONF_SHM=0')
%else
APPENDDEF(\`confOPTIMIZE', \`')
%endif
EOF
%if "%{enable_pie}" == "yes"
%ifarch s390 s390x sparc sparcv9 sparc64
%global _fpie -fPIE
%else
%global _fpie -fpie
%endif
cat >> redhat.config.m4 << EOF
APPENDDEF(\`confOPTIMIZE', \`%{_fpie}')
APPENDDEF(\`confLIBS', \`-pie')
EOF
%endif
%if "%{with_tls}" == "yes"
cat >> redhat.config.m4 << EOF
APPENDDEF(\`conf_sendmail_ENVDEF', \`-DSTARTTLS -D_FFR_TLS_1 -DTLS_EC -D_FFR_TLS_USE_CERTIFICATE_CHAIN_FILE -DDANE')dnl
APPENDDEF(\`conf_sendmail_LIBS', \`-lssl -lcrypto')dnl
EOF
%endif
%if "%{with_sasl2}" == "yes"
cat >> redhat.config.m4 << EOF
APPENDDEF(\`confENVDEF', \`-DSASL=2')dnl
APPENDDEF(\`confLIBS', \`-lsasl2 -lcrypto')dnl
EOF
%endif
%if "%{with_milter}" == "yes"
cat >> redhat.config.m4 << EOF
APPENDDEF(\`conf_sendmail_ENVDEF', \`-DMILTER')dnl
APPENDDEF(\`confENVDEF', \`-D_FFR_MILTER_CHECK_REJECTIONS_TOO')dnl
EOF
%endif
%if "%{with_ldap}" == "yes"
cat >> redhat.config.m4 << EOF
APPENDDEF(\`confMAPDEF', \`-DLDAPMAP -DLDAP_DEPRECATED')dnl
APPENDDEF(\`confENVDEF', \`-DSM_CONF_LDAP_MEMFREE=1')dnl
APPENDDEF(\`confLIBS', \`-lldap -llber -lssl -lcrypto')dnl
EOF
%endif
%if "%{with_smtputf8}" == "yes"
cat >> redhat.config.m4 << EOF
APPENDDEF(\`confENVDEF',\`-DUSE_EAI')dnl
APPENDDEF(\`confLIBS', \`-licuuc')dnl
EOF
%endif
DIRS="libsmutil sendmail mailstats rmail praliases smrsh makemap editmap"
%if "%{with_milter}" == "yes"
DIRS="libmilter $DIRS"
%endif
for i in $DIRS; do
	pushd $i
	sh Build -f ../redhat.config.m4
	popd
done
make -C doc/op op.pdf
%install
%if "%{_sbindir}" == "%{_bindir}"
mkdir -p %{buildroot}%{_prefix}/
ln -sf --relative %{buildroot}%{_bindir} %{buildroot}%{_prefix}/sbin
%endif
for d in %{_bindir} %{_sbindir} %{_includedir}/libmilter \
	%{_libdir} %{_mandir}/man{1,5,8} %{maildir} %{stdir} %{spooldir} \
	%{_docdir}/sendmail %{sendmailcf} %{_sysconfdir}/smrsh\
	%{spooldir}/clientmqueue %{_sysconfdir}/sysconfig %{_initrddir} \
	%{_sysconfdir}/pam.d %{_docdir}/sendmail/contrib \
	%{_prefix}/lib/NetworkManager/dispatcher.d
do
	install -m 755 -d %{buildroot}$d
done
install -m 700 -d %{buildroot}%{spooldir}/mqueue
%if "%{_libdir}" != "%{_prefix}/lib"
install -m 755 -d %{buildroot}%{_prefix}/lib
%endif
nameuser=`id -nu`
namegroup=`id -ng`
Make() {
	make $@ \
		DESTDIR=%{buildroot} \
		LIBDIR=%{_libdir} \
		MANROOT=%{_mandir}/man \
		LIBMODE=0755 INCMODE=0644 \
		SBINOWN=${nameuser} SBINGRP=${namegroup} \
		UBINOWN=${nameuser} UBINGRP=${namegroup} \
		MANOWN=${nameuser} MANGRP=${namegroup} \
		INCOWN=${nameuser} INCGRP=${namegroup} \
		LIBOWN=${nameuser} LIBGRP=${namegroup} \
		GBINOWN=${nameuser} GBINGRP=${namegroup} \
		CFOWN=${nameuser} CFGRP=${namegroup} \
		CFMODE=0644 MSPQOWN=${nameuser}
}
OBJDIR=obj.$(uname -s).$(uname -r).$(uname -m)
Make install -C $OBJDIR/libmilter
Make install -C $OBJDIR/sendmail
Make install -C $OBJDIR/mailstats
Make force-install -C $OBJDIR/rmail
Make install -C $OBJDIR/praliases
Make install -C $OBJDIR/smrsh
Make install -C $OBJDIR/makemap
Make install -C $OBJDIR/editmap
%if "%{_sbindir}" != "%{_bindir}"
ln -sf --relative %{buildroot}%{_sbindir}/makemap %{buildroot}%{_bindir}/makemap
%endif
for f in hoststat mailq newaliases purgestat ; do
	ln -sf --relative %{buildroot}%{_sbindir}/sendmail.sendmail %{buildroot}%{_bindir}/${f}
done
ln -sf --relative %{buildroot}%{_sbindir}/sendmail.sendmail %{buildroot}%{_prefix}/lib/sendmail.sendmail
install -p -m 644 FAQ %{buildroot}%{_docdir}/sendmail
install -p -m 644 KNOWNBUGS %{buildroot}%{_docdir}/sendmail
install -p -m 644 LICENSE %{buildroot}%{_docdir}/sendmail
install -p -m 644 README %{buildroot}%{_docdir}/sendmail
install -p -m 644 RELEASE_NOTES %{buildroot}%{_docdir}/sendmail
gzip -9 %{buildroot}%{_docdir}/sendmail/RELEASE_NOTES
install -m 644 doc/op/op.pdf %{buildroot}%{_docdir}/sendmail
install -p -m 644 sendmail/README %{buildroot}%{_docdir}/sendmail/README.sendmail
install -p -m 644 sendmail/SECURITY %{buildroot}%{_docdir}/sendmail
install -p -m 644 smrsh/README %{buildroot}%{_docdir}/sendmail/README.smrsh
install -p -m 644 libmilter/README %{buildroot}%{_docdir}/sendmail/README.libmilter
install -p -m 644 cf/README %{buildroot}%{_docdir}/sendmail/README.cf
install -p -m 644 contrib/* %{buildroot}%{_docdir}/sendmail/contrib
cp -ar cf/* %{buildroot}%{sendmailcf}
rm -rf %{buildroot}%{sendmailcf}/cf/Build.*
rm -rf %{buildroot}%{sendmailcf}/*/*.mc.*
rm -rf %{buildroot}%{sendmailcf}/*/*.m4.*
rm -f %{buildroot}%{sendmailcf}/cf/README
install -m 644 %{SOURCE6} %{buildroot}%{maildir}/sendmail.mc
%if %{without db}
  sed -i 's/\bhash\b/cdb/g;s/\.db\b/.%{db_suffix}/g' %{buildroot}%{maildir}/sendmail.mc
%endif
sed -i -e 's|@@PATH@@|%{sendmailcf}|' %{buildroot}%{maildir}/sendmail.mc
touch -r %{SOURCE6} %{buildroot}%{maildir}/sendmail.mc
cp %{buildroot}%{maildir}/sendmail.mc cf/cf/redhat.mc
sed -i -e 's|%{sendmailcf}|\.\.|' cf/cf/redhat.mc
%if "%{stdir}" != "%{maildir}"
sed -i -e 's:%{maildir}/statistics:%{stdir}/statistics:' cf/cf/redhat.mc
%endif
(cd cf/cf && m4 redhat.mc > redhat.cf)
install -m 644 cf/cf/redhat.cf %{buildroot}%{maildir}/sendmail.cf
install -p -m 644 cf/cf/submit.mc %{buildroot}%{maildir}/submit.mc
sed -i '/##### built by.*on/,+3d' %{buildroot}%{maildir}/{submit,sendmail}.cf \
	%{buildroot}%{sendmailcf}/cf/submit.cf
install -p -m 644 %{SOURCE12} %{buildroot}%{maildir}/access
install -p -m 644 %{SOURCE13} %{buildroot}%{maildir}/domaintable
install -p -m 644 %{SOURCE14} %{buildroot}%{maildir}/local-host-names
install -p -m 644 %{SOURCE15} %{buildroot}%{maildir}/mailertable
install -p -m 644 %{SOURCE16} %{buildroot}%{maildir}/trusted-users
install -p -m 644 %{SOURCE17} %{buildroot}%{maildir}/virtusertable
for map in virtusertable access domaintable mailertable ; do
	touch %{buildroot}%{maildir}/${map}.%{db_suffix}
	chmod 0644 %{buildroot}%{maildir}/${map}.%{db_suffix}
done
touch %{buildroot}%{maildir}/aliasesdb-stamp
touch %{buildroot}%{spooldir}/clientmqueue/sm-client.st
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/sendmail
install -p -m 755 %{SOURCE2} %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/10-sendmail
install -p -m 755 %{SOURCE3} %{buildroot}%{maildir}/make
install -p -m 644 %{SOURCE5} %{buildroot}%{maildir}/Makefile
chmod 644 %{buildroot}%{maildir}/helpfile
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m644 %{SOURCE7} %{buildroot}%{_unitdir}
chmod 755 %{buildroot}%{_sbindir}/{mailstats,makemap,editmap,praliases,sendmail,smrsh}
chmod 755 %{buildroot}%{_bindir}/rmail
%if "%{with_sasl2}" == "yes"
install -m 755 -d %{buildroot}%{_sysconfdir}/sasl2
install -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sasl2/Sendmail.conf
%endif
install -m 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/pam.d/smtp.sendmail
%if "%{stdir}" != "%{maildir}"
sed -i -e 's:%{maildir}/statistics:%{stdir}/statistics:' %{buildroot}%{_mandir}/man*/*
%endif
mv %{buildroot}%{_sbindir}/sendmail %{buildroot}%{_sbindir}/sendmail.sendmail
touch %{buildroot}%{_sbindir}/sendmail
mv %{buildroot}%{_sbindir}/makemap %{buildroot}%{_sbindir}/makemap.sendmail
touch %{buildroot}%{_sbindir}/makemap
mv %{buildroot}%{_sbindir}/editmap %{buildroot}%{_sbindir}/editmap.sendmail
touch %{buildroot}%{_sbindir}/editmap
for i in mailq newaliases rmail; do
	mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i.sendmail
	touch %{buildroot}%{_bindir}/$i
done
mv %{buildroot}%{_mandir}/man1/mailq.1 %{buildroot}%{_mandir}/man1/mailq.sendmail.1
touch %{buildroot}%{_mandir}/man1/mailq.1
mv %{buildroot}%{_mandir}/man1/newaliases.1 %{buildroot}%{_mandir}/man1/newaliases.sendmail.1
touch %{buildroot}%{_mandir}/man1/newaliases.1
mv %{buildroot}%{_mandir}/man5/aliases.5 %{buildroot}%{_mandir}/man5/aliases.sendmail.5
touch %{buildroot}%{_mandir}/man5/aliases.5
mv %{buildroot}%{_mandir}/man8/sendmail.8 %{buildroot}%{_mandir}/man8/sendmail.sendmail.8
touch %{buildroot}%{_mandir}/man8/sendmail.8
mv %{buildroot}%{_mandir}/man8/rmail.8 %{buildroot}%{_mandir}/man8/rmail.sendmail.8
touch %{buildroot}%{_mandir}/man8/rmail.8
mv %{buildroot}%{_mandir}/man8/makemap.8 %{buildroot}%{_mandir}/man8/makemap.sendmail.8
touch %{buildroot}%{_mandir}/man8/makemap.8
mv %{buildroot}%{_mandir}/man8/editmap.8 %{buildroot}%{_mandir}/man8/editmap.sendmail.8
touch %{buildroot}%{_mandir}/man8/editmap.8
touch %{buildroot}%{_prefix}/lib/sendmail
touch %{buildroot}%{_sysconfdir}/pam.d/smtp
for m in man8/hoststat.8 man8/purgestat.8; do
	[ -f %{buildroot}%{_mandir}/$m ] || 
		echo ".so man8/sendmail.8" > %{buildroot}%{_mandir}/$m
done
install -m0644 -D sendmail.sysusers.conf %{buildroot}%{_sysusersdir}/sendmail.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

[ -h /usr/sbin/makemap ] || rm -f /usr/sbin/makemap || :
[ -h %{_mandir}/man8/makemap.8.gz ] || rm -f %{_mandir}/man8/makemap.8.gz || :
exit 0
%postun

%systemd_postun_with_restart sendmail.service sm-client.service
if [ $1 -ge 1 ] ; then
	mta=`readlink %{_sysconfdir}/alternatives/mta`
	if [ "$mta" == "%{_sbindir}/sendmail.sendmail" ] || [ "$mta" == "/usr/sbin/sendmail.sendmail" ]; then
		alternatives --set mta %{_sbindir}/sendmail.sendmail
	fi
fi
exit 0
%post

%systemd_post sendmail.service sm-client.service
alternatives --install \
	    %{_sbindir}/sendmail mta %{_sbindir}/sendmail.sendmail 90 \
	--follower %{_sbindir}/makemap mta-makemap %{_sbindir}/makemap.sendmail \
	--follower %{_sbindir}/editmap mta-editmap %{_sbindir}/editmap.sendmail \
	--follower %{_bindir}/mailq mta-mailq %{_bindir}/mailq.sendmail \
	--follower %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.sendmail \
	--follower %{_bindir}/rmail mta-rmail %{_bindir}/rmail.sendmail \
	--follower %{_prefix}/lib/sendmail mta-sendmail %{_prefix}/lib/sendmail.sendmail \
	--follower %{_sysconfdir}/pam.d/smtp mta-pam %{_sysconfdir}/pam.d/smtp.sendmail \
	--follower %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man8/sendmail.sendmail.8.gz \
	--follower %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.sendmail.1.gz \
	--follower %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man1/newaliases.sendmail.1.gz \
	--follower %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.sendmail.5.gz \
	--follower %{_mandir}/man8/rmail.8.gz mta-rmailman %{_mandir}/man8/rmail.sendmail.8.gz \
	--follower %{_mandir}/man8/makemap.8.gz mta-makemapman %{_mandir}/man8/makemap.sendmail.8.gz \
	--follower %{_mandir}/man8/editmap.8.gz mta-editmapman %{_mandir}/man8/editmap.sendmail.8.gz \
	--initscript sendmail > /dev/null 2>&1
test -h /usr/sbin || ln -s ../bin/sendmail /usr/sbin/sendmail 2>/dev/null || :
test -h /usr/sbin || ln -s ../bin/makemap /usr/sbin/makemap 2>/dev/null || :
test -h /usr/sbin || ln -s ../bin/editmap /usr/sbin/editmap 2>/dev/null || :
{
	chown root %{_sysconfdir}/aliases.%{db_suffix} %{maildir}/access.%{db_suffix} \
		%{maildir}/mailertable.%{db_suffix} %{maildir}/domaintable.%{db_suffix} \
		%{maildir}/virtusertable.%{db_suffix}
	SM_FORCE_DBREBUILD=1 %{maildir}/make
	SM_FORCE_DBREBUILD=1 %{maildir}/make aliases
} >/dev/null 2>&1
%if "%{with_sasl2}" == "yes"
[ -f %{_libdir}/sasl2/Sendmail.conf ] && touch -r %{_sysconfdir}/sasl2/Sendmail.conf \
  %{_libdir}/sasl2/Sendmail.conf ] && mv -f %{_libdir}/sasl2/Sendmail.conf \
  %{_sysconfdir}/sasl2 2>/dev/null || :
%endif
if [ ! -f %{spooldir}/clientmqueue/sm-client.st ]; then
	touch %{spooldir}/clientmqueue/sm-client.st
	chown smmsp:smmsp %{spooldir}/clientmqueue/sm-client.st
	chmod 0660 %{spooldir}/clientmqueue/sm-client.st
fi
if [ ! -f %{sslkey} ]; then
  umask 077
  openssl genrsa 4096 >%{sslkey} 2>/dev/null
fi
if [ ! -f %{sslcert} ]; then
  FQDN=`hostname`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi
  openssl req -new -key %{sslkey} -x509 -sha256 -days 365 -set_serial $RANDOM -out %{sslcert} \
    -subj "/C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=${FQDN}/emailAddress=root@${FQDN}"
  chmod 600 %{sslcert}
fi
exit 0
%preun

%systemd_preun sendmail.service sm-client.service
if [ $1 = 0 ]; then
	alternatives --remove mta %{_sbindir}/sendmail.sendmail
fi
exit 0
%ldconfig_scriptlets milter
%files -f %{oreon_filedir}/main.list
%files -n sendmail-doc -f %{oreon_filedir}/sendmail-doc.list
%files -n sendmail-milter-devel -f %{oreon_filedir}/sendmail-milter-devel.list
%files -n sendmail-cf -f %{oreon_filedir}/sendmail-cf.list
%files -n sendmail-milter -f %{oreon_filedir}/sendmail-milter.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.18.2-3
- Prepare for Oreon 11 (RP1)
