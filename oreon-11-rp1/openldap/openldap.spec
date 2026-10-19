%global source0_hash 253db80f301258ea69cda1184766d57395b836aaabf41157eb0316eb0fac1341
%global source10_hash 45188b404eb71c3ba47e9eb5d77bfda53e636571bb1db70e9da8e88d48b17400
%global _hardened_build 1
%global systemctl_bin /usr/bin/systemctl
%global check_password_version 1.1
%global so_ver 2
%global so_ver_compat 2
%bcond servers 1
%bcond argon2 %{undefined rhel}
%global major_version 2.7
%global __brp_remove_la_files %nil
Name: openldap
Version: 2.7.1
Release:        1%{?dist}
Summary:        LDAP support libraries
License: OLDAP-2.8
URL: http://www.openldap.org/
Source0:        https://openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version}.tgz
Source1: slapd.service
Source2: slapd.tmpfiles
Source3: slapd.ldif
Source4: ldap.conf
Source6: openldap.sysusers
Source10:        https://github.com/ltb-project/openldap-ppolicy-check-password/archive/refs/tags/v1.1.tar.gz#/openldap-ppolicy-check-password-1.1.tar.gz
Source50: libexec-functions
Source52: libexec-check-config.sh
Patch0: openldap-manpages.patch
Patch1: openldap-reentrant-gethostby.patch
Patch3: openldap-smbk5pwd-overlay.patch
Patch4: openldap-ai-addrconfig.patch
Patch5: openldap-allop-overlay.patch
Patch6: openldap-switch-to-lt_dlopenadvise-to-get-RTLD_GLOBAL-set.patch
Patch7: openldap-openssl-manpage-defaultCA.patch
Patch9: openldap-libldap-avoid-SSL-context-cleanup-during-library-des.patch
Patch90: check-password-makefile.patch
Patch91: check-password.patch
%if %{with argon2}
%endif
# oreon:deps
BuildRequires:  cracklib-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  groff
BuildRequires:  krb5-devel
BuildRequires:  libevent-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  unixODBC-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; }
%setup -q -c -a 0 -a 10

pushd openldap-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P9 -p1
sed -i 's/#ifdef LDAP_CONNECTIONLESS/#if 1/' libraries/liblber/sockbuf.c libraries/liblber/lber.map

# build smbk5pwd with other overlays
ln -s ../../../contrib/slapd-modules/smbk5pwd/smbk5pwd.c servers/slapd/overlays
mv contrib/slapd-modules/smbk5pwd/README contrib/slapd-modules/smbk5pwd/README.smbk5pwd
# build allop with other overlays
ln -s ../../../contrib/slapd-modules/allop/allop.c servers/slapd/overlays
mv contrib/slapd-modules/allop/README contrib/slapd-modules/allop/README.allop
mv contrib/slapd-modules/allop/slapo-allop.5 doc/man/man5/slapo-allop.5

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
export CFLAGS="${CFLAGS} ${LDFLAGS} -Wl,--as-needed -Wl,-z,now -DLDAP_CONNECTIONLESS"
export CPPFLAGS="${CPPFLAGS:-} -DLDAP_CONNECTIONLESS"
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
pushd openldap-ppolicy-check-password-%{check_password_version}
mv check_password.so check_password.so.%{check_password_version}
ln -s check_password.so.%{check_password_version} %{buildroot}%{_libdir}/openldap/check_password.so
install -m 755 check_password.so.%{check_password_version} %{buildroot}%{_libdir}/openldap/
install -d -m 755 %{buildroot}%{_sysconfdir}/openldap
cat > %{buildroot}%{_sysconfdir}/openldap/check_password.conf <<EOF
EOF
mv README{,.check_pwd}
popd
mkdir -p %{buildroot}%{_sysconfdir}/openldap/certs
mkdir -p %{buildroot}%{_sharedstatedir}
mkdir -p %{buildroot}%{_localstatedir}
install -m 0700 -d %{buildroot}%{_sharedstatedir}/ldap
install -m 0755 -d %{buildroot}%{_localstatedir}/run/openldap
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %SOURCE2 %{buildroot}%{_tmpfilesdir}/slapd.conf
rm %{buildroot}%{_sysconfdir}/openldap/ldap.conf
install -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/openldap/ldap.conf
mkdir -p %{buildroot}%{_libexecdir}
install -m 0755 -d %{buildroot}%{_libexecdir}/openldap
install -m 0644 %SOURCE50 %{buildroot}%{_libexecdir}/openldap/functions
install -m 0755 %SOURCE52 %{buildroot}%{_libexecdir}/openldap/check-config.sh
perl -pi -e "s|%{buildroot}||g" %{buildroot}%{_sysconfdir}/openldap/*.conf
perl -pi -e "s|%{buildroot}||g" %{buildroot}%{_mandir}/*/*.*
rm %{buildroot}%{_sysconfdir}/openldap/*.default
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %SOURCE1 %{buildroot}%{_unitdir}/slapd.service
mv %{buildroot}%{_libdir}/slapd %{buildroot}%{_sbindir}/
for X in acl add auth cat dn index modify passwd test schema ; do
  rm %{buildroot}%{_sbindir}/slap$X
  ln -s slapd %{buildroot}%{_sbindir}/slap$X
done
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
chmod 0755 %{buildroot}%{_libdir}/lib*.so*
chmod 0644 %{buildroot}%{_libdir}/lib*.*a
chmod 0644 %{buildroot}%{_libdir}/openldap/*.la
mkdir -p %{buildroot}%{_datadir}
install -m 0755 -d %{buildroot}%{_datadir}/openldap-servers
install -m 0644 %SOURCE3 %{buildroot}%{_datadir}/openldap-servers/slapd.ldif
install -m 0700 -d %{buildroot}%{_sysconfdir}/openldap/slapd.d
rm %{buildroot}%{_sysconfdir}/openldap/slapd.conf
rm %{buildroot}%{_sysconfdir}/openldap/slapd.ldif
mv %{buildroot}%{_sysconfdir}/openldap/schema/README README.schema
rm %{buildroot}%{_libdir}/*.la  # because we do not want files in %{_libdir}/openldap/ removed, yet
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with servers}
%post servers

%systemd_post slapd.service
if [[ ! -f %{_sysconfdir}/openldap/slapd.d/cn=config.ldif && \
      ! -f %{_sysconfdir}/openldap/slapd.conf
   ]]; then
      mkdir -p %{_sysconfdir}/openldap/slapd.d/ &>/dev/null || :
      /usr/sbin/slapadd -F %{_sysconfdir}/openldap/slapd.d/ -n0 -l %{_datadir}/openldap-servers/slapd.ldif
      chown -R ldap:ldap %{_sysconfdir}/openldap/slapd.d/
      %{systemctl_bin} try-restart slapd.service &>/dev/null
fi
if [ $1 -ge 1 ]; then
    %{systemctl_bin} condrestart slapd.service &>/dev/null || :
fi
exit 0
%preun servers

%systemd_preun slapd.service
%postun servers

%systemd_postun_with_restart slapd.service
%endif
%files -f %{oreon_filedir}/main.list
%files -n openldap-devel -f %{oreon_filedir}/openldap-devel.list
%files -n openldap-compat -f %{oreon_filedir}/openldap-compat.list
%files -n openldap-servers -f %{oreon_filedir}/openldap-servers.list
%files -n openldap-clients -f %{oreon_filedir}/openldap-clients.list

%changelog

%autochangelog
