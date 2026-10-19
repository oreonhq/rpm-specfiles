%global source0_hash a2f3242345753448072177fae83c322a403c9263696996406201145dab8e8625
%global source53_hash 5ccba9ec765720c79b9d8ae0f02e4c39f042d54e742a238ebb20b51a61915167
%undefine _strict_symbol_defs_build
%bcond_with db
%bcond_without mysql
%bcond_without pgsql
%bcond_without sqlite
%bcond_without cdb
%bcond_without ldap
%bcond_without lmdb
%bcond_without pcre
%bcond_without sasl
%bcond_without tls
%bcond_without ipv6
%bcond_without pflogsumm
%if %{without db} && %{with lmdb}
%global defmap_lmdb 1
%else
%global defmap_lmdb 0
%endif
%global sysv2systemdnvr 2.8.12-2
%{!?_hardened_build:%global _hardened_build 1}
%define postfix_user	postfix
%define maildrop_group	postdrop
%define postfix_config_dir	%{_sysconfdir}/postfix
%define postfix_daemon_dir	%{_libexecdir}/postfix
%define postfix_shlib_dir	%{_libdir}/postfix
%define postfix_command_dir	%{_sbindir}
%define postfix_queue_dir	%{_var}/spool/postfix
%define postfix_data_dir	%{_var}/lib/postfix
%define postfix_doc_dir		%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%define postfix_sample_dir	%{postfix_doc_dir}/samples
%define postfix_readme_dir	%{postfix_doc_dir}/README_FILES
%global sslcert %{_sysconfdir}/pki/tls/certs/postfix.pem
%global sslkey  %{_sysconfdir}/pki/tls/private/postfix.key
%global _privatelibs libpostfix-.+\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
Name: postfix
Summary:        Postfix Mail Transport Agent
Version: 3.11.7
Release:        1%{?dist}
Epoch: 2
URL: http://www.postfix.org
License: (IPL-1.0 OR EPL-2.0) AND GPL-2.0-or-later AND BSD-4-Clause-UC
Requires(post): systemd systemd-sysv hostname
Requires(post): %{_sbindir}/alternatives
Requires(post): %{_bindir}/openssl
Requires(preun): %{_sbindir}/alternatives
Requires(preun): systemd
Requires(postun): systemd
Requires: diffutils
Requires: findutils
Requires: policycoreutils
Provides: MTA smtpd smtpdaemon server(smtp)
Source0:        http://ftp.porcupine.org/mirrors/postfix-release/official/%{name}-%{version}.tar.gz
Source1: postfix-etc-init.d-postfix
Source2: postfix.service
Source3: README-Postfix-SASL-RedHat.txt
Source4: postfix.aliasesdb
Source5: postfix-chroot-update
Source6: postfix.sysusers
%define pflogsumm_ver 1.1.6
Source53:        http://jimsun.linxnet.com/downloads/pflogsumm-1.1.6.tar.gz
Source100: postfix-sasl.conf
Source101: postfix-pam.conf
Patch1: postfix-3.11.0-config.patch
Patch2: postfix-3.11.0-files.patch
Patch3: postfix-3.9.0-alternatives.patch
Patch4: postfix-3.8.0-large-fs.patch
Patch9: pflogsumm-1.1.6-syslog-name-underscore-fix.patch
Patch11: postfix-3.4.4-chroot-example-fix.patch
%{?with_db:BuildRequires: libdb-devel}
%{?with_ldap:BuildRequires: openldap-devel}
%{?with_lmdb:BuildRequires: lmdb-devel}
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
%{?with_pcre:BuildRequires: pcre2-devel}
%{?with_mysql:BuildRequires: mariadb-connector-c-devel}
%{?with_pgsql:BuildRequires: libpq-devel}
%{?with_sqlite:BuildRequires: sqlite-devel}
%{?with_cdb:BuildRequires: tinycdb-devel}
%{?with_tls:BuildRequires: openssl-devel}
%if 0%{?defmap_lmdb}
Requires: %{name}-lmdb%{?_isa} = %{epoch}:%{version}-%{release}
%endif
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/sendmail
Provides: /usr/sbin/smtp-sink
%endif
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libicu-devel
BuildRequires:  libpq-devel
BuildRequires:  lmdb-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-units
BuildRequires:  tinycdb-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Postfix is a Mail Transport Agent (MTA).

%if 0%{?fedora} < 23 && 0%{?rhel} < 9 && 0%{?oreon} < 11
%package sysvinit
Summary: SysV initscript for postfix
BuildArch: noarch
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): chkconfig
Requires(post): chkconfig
%description sysvinit
This package contains the SysV initscript.
%endif

%package perl-scripts
Summary: Postfix utilities written in perl
Requires: %{name} = %{epoch}:%{version}-%{release}
Obsoletes: postfix < 2:2.5.5-2
%if %{with pflogsumm}
Provides: postfix-pflogsumm = %{epoch}:%{version}-%{release}
Obsoletes: postfix-pflogsumm < 2:2.5.5-2
%endif
%description perl-scripts
This package contains perl scripts pflogsumm and qshape.

Pflogsumm is a log analyzer/summarizer for the Postfix MTA. It is
designed to provide an over-view of Postfix activity. Pflogsumm
generates summaries and, in some cases, detailed reports of mail
server traffic volumes, rejected and bounced email, and server
warnings, errors and panics.

qshape prints Postfix queue domain and age distribution.

%if %{with mysql}
%package mysql
Summary: Postfix MySQL map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description mysql
This provides support for MySQL maps in Postfix. If you plan to use MySQL
maps with Postfix, you need this.
%endif

%if %{with pgsql}
%package pgsql
Summary: Postfix PostgreSQL map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description pgsql
This provides support for PostgreSQL  maps in Postfix. If you plan to use
PostgreSQL maps with Postfix, you need this.
%endif

%if %{with sqlite}
%package sqlite
Summary: Postfix SQLite map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description sqlite
This provides support for SQLite maps in Postfix. If you plan to use SQLite
maps with Postfix, you need this.
%endif

%if %{with cdb}
%package cdb
Summary: Postfix CDB map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description cdb
This provides support for CDB maps in Postfix. If you plan to use CDB
maps with Postfix, you need this.
%endif

%if %{with ldap}
%package ldap
Summary: Postfix LDAP map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description ldap
This provides support for LDAP maps in Postfix. If you plan to use LDAP
maps with Postfix, you need this.
%endif

%if %{with lmdb}
%package lmdb
Summary: Postfix LDMB map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description lmdb
This provides support for LMDB maps in Postfix. If you plan to use LMDB
maps with Postfix, you need this.
%endif

%if %{with pcre}
%package pcre
Summary: Postfix PCRE map support
Requires: %{name} = %{epoch}:%{version}-%{release}
%description pcre
This provides support for PCRE maps in Postfix. If you plan to use PCRE
maps with Postfix, you need this.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source53_hash}" = "none" || { f="%{SOURCE53}"; test -f "$f" || { echo "oreon: missing Source53 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source53_hash}" || { echo "oreon: Source53 hash mismatch" >&2; exit 1; }; }
%setup -q
# Apply obligatory patches
%patch -P1 -p1 -b .config
%patch -P2 -p1 -b .files
%patch -P3 -p1 -b .alternatives
%patch -P4 -p1 -b .large-fs

# Change DEF_SHLIB_DIR according to build host
sed -i \
's|^\(\s*#define\s\+DEF_SHLIB_DIR\s\+\)"/usr/lib/postfix"|\1"%{_libdir}/postfix"|' \
src/global/mail_params.h

%if %{with pflogsumm}
gzip -dc %{SOURCE53} | tar xf -
pushd pflogsumm-%{pflogsumm_ver}
%patch -P9 -p1 -b .pflogsumm-1.1.6-syslog-name-underscore-fix
popd
%endif
%patch -P11 -p1 -b .chroot-example-fix

# Backport 3.8-20221006 fix for uname -r detection
sed -i makedefs -e '\@Linux\.@s|345|3456|'
sed -i src/util/sys_defs.h -e 's@defined(LINUX5)@defined(LINUX5) || defined(LINUX6)@'

for f in README_FILES/TLS_{LEGACY_,}README TLS_ACKNOWLEDGEMENTS; do
	iconv -f iso8859-1 -t utf8 -o ${f}{_,} &&
		touch -r ${f}{,_} && mv -f ${f}{_,}
done

# fix default maps
%if 0%{?defmap_lmdb}
  sed -i '/^\s*alias_maps\s*=\s*hash:\/etc\/aliases/ s|hash:|lmdb:|g' conf/main.cf
  sed -i '/^\s*alias_database\s*=\s*hash:\/etc\/aliases/ s|hash:|lmdb:|g' conf/main.cf
  echo >> conf/main.cf
  echo "default_database_type = lmdb" >> conf/main.cf
%endif

%build

%set_build_flags
unset AUXLIBS AUXLIBS_LDAP AUXLIBS_LMDB AUXLIBS_PCRE AUXLIBS_MYSQL AUXLIBS_PGSQL AUXLIBS_SQLITE AUXLIBS_CDB
CCARGS="-fPIC -fcommon -std=gnu17"
AUXLIBS="-lnsl"
%if %{without db}
  CCARGS="${CCARGS} -DNO_DB"
%endif
%ifarch s390 s390x ppc
CCARGS="${CCARGS} -fsigned-char"
%endif
%if %{with ldap}
  CCARGS="${CCARGS} -DHAS_LDAP -DLDAP_DEPRECATED=1 %{?with_sasl:-DUSE_LDAP_SASL}"
  AUXLIBS_LDAP="-lldap -llber"
%endif
%if %{with lmdb}
  CCARGS="${CCARGS} -DHAS_LMDB"
  AUXLIBS_LMDB="-llmdb"
%endif
%if %{with pcre}
  CCARGS="${CCARGS} -DHAS_PCRE=2 `pcre2-config --cflags`"
  AUXLIBS_PCRE=`pcre2-config --libs8`
%endif
%if %{with mysql}
  CCARGS="${CCARGS} -DHAS_MYSQL -I%{_includedir}/mysql"
  AUXLIBS_MYSQL="-L%{_libdir}/mariadb -lmysqlclient -lm"
%endif
%if %{with pgsql}
  CCARGS="${CCARGS} -DHAS_PGSQL -I%{_includedir}/pgsql"
  AUXLIBS_PGSQL="-lpq"
%endif
%if %{with sqlite}
  CCARGS="${CCARGS} -DHAS_SQLITE `pkg-config --cflags sqlite3`"
  AUXLIBS_SQLITE="`pkg-config --libs sqlite3`"
%endif
%if %{with cdb}
  CCARGS="${CCARGS} -DHAS_CDB `pkg-config --cflags libcdb`"
  AUXLIBS_CDB="`pkg-config --libs libcdb`"
%endif
%if %{with sasl}
  CCARGS="${CCARGS} -DUSE_SASL_AUTH -DUSE_CYRUS_SASL -I%{_includedir}/sasl"
  AUXLIBS="${AUXLIBS} -L%{_libdir}/sasl2 -lsasl2"
  %global sasl_config_dir %{_sysconfdir}/sasl2
%endif
%if %{with tls}
  if pkg-config openssl ; then
    CCARGS="${CCARGS} -DUSE_TLS `pkg-config --cflags openssl`"
    AUXLIBS="${AUXLIBS} `pkg-config --libs openssl`"
  else
    CCARGS="${CCARGS} -DUSE_TLS -I%{_includedir}/openssl"
    AUXLIBS="${AUXLIBS} -lssl -lcrypto"
  fi
%endif
%if ! %{with ipv6}
  CCARGS="${CCARGS} -DNO_IPV6"
%endif
CCARGS="${CCARGS} -DDEF_CONFIG_DIR=\\\"%{postfix_config_dir}\\\""
CCARGS="${CCARGS} $(getconf LFS_CFLAGS)"
LDFLAGS="$LDFLAGS %{?_hardened_build:-Wl,-z,relro,-z,now}"
make -f Makefile.init makefiles shared=yes dynamicmaps=yes \
  %{?_hardened_build:pie=yes} CCARGS="${CCARGS}" AUXLIBS="${AUXLIBS}" \
  AUXLIBS_LDAP="${AUXLIBS_LDAP}" AUXLIBS_LMDB="${AUXLIBS_LMDB}" \
  AUXLIBS_PCRE="${AUXLIBS_PCRE}" AUXLIBS_MYSQL="${AUXLIBS_MYSQL}" \
  AUXLIBS_PGSQL="${AUXLIBS_PGSQL}" AUXLIBS_SQLITE="${AUXLIBS_SQLITE}" \
  AUXLIBS_CDB="${AUXLIBS_CDB}" \
  DEBUG="" SHLIB_RPATH="-Wl,-rpath,%{postfix_shlib_dir} $LDFLAGS" \
  OPT="$CFLAGS -fno-strict-aliasing -Wno-comment" \
  POSTFIX_INSTALL_OPTS=-keep-build-mtime
%make_build
%install
for i in man1/mailq.1 man1/newaliases.1 man1/sendmail.1 man5/aliases.5 man8/smtp{,d}.8; do
  dest=$(echo $i | sed 's|\.[1-9]$|.postfix\0|')
  mv man/$i man/$dest
  sed -i "s|^\.so $i|\.so $dest|" man/man?/*.[1-9]
done
make non-interactive-package \
       install_root=$RPM_BUILD_ROOT \
       config_directory=%{postfix_config_dir} \
       meta_directory=%{postfix_config_dir} \
       shlib_directory=%{postfix_shlib_dir} \
       daemon_directory=%{postfix_daemon_dir} \
       command_directory=%{postfix_command_dir} \
       queue_directory=%{postfix_queue_dir} \
       data_directory=%{postfix_data_dir} \
       sendmail_path=%{postfix_command_dir}/sendmail.postfix \
       newaliases_path=%{_bindir}/newaliases.postfix \
       mailq_path=%{_bindir}/mailq.postfix \
       mail_owner=%{postfix_user} \
       setgid_group=%{maildrop_group} \
       manpage_directory=%{_mandir} \
       sample_directory=%{postfix_sample_dir} \
       readme_directory=%{postfix_readme_dir} || exit 1
%if 0%{?fedora} < 23 && 0%{?rhel} < 9 && 0%{?oreon} < 11
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
install -c %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/postfix
%endif
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
install -m 755 %{SOURCE4} %{buildroot}%{postfix_daemon_dir}/aliasesdb
install -m 755 %{SOURCE5} %{buildroot}%{postfix_daemon_dir}/chroot-update
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/postfix.conf
install -c auxiliary/rmail/rmail $RPM_BUILD_ROOT%{_bindir}/rmail.postfix
for i in active bounce corrupt defer deferred flush incoming private saved maildrop public pid saved trace; do
    mkdir -p $RPM_BUILD_ROOT%{postfix_queue_dir}/$i
done
for i in smtp-sink smtp-source posttls-finger ; do
  install -c -m 755 bin/$i $RPM_BUILD_ROOT%{postfix_command_dir}/
  install -c -m 755 man/man1/$i.1 $RPM_BUILD_ROOT%{_mandir}/man1/
done
sed -i -r "s#(/man[158]/.*.[158]):f#\1.gz:f#" $RPM_BUILD_ROOT%{postfix_config_dir}/postfix-files
cat $RPM_BUILD_ROOT%{postfix_config_dir}/postfix-files
%if %{with sasl}
mkdir -p $RPM_BUILD_ROOT%{sasl_config_dir}
install -m 644 %{SOURCE100} $RPM_BUILD_ROOT%{sasl_config_dir}/smtpd.conf
%endif
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE101} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/smtp.postfix
mkdir -p $RPM_BUILD_ROOT%{postfix_doc_dir}
cp -p %{SOURCE3} COMPATIBILITY LICENSE TLS_ACKNOWLEDGEMENTS TLS_LICENSE $RPM_BUILD_ROOT%{postfix_doc_dir}
mkdir -p $RPM_BUILD_ROOT%{postfix_doc_dir}/examples{,/chroot-setup}
cp -pr examples/{qmail-local,smtpd-policy} $RPM_BUILD_ROOT%{postfix_doc_dir}/examples
cp -p examples/chroot-setup/LINUX2 $RPM_BUILD_ROOT%{postfix_doc_dir}/examples/chroot-setup
cp conf/{main,bounce}.cf.default $RPM_BUILD_ROOT%{postfix_doc_dir}
sed -i 's#%{postfix_config_dir}\(/bounce\.cf\.default\)#%{postfix_doc_dir}\1#' $RPM_BUILD_ROOT%{_mandir}/man5/bounce.5
rm -f $RPM_BUILD_ROOT%{postfix_config_dir}/{TLS_,}LICENSE
find $RPM_BUILD_ROOT%{postfix_doc_dir} -type f | xargs chmod 644
find $RPM_BUILD_ROOT%{postfix_doc_dir} -type d | xargs chmod 755
%if %{with pflogsumm}
install -c -m 644 pflogsumm-%{pflogsumm_ver}/pflogsumm-faq.txt $RPM_BUILD_ROOT%{postfix_doc_dir}/pflogsumm-faq.txt
install -c -m 644 pflogsumm-%{pflogsumm_ver}/pflogsumm.1 $RPM_BUILD_ROOT%{_mandir}/man1/pflogsumm.1
install -c pflogsumm-%{pflogsumm_ver}/pflogsumm $RPM_BUILD_ROOT%{postfix_command_dir}/pflogsumm
%endif
mantools/srctoman - auxiliary/qshape/qshape.pl > qshape.1
install -c qshape.1 $RPM_BUILD_ROOT%{_mandir}/man1/qshape.1
install -c auxiliary/qshape/qshape.pl $RPM_BUILD_ROOT%{postfix_command_dir}/qshape
rm -f $RPM_BUILD_ROOT%{postfix_config_dir}/aliases
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/sendmail.postfix $RPM_BUILD_ROOT%{_prefix}/lib/
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/misc
touch $RPM_BUILD_ROOT%{_var}/lib/misc/postfix.aliasesdb-stamp
for i in %{postfix_command_dir}/sendmail %{_bindir}/{mailq,newaliases,rmail} \
	%{_sysconfdir}/pam.d/smtp %{_prefix}/lib/sendmail \
	%{_mandir}/{man1/{mailq.1,newaliases.1},man5/aliases.5,man8/{sendmail.8,smtp{,d}.8}}
do
	touch $RPM_BUILD_ROOT$i
done
function split_file
{
  grep "$1" "$3" >> "$3.d/$2" || :
  sed -i "\|$1| d" "$3" || :
}
pushd $RPM_BUILD_ROOT%{postfix_config_dir}
for map in %{?with_mysql:mysql} %{?with_pgsql:pgsql} %{?with_sqlite:sqlite} \
%{?with_cdb:cdb} %{?with_ldap:ldap} %{?with_lmdb:lmdb} %{?with_pcre:pcre}; do
  rm -f dynamicmaps.cf.d/"$map" "postfix-files.d/$map"
  split_file "^\s*$map\b" "$map" dynamicmaps.cf
  sed -i "s|postfix-$map\\.so|%{postfix_shlib_dir}/\\0|" "dynamicmaps.cf.d/$map"
  split_file "^\$shlib_directory/postfix-$map\\.so:" "$map" postfix-files
  split_file "^\$manpage_directory/man5/${map}_table\\.5" "$map" postfix-files
  map_upper=`echo $map | tr '[:lower:]' '[:upper:]'`
  split_file "^\$readme_directory/${map_upper}_README:" "$map" postfix-files
done
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -e

%systemd_post %{name}.service
%{_sbindir}/postfix set-permissions upgrade-configuration \
	daemon_directory=%{postfix_daemon_dir} \
	command_directory=%{postfix_command_dir} \
	mail_owner=%{postfix_user} \
	setgid_group=%{maildrop_group} \
	manpage_directory=%{_mandir} \
	sample_directory=%{postfix_sample_dir} \
	readme_directory=%{postfix_readme_dir} &> /dev/null
ALTERNATIVES_DOCS=""
[ "%%{_excludedocs}" = 1 ] || ALTERNATIVES_DOCS='--follower %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.postfix.1.gz
	--follower %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man1/newaliases.postfix.1.gz
	--follower %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/sendmail.postfix.1.gz
	--follower %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.postfix.5.gz
	--follower %{_mandir}/man8/smtp.8.gz mta-smtpman %{_mandir}/man8/smtp.postfix.8.gz
	--follower %{_mandir}/man8/smtpd.8.gz mta-smtpdman %{_mandir}/man8/smtpd.postfix.8.gz'
alternatives --install %{postfix_command_dir}/sendmail mta %{postfix_command_dir}/sendmail.postfix 60 \
	--follower %{_bindir}/mailq mta-mailq %{_bindir}/mailq.postfix \
	--follower %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.postfix \
	--follower %{_sysconfdir}/pam.d/smtp mta-pam %{_sysconfdir}/pam.d/smtp.postfix \
	--follower %{_bindir}/rmail mta-rmail %{_bindir}/rmail.postfix \
	--follower %{_prefix}/lib/sendmail mta-sendmail %{_prefix}/lib/sendmail.postfix \
	$ALTERNATIVES_DOCS \
	--initscript postfix
test -h /usr/sbin || ln -s ../bin/sendmail /usr/sbin/sendmail 2>/dev/null || :
%if %{with sasl}
if [ -f %{_libdir}/sasl2/smtpd.conf ]; then
	mv -f %{_libdir}/sasl2/smtpd.conf %{sasl_config_dir}/smtpd.conf
	/sbin/restorecon %{sasl_config_dir}/smtpd.conf 2> /dev/null
fi
%endif
if [ ! -f %{sslkey} ]; then
  umask 077
  %{_bindir}/openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out %{sslkey} 2>/dev/null || echo "openssl genpkey failed"
fi
if [ ! -f %{sslcert} ]; then
  FQDN=`hostname`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi
  req_cmd="%{_bindir}/openssl req -new -key %{sslkey} -x509 -sha256 -days 365 -set_serial $RANDOM -out %{sslcert} \
    -subj /C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=${FQDN}/emailAddress=root@${FQDN}"
  $req_cmd -noenc -copy_extensions none 2>/dev/null || $req_cmd 2>/dev/null || echo "openssl req failed"
  chmod 644 %{sslcert}
fi
exit 0
%pre

%sysusers_create_compat %{SOURCE6}
if [ -e %{_mandir}/man8/smtp.8.gz ]; then
	[ -h %{_mandir}/man8/smtp.8.gz ] || rm -f %{_mandir}/man8/smtp.8.gz
fi
exit 0
%preun

%systemd_preun %{name}.service
if [ "$1" = 0 ]; then
    alternatives --remove mta %{postfix_command_dir}/sendmail.postfix
fi
exit 0
%postun

%systemd_postun_with_restart %{name}.service
%if 0%{?fedora} < 23 && 0%{?rhel} < 9 && 0%{?oreon} < 11
%post sysvinit

/sbin/chkconfig --add postfix >/dev/null 2>&1 ||:
%preun sysvinit

if [ "$1" = 0 ]; then
    %{_initrddir}/postfix stop >/dev/null 2>&1 ||:
    /sbin/chkconfig --del postfix >/dev/null 2>&1 ||:
fi
%postun sysvinit

[ "$1" -ge 1 ] && %{_initrddir}/postfix condrestart >/dev/null 2>&1 ||:
%triggerpostun -n postfix-sysvinit -- postfix < %{sysv2systemdnvr}

/sbin/chkconfig --add postfix >/dev/null 2>&1 || :
%endif
%triggerun -- postfix < %{sysv2systemdnvr}

%{_bindir}/systemd-sysv-convert --save postfix >/dev/null 2>&1 ||:
%{_bindir}/systemd-sysv-convert --apply postfix >/dev/null 2>&1 ||:
/sbin/chkconfig --del postfix >/dev/null 2>&1 || :
/bin/systemctl try-restart postfix.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n postfix-perl-scripts -f %{oreon_filedir}/postfix-perl-scripts.list
%files -n postfix-mysql -f %{oreon_filedir}/postfix-mysql.list
%files -n postfix-pgsql -f %{oreon_filedir}/postfix-pgsql.list
%files -n postfix-sqlite -f %{oreon_filedir}/postfix-sqlite.list
%files -n postfix-cdb -f %{oreon_filedir}/postfix-cdb.list
%files -n postfix-ldap -f %{oreon_filedir}/postfix-ldap.list
%files -n postfix-lmdb -f %{oreon_filedir}/postfix-lmdb.list
%files -n postfix-pcre -f %{oreon_filedir}/postfix-pcre.list

%changelog

%autochangelog
