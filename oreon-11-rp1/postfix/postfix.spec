# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 6367dcc6b9d6b444c4a1d09e9fda3abf1479d88c9c434a31cd5cfe06f9c36627
%global source53_sha256 5ccba9ec765720c79b9d8ae0f02e4c39f042d54e742a238ebb20b51a61915167
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source53_sha256:%(test -z "%{source53_sha256}" || { f="%{SOURCE53}"; test -f "$f" || { echo "oreon: missing Source53 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source53_sha256}" || { echo "oreon: Source53 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# plugins have unresolvable symbols in compile time
%undefine _strict_symbol_defs_build

%if 0%{?rhel} < 10
%bcond_without db
%else
%bcond_with db
%endif
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

# hardened build if not overrided
%{!?_hardened_build:%global _hardened_build 1}

# Postfix requires one exlusive uid/gid and a 2nd exclusive gid for its own
# use.  Let me know if the second gid collides with another package.
# Be careful: Redhat's 'mail' user & group isn't unique!
# It's now handled by systemd-sysusers.
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

# Filter private libraries
%global _privatelibs libpostfix-.+\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

Name: postfix
Summary: Postfix Mail Transport Agent
Version: 3.11.0
Release: 1%{?dist}
Epoch: 2
URL: http://www.postfix.org
License: (IPL-1.0 OR EPL-2.0) AND GPL-2.0-or-later AND BSD-4-Clause-UC
Requires(post): systemd systemd-sysv hostname
Requires(post): %{_sbindir}/alternatives
Requires(post): %{_bindir}/openssl
Requires(preun): %{_sbindir}/alternatives
Requires(preun): systemd
Requires(postun): systemd
# Required by /usr/libexec/postfix/postfix-script
Requires: diffutils
Requires: findutils
# for restorecon
Requires: policycoreutils
Provides: MTA smtpd smtpdaemon server(smtp)

Source0: http://ftp.porcupine.org/mirrors/postfix-release/official/%{name}-%{version}.tar.gz
Source1: postfix-etc-init.d-postfix
Source2: postfix.service
Source3: README-Postfix-SASL-RedHat.txt
Source4: postfix.aliasesdb
Source5: postfix-chroot-update
Source6: postfix.sysusers

# Sources 50-99 are upstream [patch] contributions

%define pflogsumm_ver 1.1.6

# Postfix Log Entry Summarizer: http://jimsun.linxnet.com/postfix_contrib.html
Source53: http://jimsun.linxnet.com/downloads/pflogsumm-%{pflogsumm_ver}.tar.gz

# Sources >= 100 are config files

Source100: postfix-sasl.conf
Source101: postfix-pam.conf

# Patches

Patch1: postfix-3.11.0-config.patch
Patch2: postfix-3.11.0-files.patch
Patch3: postfix-3.9.0-alternatives.patch
# probably rhbz#428996
Patch4: postfix-3.8.0-large-fs.patch
# rhbz#1931403, sent upstream
Patch9: pflogsumm-1.1.6-syslog-name-underscore-fix.patch
Patch11: postfix-3.4.4-chroot-example-fix.patch
%if 0%{?rhel}
Patch12: postfix-3.10.7-rhel-remove-version-mismatch-warning.patch
%endif

# Optional patches - set the appropriate environment variables to include
#                    them when building the package/spec file


# Determine the different packages required for building postfix
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: zlib-devel
BuildRequires: systemd-units
BuildRequires: libicu-devel
BuildRequires: gcc
BuildRequires: m4
BuildRequires: findutils
BuildRequires: systemd-rpm-macros
BuildRequires: sed
%if 0%{?rhel} < 9
BuildRequires: libnsl2-devel
%endif

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
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/sendmail
Provides: /usr/sbin/smtp-sink
%endif

%description
Postfix is a Mail Transport Agent (MTA).

%if 0%{?fedora} < 23 && 0%{?rhel} < 9
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
# perl-scripts introduced in 2:2.5.5-2
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
%oreon_verify_sources
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

%if 0%{?rhel}
%patch -P12 -p1 -b .warning
%endif

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
%if 0%{?rhel} >= 9
AUXLIBS=""
%else
AUXLIBS="-lnsl"
%endif

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
%if 0%{?rhel} >= 9
    CCARGS="${CCARGS} -DNO_NIS"
%endif
LDFLAGS="$LDFLAGS %{?_hardened_build:-Wl,-z,relro,-z,now}"

# SHLIB_RPATH is needed to find private libraries
# LDFLAGS are added to SHLIB_RPATH because the postfix build system
# ignores them. Adding LDFLAGS to SHLIB_RPATH is currently the only
# way how to get them in
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
# install postfix into $RPM_BUILD_ROOT

# Move stuff around so we don't conflict with sendmail
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

%if 0%{?fedora} < 23 && 0%{?rhel} < 9
# This installs into the /etc/rc.d/init.d directory
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
install -c %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/postfix
%endif

# Systemd
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
install -m 755 %{SOURCE4} %{buildroot}%{postfix_daemon_dir}/aliasesdb
install -m 755 %{SOURCE5} %{buildroot}%{postfix_daemon_dir}/chroot-update

# systemd-sysusers
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/postfix.conf

install -c auxiliary/rmail/rmail $RPM_BUILD_ROOT%{_bindir}/rmail.postfix

for i in active bounce corrupt defer deferred flush incoming private saved maildrop public pid saved trace; do
    mkdir -p $RPM_BUILD_ROOT%{postfix_queue_dir}/$i
done

# install performance benchmark and test tools by hand
for i in smtp-sink smtp-source posttls-finger ; do
  install -c -m 755 bin/$i $RPM_BUILD_ROOT%{postfix_command_dir}/
  install -c -m 755 man/man1/$i.1 $RPM_BUILD_ROOT%{_mandir}/man1/
done

## RPM compresses man pages automatically.
## - Edit postfix-files to reflect this, so post-install won't get confused
##   when called during package installation.
sed -i -r "s#(/man[158]/.*.[158]):f#\1.gz:f#" $RPM_BUILD_ROOT%{postfix_config_dir}/postfix-files

cat $RPM_BUILD_ROOT%{postfix_config_dir}/postfix-files
%if %{with sasl}
# Install the smtpd.conf file for SASL support.
mkdir -p $RPM_BUILD_ROOT%{sasl_config_dir}
install -m 644 %{SOURCE100} $RPM_BUILD_ROOT%{sasl_config_dir}/smtpd.conf
%endif

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE101} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/smtp.postfix

# prepare documentation
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

# install qshape
mantools/srctoman - auxiliary/qshape/qshape.pl > qshape.1
install -c qshape.1 $RPM_BUILD_ROOT%{_mandir}/man1/qshape.1
install -c auxiliary/qshape/qshape.pl $RPM_BUILD_ROOT%{postfix_command_dir}/qshape

# remove alias file
rm -f $RPM_BUILD_ROOT%{postfix_config_dir}/aliases

# create /usr/lib/sendmail
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf --relative $RPM_BUILD_ROOT%{_sbindir}/sendmail.postfix $RPM_BUILD_ROOT%{_prefix}/lib/

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/misc
touch $RPM_BUILD_ROOT%{_var}/lib/misc/postfix.aliasesdb-stamp

# prepare alternatives ghosts
for i in %{postfix_command_dir}/sendmail %{_bindir}/{mailq,newaliases,rmail} \
	%{_sysconfdir}/pam.d/smtp %{_prefix}/lib/sendmail \
	%{_mandir}/{man1/{mailq.1,newaliases.1},man5/aliases.5,man8/{sendmail.8,smtp{,d}.8}}
do
	touch $RPM_BUILD_ROOT$i
done

# helper for splitting content of dynamicmaps.cf and postfix-files
function split_file
{
# "|| :" to silently skip non existent records
  grep "$1" "$3" >> "$3.d/$2" || :
  sed -i "\|$1| d" "$3" || :
}

# split global dynamic maps configuration to individual sub-packages
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

%post -e
%systemd_post %{name}.service

# upgrade configuration files if necessary
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

# Make sure that /usr/sbin/sendmail is not missing, if /usr/sbin is a
# directory. The symlink will only be created if there is no symlink
# or file already.
test -h /usr/sbin || ln -s ../bin/sendmail /usr/sbin/sendmail 2>/dev/null || :

%if %{with sasl}
# Move sasl config to new location
if [ -f %{_libdir}/sasl2/smtpd.conf ]; then
	mv -f %{_libdir}/sasl2/smtpd.conf %{sasl_config_dir}/smtpd.conf
	/sbin/restorecon %{sasl_config_dir}/smtpd.conf 2> /dev/null
fi
%endif

# Create self-signed SSL certificate
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
# openssl-3.0 and fallback for backward compatibility with openssl < 3.0
  $req_cmd -noenc -copy_extensions none 2>/dev/null || $req_cmd 2>/dev/null || echo "openssl req failed"
  chmod 644 %{sslcert}
fi

exit 0

%pre
# Add user and groups if necessary
%sysusers_create_compat %{SOURCE6}

# hack, to turn man8/smtp.8.gz into alternatives symlink (part of the rhbz#2274402 fix)
# this could be probably dropped in f44+
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

%if 0%{?fedora} < 23 && 0%{?rhel} < 9
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




%files

# For correct directory permissions check postfix-install script.
# It reads the file postfix-files which defines the ownership
# and permissions for all files postfix installs.

%defattr(-, root, root, -)

# Config files not part of upstream

%if %{with sasl}
%config(noreplace) %{sasl_config_dir}/smtpd.conf
%endif
%config(noreplace) %{_sysconfdir}/pam.d/smtp.postfix
%{_unitdir}/postfix.service

# Documentation

%{postfix_doc_dir}
%if %{with pflogsumm}
%exclude %{postfix_doc_dir}/pflogsumm-faq.txt
%endif

# Exclude due to dynamic maps subpackages
%exclude %{_mandir}/man5/mysql_table.5*
%exclude %{postfix_doc_dir}/README_FILES/MYSQL_README
%exclude %{_mandir}/man5/pgsql_table.5*
%exclude %{postfix_doc_dir}/README_FILES/PGSQL_README
%exclude %{_mandir}/man5/sqlite_table.5*
%exclude %{postfix_doc_dir}/README_FILES/SQLITE_README
%exclude %{postfix_doc_dir}/README_FILES/CDB_README
%exclude %{_mandir}/man5/ldap_table.5*
%exclude %{postfix_doc_dir}/README_FILES/LDAP_README
%exclude %{_mandir}/man5/lmdb_table.5*
%exclude %{postfix_doc_dir}/README_FILES/LMDB_README
%exclude %{_mandir}/man5/pcre_table.5*
%exclude %{postfix_doc_dir}/README_FILES/PCRE_README

# Misc files

%dir %attr(0755, root, root) %{postfix_config_dir}
%dir %attr(0755, root, root) %{postfix_daemon_dir}
%dir %attr(0755, root, root) %{postfix_queue_dir}
%dir %attr(0755, root, root) %{postfix_shlib_dir}
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/active
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/bounce
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/corrupt
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/defer
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/deferred
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/flush
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/hold
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/incoming
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/saved
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/trace
%dir %attr(0730, %{postfix_user}, %{maildrop_group}) %{postfix_queue_dir}/maildrop
%dir %attr(0755, root, root) %{postfix_queue_dir}/pid
%dir %attr(0700, %{postfix_user}, root) %{postfix_queue_dir}/private
%dir %attr(0710, %{postfix_user}, %{maildrop_group}) %{postfix_queue_dir}/public
%dir %attr(0700, %{postfix_user}, root) %{postfix_data_dir}
%dir %attr(0755, root, root) %{postfix_config_dir}/dynamicmaps.cf.d
%dir %attr(0755, root, root) %{postfix_config_dir}/postfix-files.d

%attr(0644, root, root) %{_mandir}/man1/post*.1*
%attr(0644, root, root) %{_mandir}/man1/smtp*.1*
%attr(0644, root, root) %{_mandir}/man1/*.postfix.1*
%attr(0644, root, root) %{_mandir}/man5/access.5*
%attr(0644, root, root) %{_mandir}/man5/[b-v]*.5*
%attr(0644, root, root) %{_mandir}/man5/*.postfix.5*
%attr(0644, root, root) %{_mandir}/man8/[a-qt-v]*.8*
%attr(0644, root, root) %{_mandir}/man8/s[ch-lnp]*.8*
%attr(0644, root, root) %{_mandir}/man8/smtp.postfix.8*
%attr(0644, root, root) %{_mandir}/man8/smtpd.postfix.8*

%attr(0755, root, root) %{postfix_command_dir}/smtp-sink
%attr(0755, root, root) %{postfix_command_dir}/smtp-source
%attr(0755, root, root) %{postfix_command_dir}/posttls-finger

%attr(0755, root, root) %{postfix_command_dir}/postalias
%attr(0755, root, root) %{postfix_command_dir}/postcat
%attr(0755, root, root) %{postfix_command_dir}/postconf
%attr(2755, root, %{maildrop_group}) %{postfix_command_dir}/postdrop
%attr(0755, root, root) %{postfix_command_dir}/postfix
%attr(0755, root, root) %{postfix_command_dir}/postkick
%attr(0755, root, root) %{postfix_command_dir}/postlock
%attr(2755, root, %{maildrop_group}) %{postfix_command_dir}/postlog
%attr(0755, root, root) %{postfix_command_dir}/postmap
%attr(0755, root, root) %{postfix_command_dir}/postmulti
%attr(2755, root, %{maildrop_group}) %{postfix_command_dir}/postqueue
%attr(0755, root, root) %{postfix_command_dir}/postsuper
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/access
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/canonical
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/generic
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/header_checks
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/main.cf
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/main.cf.proto
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/master.cf
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/master.cf.proto
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/relocated
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/transport
%attr(0644, root, root) %config(noreplace) %{postfix_config_dir}/virtual
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf
%attr(0755, root, root) %{postfix_daemon_dir}/[^mp]*
%attr(0755, root, root) %{postfix_daemon_dir}/master
%attr(0755, root, root) %{postfix_daemon_dir}/pickup
%attr(0755, root, root) %{postfix_daemon_dir}/pipe
%attr(0755, root, root) %{postfix_daemon_dir}/post-install
%attr(0644, root, root) %{postfix_config_dir}/postfix-files
%attr(0755, root, root) %{postfix_daemon_dir}/postfix-non-bdb-script
%attr(0755, root, root) %{postfix_daemon_dir}/postfix-script
%attr(0755, root, root) %{postfix_daemon_dir}/postfix-tls-script
%attr(0755, root, root) %{postfix_daemon_dir}/postfix-wrapper
%attr(0755, root, root) %{postfix_daemon_dir}/postmulti-script
%attr(0755, root, root) %{postfix_daemon_dir}/postscreen
%attr(0755, root, root) %{postfix_daemon_dir}/postlogd
%attr(0755, root, root) %{postfix_daemon_dir}/proxymap
%attr(0755, root, root) %{postfix_shlib_dir}/libpostfix-*.so
%{_bindir}/mailq.postfix
%{_bindir}/newaliases.postfix
%attr(0755, root, root) %{_bindir}/rmail.postfix
%attr(0755, root, root) %{_sbindir}/sendmail.postfix
%{_prefix}/lib/sendmail.postfix

%ghost %{_sysconfdir}/pam.d/smtp

%ghost %{_mandir}/man1/mailq.1.gz
%ghost %{_mandir}/man1/newaliases.1.gz
%ghost %{_mandir}/man5/aliases.5.gz
%ghost %{_mandir}/man8/sendmail.8.gz
%ghost %{_mandir}/man8/smtp.8.gz
%ghost %{_mandir}/man8/smtpd.8.gz

%ghost %attr(0755, root, root) %{_bindir}/mailq
%ghost %attr(0755, root, root) %{_bindir}/newaliases
%ghost %attr(0755, root, root) %{_bindir}/rmail
%ghost %attr(0755, root, root) %{_sbindir}/sendmail
%ghost %attr(0755, root, root) %{_prefix}/lib/sendmail

%ghost %attr(0644, root, root) %{_var}/lib/misc/postfix.aliasesdb-stamp

# systemd-sysusers
%{_sysusersdir}/postfix.conf

%if 0%{?fedora} < 23 && 0%{?rhel} < 9
%files sysvinit
%{_initrddir}/postfix
%endif

%files perl-scripts
%attr(0755, root, root) %{postfix_command_dir}/qshape
%attr(0644, root, root) %{_mandir}/man1/qshape*
%if %{with pflogsumm}
%doc %{postfix_doc_dir}/pflogsumm-faq.txt
%attr(0644, root, root) %{_mandir}/man1/pflogsumm.1.gz
%attr(0755, root, root) %{postfix_command_dir}/pflogsumm
%endif

%if %{with mysql}
%files mysql
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/mysql
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/mysql
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-mysql.so
%attr(0644, root, root) %{_mandir}/man5/mysql_table.5*
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/MYSQL_README

%endif

%if %{with pgsql}
%files pgsql
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/pgsql
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/pgsql
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-pgsql.so
%attr(0644, root, root) %{_mandir}/man5/pgsql_table.5*
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/PGSQL_README
%endif

%if %{with sqlite}
%files sqlite
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/sqlite
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/sqlite
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-sqlite.so
%attr(0644, root, root) %{_mandir}/man5/sqlite_table.5*
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/SQLITE_README
%endif

%if %{with cdb}
%files cdb
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/cdb
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/cdb
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-cdb.so
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/CDB_README
%endif

%if %{with ldap}
%files ldap
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/ldap
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/ldap
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-ldap.so
%attr(0644, root, root) %{_mandir}/man5/ldap_table.5*
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/LDAP_README
%endif

%if %{with lmdb}
%files lmdb
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/lmdb
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/lmdb
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-lmdb.so
%attr(0644, root, root) %{_mandir}/man5/lmdb_table.5*
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/LMDB_README
%endif

%if %{with pcre}
%files pcre
%attr(0644, root, root) %{postfix_config_dir}/dynamicmaps.cf.d/pcre
%attr(0644, root, root) %{postfix_config_dir}/postfix-files.d/pcre
%attr(0755, root, root) %{postfix_shlib_dir}/postfix-pcre.so
%attr(0644, root, root) %{_mandir}/man5/pcre_table.5*
%attr(0644, root, root) %{postfix_doc_dir}/README_FILES/PCRE_README
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.11.0-1
- Prepare for Oreon 11 (RP1)
