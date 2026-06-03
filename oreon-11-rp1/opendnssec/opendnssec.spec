%global source0_hash none

%global _hardened_build 1

Summary: DNSSEC key and zone management software
Name: opendnssec
Version: 2.1.14
Release: 3%{?dist}
License: BSD-2-Clause
Url: http://www.opendnssec.org/
Source0:        https://dist.opendnssec.org/source/%{?prever:testing/}%{name}-%{version}%{?prever}.tar.gz
Source10:        https://dist.opendnssec.org/source/%{?prever:testing/}%{name}-%{version}%{?prever}.tar.gz.sig
Source1:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/ods-enforcerd.service
Source2:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/ods-signerd.service
Source3:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/ods.sysconfig
Source4:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/conf.xml
Source5:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/tmpfiles-opendnssec.conf
Source6:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/opendnssec.cron
Source7:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/opendnssec-2.1.sqlite_convert.sql
Source8:        https://src.fedoraproject.org/rpms/opendnssec/raw/rawhide/f/opendnssec-2.1.sqlite_rpmversion.sql
Source9: %{name}-sysusers.conf
Patch1: 0001-Pass-right-remaining-buffer-size-in-hsm_hex_unparse-.patch
Patch2: opendnssec-configure-c99.patch
Patch3: opendnssec-2.1.14rc1-gcc14.patch
Patch4: opendnssec-c99-2.patch
Patch5: opendnssec-implicit-declarations.patch

Requires: opencryptoki, softhsm >= 2.5.0 , systemd-units
Requires: libxml2, libxslt sqlite
BuildRequires: make
BuildRequires:  gcc
BuildRequires: ldns-devel >= 1.6.12, sqlite-devel >= 3.0.0, openssl-devel
BuildRequires: libxml2-devel CUnit-devel, doxygen
# It tests for pkill/killall and would use /bin/false if not found
BuildRequires: procps-ng
BuildRequires: perl-interpreter
BuildRequires: libmicrohttpd-devel jansson-devel libyaml-devel

BuildRequires: systemd-units
Requires(pre): shadow-utils
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%if 0%{?prever:1}
# For building development snapshots
Buildrequires: autoconf, automake, libtool
%ifarch %{java_arches}
Buildrequires: java
%endif
%endif

%description
OpenDNSSEC was created as an open-source turn-key solution for DNSSEC.
It secures zone data just before it is published in an authoritative
name server. It requires a PKCS#11 crypto module library, such as softhsm

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}%{?prever}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# Prevent re-running autoconf.
touch -r aclocal.m4 configure* m4/*

# bump default policy ZSK keysize to 2048
sed -i "s/1024/2048/" conf/kasp.xml.in

%build
export LDFLAGS="-Wl,-z,relro,-z,now -pie -specs=/usr/lib/rpm/redhat/redhat-hardened-ld"
export CFLAGS="$RPM_OPT_FLAGS -fPIE -pie -Wextra -Wformat -Wformat-nonliteral -Wformat-security"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIE -pie -Wformat-nonliteral -Wformat-security"
%if 0%{?prever:1}
# for development snapshots
autoreconf
%endif
%configure --with-ldns=%{_libdir}
%make_build

%check
# Requires sample db not shipped with upstream
# make check

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_localstatedir}/opendnssec/{tmp,signed,signconf,enforcer}
install -d -m 0755 %{buildroot}%{_initrddir} %{buildroot}%{_sysconfdir}/cron.d/
install -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/cron.d/opendnssec
rm -f %{buildroot}/%{_sysconfdir}/opendnssec/*.sample
install -d -m 0755 %{buildroot}/%{_sysconfdir}/sysconfig
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/ods
install -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/opendnssec/
install -D %{SOURCE9} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/opendnssec.conf
mkdir -p %{buildroot}%{_localstatedir}/run/opendnssec
mkdir -p %{buildroot}%{_datadir}/opendnssec/
cp -a enforcer/utils %{buildroot}%{_datadir}/opendnssec/migration
cp -a enforcer/src/db/schema.* %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/
# fixup path for mysql/sqlite. Use our replacement sqlite_convert.sql to detect previous migration
cp -a %{SOURCE7} %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/sqlite_convert.sql
cp -a %{SOURCE8} %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/rpmversion.sql
sed -i "s:^SCHEMA=.*schema:SCHEMA=%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/schema:" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
sed -i "s:find_problematic_zones.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/find_problematic_zones.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
sed -i "s:^SCHEMA=.*schema:SCHEMA=%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/schema:" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_mysql
sed -i "s:find_problematic_zones.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/find_problematic_zones.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_mysql
sed -i "s:sqlite_convert.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/sqlite_convert.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite


%files
%{_unitdir}/ods-enforcerd.service
%{_unitdir}/ods-signerd.service
%config(noreplace) %{_tmpfilesdir}/opendnssec.conf
%attr(0770,root,ods) %dir %{_sysconfdir}/opendnssec
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec/tmp
%attr(0775,root,ods) %dir %{_localstatedir}/opendnssec/signed
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec/signconf
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec/enforcer
%attr(0660,root,ods) %config(noreplace) %{_sysconfdir}/opendnssec/*.xml
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/ods
%attr(0770,root,ods) %dir %{_localstatedir}/run/opendnssec
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/opendnssec
%doc NEWS README.md
%license LICENSE
%{_mandir}/*/*
%{_sbindir}/*
%{_bindir}/*
%attr(0755,root,root) %dir %{_datadir}/opendnssec
%{_datadir}/opendnssec/*
%{_sysusersdir}/%{name}.conf

%pre

%sysusers_create_package %{name} %{SOURCE9}

%post
# Initialise a slot on the softhsm on first install
if [ "$1" -eq 1 ]; then
   %{_sbindir}/runuser -u ods -- %{_bindir}/softhsm2-util --init-token \
                --free --label "OpenDNSSEC" --pin 1234 --so-pin 1234
   if [ ! -s %{_localstatedir}/opendnssec/kasp.db ]; then
      echo y | %{_sbindir}/ods-enforcer-db-setup
      %{_bindir}/sqlite3 -batch %{_localstatedir}/opendnssec/kasp.db < %{_datadir}/opendnssec/migration/1.4-2.0_db_convert/rpmversion.sql
   fi

elif [ -z "$(%{_bindir}/sqlite3 %{_localstatedir}/opendnssec/kasp.db 'select * from rpm_migration;')" ]; then
   # Migrate version 1.4 db to version 2.1 db
   if [ -e %{_localstatedir}/opendnssec/rpm-migration-in-progress ]; then
      echo "previous (partial?) migration found - human intervention is needed"
   else
      echo "opendnssec 1.4 database found, migrating to 2.x"
      touch %{_localstatedir}/opendnssec/rpm-migration-in-progress
      mv -n %{_localstatedir}/opendnssec/kasp.db %{_localstatedir}/opendnssec/kasp.db-1.4
      echo "migrating conf.xml from 1.4 to 2.1 schema"
      cp -n %{_sysconfdir}/opendnssec/conf.xml %{_sysconfdir}/opendnssec/conf.xml-1.4
      # fixup incompatibilities inflicted upon us by upstream :(
      sed -i "/<Interval>.*Interval>/d" %{_sysconfdir}/opendnssec/conf.xml
      echo "Converting kasp.db"
      ERR=""
      %{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite -i %{_localstatedir}/opendnssec/kasp.db-1.4 -o %{_localstatedir}/opendnssec/kasp.db || ERR="convert_sqlite error"
      chown ods.ods %{_localstatedir}/opendnssec/kasp.db
      cp -n %{_sysconfdir}/opendnssec/zonelist.xml %{_localstatedir}/opendnssec/enforcer/zones.xml
      if [ -z "$ERR" ]; then
         echo "calling ods-migrate"
         ods-migrate || ERR="ods-migrate failed"
         if [ -z "$ERR" ]; then
            echo "opendnssec 1.4 to 2.x migration completed"
            rm %{_localstatedir}/opendnssec/rpm-migration-in-progress
         else
            echo "ods-migrate process failed - human intervention is needed"
         fi
      else
         echo "%{_localstatedir}/opendnssec/kasp.db conversion failed - not calling ods-migrate to complete migration. human intervention is needed"
      fi
   fi
fi

# in case we update any xml conf file
ods-enforcer update all >/dev/null 2>/dev/null ||:

%systemd_post ods-enforcerd.service
%systemd_post ods-signerd.service

%preun
%systemd_preun ods-enforcerd.service
%systemd_preun ods-signerd.service

%postun
%systemd_postun_with_restart ods-enforcerd.service
%systemd_postun_with_restart ods-signerd.service

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.14-3
- Import
