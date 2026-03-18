%global _hardened_build 1

%global systemctl_bin /usr/bin/systemctl
%global check_password_version 1.1

%global so_ver 2
%global so_ver_compat 2

# Build openldap-servers package and its libslapi in openldap-devel and openldap-compat
%bcond servers 1

# Build with argon2 support
%bcond argon2 %{undefined rhel}

# When you change "Version: " to the new major version, remember to change this value too
%global major_version 2.6

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name: openldap
Version: 2.6.13
Release: 1%{?dist}
Summary: LDAP support libraries
License: OLDAP-2.8
URL: http://www.openldap.org/

Source0: https://openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version}.tgz
Source1: slapd.service
Source2: slapd.tmpfiles
Source3: slapd.ldif
Source4: ldap.conf
Source6: openldap.sysusers
Source10: https://github.com/ltb-project/openldap-ppolicy-check-password/archive/v%{check_password_version}/openldap-ppolicy-check-password-%{check_password_version}.tar.gz
Source50: libexec-functions
Source52: libexec-check-config.sh

# Patches for 2.6
Patch0: openldap-manpages.patch
Patch1: openldap-reentrant-gethostby.patch

Patch3: openldap-smbk5pwd-overlay.patch
Patch4: openldap-ai-addrconfig.patch
Patch5: openldap-allop-overlay.patch

# fix back_perl problems with lt_dlopen()
# might cause crashes because of symbol collisions
# the proper fix is to link all perl modules against libperl
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=327585
Patch6: openldap-switch-to-lt_dlopenadvise-to-get-RTLD_GLOBAL-set.patch

# System-wide default for CA certs
Patch7: openldap-openssl-manpage-defaultCA.patch
Patch8: openldap-add-export-symbols-LDAP_CONNECTIONLESS.patch
Patch9: openldap-libldap-avoid-SSL-context-cleanup-during-library-des.patch
Patch10: openldap-ITS-10297-Defer-hostname-resolution-til-first-use.patch

# check-password module specific patches
Patch90: check-password-makefile.patch
Patch91: check-password.patch

BuildRequires: cyrus-sasl-devel
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: groff
BuildRequires: krb5-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libevent-devel
BuildRequires: libxcrypt-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: unixODBC-devel
BuildRequires: cracklib-devel
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
%if %{with argon2}
BuildRequires: libsodium-devel
%endif

%description
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools. LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet. The openldap package contains configuration files,
libraries, and documentation for OpenLDAP.

%package devel
Summary: LDAP development libraries and header files
Requires: openldap%{?_isa} = %{version}-%{release}
Requires: cyrus-sasl-devel%{?_isa}

%description devel
The openldap-devel package includes the development libraries and
header files needed for compiling applications that use LDAP
(Lightweight Directory Access Protocol) internals. LDAP is a set of
protocols for enabling directory services over the Internet. Install
this package only if you plan to develop or will need to compile
customized LDAP clients.

%package compat
Summary: Package providing legacy non-threaded libldap
Requires: openldap%{?_isa} = %{version}-%{release}
# since libldap is manually linked from libldap_r, the provides is not generated automatically
%ifarch armv7hl i686
Provides: libldap-2.4.so.%{so_ver_compat}
Provides: libldap_r-2.4.so.%{so_ver_compat}
Provides: liblber-2.4.so.%{so_ver_compat}
%if %{with servers}
Provides: libslapi-2.4.so.%{so_ver_compat}
%endif
%else
Provides: libldap-2.4.so.%{so_ver_compat}()(%{__isa_bits}bit)
Provides: libldap_r-2.4.so.%{so_ver_compat}()(%{__isa_bits}bit)
Provides: liblber-2.4.so.%{so_ver_compat}()(%{__isa_bits}bit)
%if %{with servers}
Provides: libslapi-2.4.so.%{so_ver_compat}()(%{__isa_bits}bit)
%endif
%endif

%description compat
The openldap-compat package contains shared libraries named as libldap-2.4.so,
%if %{with servers}
libldap_r-2.4.so, liblber-2.4.so and libslapi-2.4.so.
%else
libldap_r-2.4.so and liblber-2.4.so
%endif
The libraries are just links to the current version shared libraries,
and are available for compatibility reasons.

%if %{with servers}
%package servers
Summary: LDAP server
Requires: openldap%{?_isa} = %{version}-%{release}
%{?systemd_requires}
# migrationtools (slapadd functionality):
Provides: ldif2ldbm

%description servers
OpenLDAP is an open-source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools. LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet. This package contains the slapd server and related files.
# endif servers
%endif

%package clients
Summary: LDAP client utilities
Requires: openldap%{?_isa} = %{version}-%{release}

%description clients
OpenLDAP is an open-source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools. LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet. The openldap-clients package contains the client
programs needed for accessing and modifying OpenLDAP directories.

%prep
%setup -q -c -a 0 -a 10

pushd openldap-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1

# build smbk5pwd with other overlays
ln -s ../../../contrib/slapd-modules/smbk5pwd/smbk5pwd.c servers/slapd/overlays
mv contrib/slapd-modules/smbk5pwd/README contrib/slapd-modules/smbk5pwd/README.smbk5pwd
# build allop with other overlays
ln -s ../../../contrib/slapd-modules/allop/allop.c servers/slapd/overlays
mv contrib/slapd-modules/allop/README contrib/slapd-modules/allop/README.allop
mv contrib/slapd-modules/allop/slapo-allop.5 doc/man/man5/slapo-allop.5

mv servers/slapd/back-perl/README{,.back_perl}

# fix documentation encoding
for filename in doc/drafts/draft-ietf-ldapext-acl-model-xx.txt; do
  iconv -f iso-8859-1 -t utf-8 "$filename" > "$filename.utf8"
  mv "$filename.utf8" "$filename"
done

popd

pushd openldap-ppolicy-check-password-%{check_password_version}
%patch -P90 -p1
%patch -P91 -p1
popd

%build

%set_build_flags
# enable experimental support for LDAP over UDP (LDAP_CONNECTIONLESS)
export CFLAGS="${CFLAGS} ${LDFLAGS} -Wl,--as-needed -Wl,-z,now -DLDAP_CONNECTIONLESS"
# disable legacy hash algorithm
export CFLAGS="${CFLAGS} -DOPENSSL_NO_MD2"

pushd openldap-%{version}
%configure \
	--enable-debug \
	--enable-dynamic \
	--enable-versioning \
	\
	--enable-dynacl \
	--enable-cleartext \
	--enable-crypt \
	--enable-lmpasswd \
	--enable-spasswd \
	--enable-modules \
	--enable-perl \
	--enable-rewrite \
	--enable-rlookups \
%if %{with servers}
	--enable-slapi \
%if %{with argon2}
        --enable-argon2 \
%endif
%endif
	--disable-slp \
	\
	--enable-backends=mod \
	--enable-bdb=yes \
	--enable-hdb=yes \
	--enable-mdb=yes \
	--enable-monitor=yes \
	--disable-ndb \
	--disable-sql \
	--disable-wt \
	\
	--enable-overlays=mod \
	\
	--disable-static \
	\
	--enable-balancer=mod \
        \
	--with-cyrus-sasl \
	--without-fetch \
	--with-threads \
	--with-pic \
	--with-gnu-ld \
	\
	--libexecdir=%{_libdir}

%make_build
popd

pushd openldap-ppolicy-check-password-%{check_password_version}
%make_build LDAP_INC="-I../openldap-%{version}/include \
 -I../openldap-%{version}/servers/slapd \
 -I../openldap-%{version}/build-servers/include"
popd

%install

mkdir -p %{buildroot}%{_libdir}/
%if %{with servers}
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/openldap.conf
%endif

pushd openldap-%{version}
%make_install STRIP_OPTS=""
popd

# install check_password module
pushd openldap-ppolicy-check-password-%{check_password_version}
mv check_password.so check_password.so.%{check_password_version}
ln -s check_password.so.%{check_password_version} %{buildroot}%{_libdir}/openldap/check_password.so
install -m 755 check_password.so.%{check_password_version} %{buildroot}%{_libdir}/openldap/
# install -m 644 README %{buildroot}%{_libdir}/openldap
install -d -m 755 %{buildroot}%{_sysconfdir}/openldap
cat > %{buildroot}%{_sysconfdir}/openldap/check_password.conf <<EOF
# OpenLDAP pwdChecker library configuration

#useCracklib 1
#minPoints 3
#minUpper 0
#minLower 0
#minDigit 0
#minPunct 0
EOF
mv README{,.check_pwd}
popd

# setup directories for TLS certificates
mkdir -p %{buildroot}%{_sysconfdir}/openldap/certs

# setup data and runtime directories
mkdir -p %{buildroot}%{_sharedstatedir}
mkdir -p %{buildroot}%{_localstatedir}
install -m 0700 -d %{buildroot}%{_sharedstatedir}/ldap
install -m 0755 -d %{buildroot}%{_localstatedir}/run/openldap

# setup autocreation of runtime directories on tmpfs
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %SOURCE2 %{buildroot}%{_tmpfilesdir}/slapd.conf

# install default ldap.conf (customized)
rm %{buildroot}%{_sysconfdir}/openldap/ldap.conf
install -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/openldap/ldap.conf

# setup maintainance scripts
mkdir -p %{buildroot}%{_libexecdir}
install -m 0755 -d %{buildroot}%{_libexecdir}/openldap
install -m 0644 %SOURCE50 %{buildroot}%{_libexecdir}/openldap/functions
install -m 0755 %SOURCE52 %{buildroot}%{_libexecdir}/openldap/check-config.sh

# remove build root from config files and manual pages
perl -pi -e "s|%{buildroot}||g" %{buildroot}%{_sysconfdir}/openldap/*.conf
perl -pi -e "s|%{buildroot}||g" %{buildroot}%{_mandir}/*/*.*

# we don't need the default files -- RPM handles changes
rm %{buildroot}%{_sysconfdir}/openldap/*.default

# install an init script for the servers
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %SOURCE1 %{buildroot}%{_unitdir}/slapd.service

# move slapd out of _libdir
mv %{buildroot}%{_libdir}/slapd %{buildroot}%{_sbindir}/

# setup tools as symlinks to slapd
for X in acl add auth cat dn index modify passwd test schema ; do
  rm %{buildroot}%{_sbindir}/slap$X
  ln -s slapd %{buildroot}%{_sbindir}/slap$X
done

# re-symlink unversioned libraries, so ldconfig is not confused
pushd %{buildroot}%{_libdir}
v=%{version}
version=$(echo ${v%.[0-9]*})
for lib in liblber libldap %{?with_servers:libslapi}; do
        rm -f ${lib}.so
        ln -s ${lib}.so.%{so_ver} ${lib}.so
done

for lib in $(ls | grep libldap); do
    IFS='.'
    read -r -a libsplit <<< "$lib"
    if [[ -z "${libsplit[3]}" && -n "${libsplit[2]}" ]]
    then
        so_ver_short_2_4="%{so_ver_compat}"
    elif [ -n "${libsplit[3]}" ]
    then
        so_ver_full_2_4="%{so_ver_compat}.${libsplit[3]}.${libsplit[4]}"
    fi
    unset IFS
done

# Provide only libldap and copy it to libldap_r for both 2.4 and 2.6+ versions, make a versioned lib link
# We increase it by 2 because libldap-2.4 has the 'so.2' major version on 2.4.59 (one of the last versions which is EOL)
gcc -shared -o "%{buildroot}%{_libdir}/libldap-2.4.so.${so_ver_short_2_4}" -Wl,--no-as-needed \
       -Wl,-soname -Wl,libldap-2.4.so.${so_ver_short_2_4} -L "%{buildroot}%{_libdir}" -Wl,-z,now -lldap
gcc -shared -o "%{buildroot}%{_libdir}/libldap_r-2.4.so.${so_ver_short_2_4}" -Wl,--no-as-needed \
       -Wl,-soname -Wl,libldap_r-2.4.so.${so_ver_short_2_4} -L "%{buildroot}%{_libdir}" -Wl,-z,now -lldap
gcc -shared -o "%{buildroot}%{_libdir}/liblber-2.4.so.${so_ver_short_2_4}" -Wl,--no-as-needed \
       -Wl,-soname -Wl,liblber-2.4.so.${so_ver_short_2_4} -L "%{buildroot}%{_libdir}" -Wl,-z,now -llber
%if %{with servers}
gcc -shared -o "%{buildroot}%{_libdir}/libslapi-2.4.so.${so_ver_short_2_4}" -Wl,--no-as-needed \
       -Wl,-soname -Wl,libslapi-2.4.so.${so_ver_short_2_4} -L "%{buildroot}%{_libdir}" -Wl,-z,now -lslapi
ln -s libslapi-2.4.so.{${so_ver_short_2_4},${so_ver_full_2_4}}
%endif
ln -s libldap-2.4.so.{${so_ver_short_2_4},${so_ver_full_2_4}}
ln -s libldap_r-2.4.so.{${so_ver_short_2_4},${so_ver_full_2_4}}
ln -s liblber-2.4.so.{${so_ver_short_2_4},${so_ver_full_2_4}}

popd

# tweak permissions on the libraries to make sure they're correct
chmod 0755 %{buildroot}%{_libdir}/lib*.so*
chmod 0644 %{buildroot}%{_libdir}/lib*.*a
chmod 0644 %{buildroot}%{_libdir}/openldap/*.la

# slapd.conf(5) is obsoleted since 2.3, see slapd-config(5)
mkdir -p %{buildroot}%{_datadir}
install -m 0755 -d %{buildroot}%{_datadir}/openldap-servers
install -m 0644 %SOURCE3 %{buildroot}%{_datadir}/openldap-servers/slapd.ldif
install -m 0700 -d %{buildroot}%{_sysconfdir}/openldap/slapd.d
rm %{buildroot}%{_sysconfdir}/openldap/slapd.conf
rm %{buildroot}%{_sysconfdir}/openldap/slapd.ldif

# move doc files out of _sysconfdir
mv %{buildroot}%{_sysconfdir}/openldap/schema/README README.schema

# remove files which we don't want packaged
rm %{buildroot}%{_libdir}/*.la  # because we do not want files in %{_libdir}/openldap/ removed, yet

%ldconfig_scriptlets

%if %{with servers}

%post servers
%systemd_post slapd.service

# generate configuration if necessary
if [[ ! -f %{_sysconfdir}/openldap/slapd.d/cn=config.ldif && \
      ! -f %{_sysconfdir}/openldap/slapd.conf
   ]]; then
      # if there is no configuration available, generate one from the defaults
      mkdir -p %{_sysconfdir}/openldap/slapd.d/ &>/dev/null || :
      /usr/sbin/slapadd -F %{_sysconfdir}/openldap/slapd.d/ -n0 -l %{_datadir}/openldap-servers/slapd.ldif
      chown -R ldap:ldap %{_sysconfdir}/openldap/slapd.d/
      %{systemctl_bin} try-restart slapd.service &>/dev/null
fi

# restart after upgrade
if [ $1 -ge 1 ]; then
    %{systemctl_bin} condrestart slapd.service &>/dev/null || :
fi

exit 0

%preun servers
%systemd_preun slapd.service

%postun servers
%systemd_postun_with_restart slapd.service
%endif
# endif servers

%files
%doc openldap-%{version}/ANNOUNCEMENT
%doc openldap-%{version}/CHANGES
%license openldap-%{version}/COPYRIGHT
%license openldap-%{version}/LICENSE
%doc openldap-%{version}/README
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/certs
%config(noreplace) %{_sysconfdir}/openldap/ldap.conf
%dir %{_libexecdir}/openldap/
%{_libdir}/liblber.so.*
%{_libdir}/libldap.so.*
%if %{with servers}
%{_libdir}/libslapi.so.*
%endif
%{_mandir}/man5/ldif.5*
%{_mandir}/man5/ldap.conf.5*

%if %{with servers}
%files servers
%doc openldap-%{version}/contrib/slapd-modules/smbk5pwd/README.smbk5pwd
%doc openldap-%{version}/doc/guide/admin/*.html
%doc openldap-%{version}/doc/guide/admin/*.png
%doc openldap-%{version}/servers/slapd/back-perl/SampleLDAP.pm
%doc openldap-%{version}/servers/slapd/back-perl/README.back_perl
%doc openldap-ppolicy-check-password-%{check_password_version}/README.check_pwd
%doc README.schema
%config(noreplace) %dir %attr(0750,ldap,ldap) %{_sysconfdir}/openldap/slapd.d
%config(noreplace) %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/openldap/check_password.conf
%{_tmpfilesdir}/slapd.conf
%dir %attr(0700,ldap,ldap) %{_sharedstatedir}/ldap
%dir %attr(-,ldap,ldap) %{_localstatedir}/run/openldap
%{_unitdir}/slapd.service
%{_datadir}/openldap-servers/
%{_libdir}/openldap/accesslog*
%{_libdir}/openldap/allop*
%if %{with argon2}
%{_libdir}/openldap/argon2*
%{_mandir}/man5/slappw-argon2.5*
%else
%exclude %{_mandir}/man5/slappw-argon2.5*
%endif
%{_libdir}/openldap/auditlog*
%{_libdir}/openldap/autoca*
%{_libdir}/openldap/back_asyncmeta*
%{_libdir}/openldap/back_dnssrv*
%{_libdir}/openldap/back_ldap*
%{_libdir}/openldap/back_meta*
%{_libdir}/openldap/back_null*
%{_libdir}/openldap/back_passwd*
%{_libdir}/openldap/back_relay*
%{_libdir}/openldap/back_sock*
%{_libdir}/openldap/check_password*
%{_libdir}/openldap/collect*
%{_libdir}/openldap/constraint*
%{_libdir}/openldap/dds*
%{_libdir}/openldap/deref*
%{_libdir}/openldap/dyngroup*
%{_libdir}/openldap/dynlist*
%{_libdir}/openldap/home*
%{_libdir}/openldap/lloadd*
%{_libdir}/openldap/memberof*
%{_libdir}/openldap/nestgroup*
%{_libdir}/openldap/otp*
%{_libdir}/openldap/pcache*
%{_libdir}/openldap/ppolicy*
%{_libdir}/openldap/refint*
%{_libdir}/openldap/remoteauth*
%{_libdir}/openldap/retcode*
%{_libdir}/openldap/rwm*
%{_libdir}/openldap/seqmod*
%{_libdir}/openldap/smbk5pwd*
%{_libdir}/openldap/sssvlv*
%{_libdir}/openldap/syncprov*
%{_libdir}/openldap/translucent*
%{_libdir}/openldap/unique*
%{_libdir}/openldap/valsort*
%{_libexecdir}/openldap/functions
%{_libexecdir}/openldap/check-config.sh
%{_sbindir}/slap*
%{_mandir}/man5/lloadd.conf.5*
%{_mandir}/man8/lloadd.8*
%{_mandir}/man5/slapd*.5*
%{_mandir}/man5/slapo-*.5*
%{_mandir}/man8/slap*.8*
%{_sysusersdir}/openldap.conf
# obsolete configuration
%ghost %config(noreplace,missingok) %attr(0640,ldap,ldap) %{_sysconfdir}/openldap/slapd.conf
%else
%exclude %{_datadir}/openldap-servers/
%exclude %{_libdir}/openldap/
%exclude %{_libexecdir}/openldap/check-config.sh
%exclude %{_libexecdir}/openldap/functions
%exclude %{_mandir}/man5/slapd*.5*
%exclude %{_mandir}/man5/slapo-*.5*
%exclude %{_mandir}/man5/lloadd.conf.5*
%exclude %{_mandir}/man5/slappw-argon2.5*
%exclude %{_mandir}/man8/*
%exclude %{_sbindir}/slap*
%exclude %{_sysconfdir}/openldap/check_password.conf
%exclude %{_sysconfdir}/openldap/schema
%exclude %{_tmpfilesdir}/slapd.conf
%exclude %{_unitdir}/slapd.service
%endif
# endif servers


%files clients
%{_bindir}/ldap*
%{_mandir}/man1/ldap*.1*

%files devel
%doc openldap-%{version}/doc/drafts openldap-%{version}/doc/rfc
%{_libdir}/liblber.so
%{_libdir}/libldap.so
%if %{with servers}
%{_libdir}/libslapi.so
%endif
%{_includedir}/*
%{_libdir}/pkgconfig/lber.pc
%{_libdir}/pkgconfig/ldap.pc
%{_mandir}/man3/*

%files compat
%{_libdir}/libldap-2.4*.so.*
%{_libdir}/libldap_r-2.4*.so.*
%{_libdir}/liblber-2.4*.so.*
%if %{with servers}
%{_libdir}/libslapi-2.4*.so.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.13-1
- Prepare for Oreon 11 (RP1)
