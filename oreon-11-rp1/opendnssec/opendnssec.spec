%global source0_hash f0a72d83834328ffe5660549be9ab79dc396364d7ffec25411300789d0f269a0
%global _hardened_build 1
Summary:        DNSSEC key and zone management software
Name: opendnssec
Version: 2.1.14
Release:        1%{?dist}
License: BSD-2-Clause
Url: http://www.opendnssec.org/
Source0:        https://github.com/opendnssec/opendnssec/archive/refs/tags/%{version}.tar.gz#/opendnssec-%{version}.tar.gz
Source1:        ods-enforcerd.service
Source2:        ods-signerd.service
Source3:        ods.sysconfig
Source4:        conf.xml
Source5:        tmpfiles-opendnssec.conf
Source6:        opendnssec.cron
Source7:        opendnssec-2.1.sqlite_convert.sql
Source8:        opendnssec-2.1.sqlite_rpmversion.sql
Source9: %{name}-sysusers.conf
Patch1:        0001-Pass-right-remaining-buffer-size-in-hsm_hex_unparse-.patch
Patch2:        opendnssec-configure-c99.patch
Patch3:        opendnssec-2.1.14rc1-gcc14.patch
Patch4:        opendnssec-c99-2.patch
Patch5:        opendnssec-implicit-declarations.patch
Requires: opencryptoki, softhsm >= 2.5.0 , systemd-units
Requires: libxml2, libxslt sqlite
Requires(pre): shadow-utils
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%if 0%{?prever:1}
%ifarch %{java_arches}
%endif
%endif
# oreon:deps
BuildRequires:  CUnit-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  ldns-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libxml2-devel
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  procps-ng
BuildRequires:  sqlite-devel
BuildRequires:  systemd-units
# /oreon:deps
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
autoreconf
%endif
%configure --with-ldns=%{_libdir}
%make_build
%check

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
cp -a %{SOURCE7} %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/sqlite_convert.sql
cp -a %{SOURCE8} %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/rpmversion.sql
sed -i "s:^SCHEMA=.*schema:SCHEMA=%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/schema:" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
sed -i "s:find_problematic_zones.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/find_problematic_zones.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
sed -i "s:^SCHEMA=.*schema:SCHEMA=%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/schema:" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_mysql
sed -i "s:find_problematic_zones.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/find_problematic_zones.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_mysql
sed -i "s:sqlite_convert.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/sqlite_convert.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
%oreon_autofiles main

%pre

%sysusers_create_package %{name} %{SOURCE9}
%post

if [ "$1" -eq 1 ]; then
   %{_sbindir}/runuser -u ods -- %{_bindir}/softhsm2-util --init-token \
                --free --label "OpenDNSSEC" --pin 1234 --so-pin 1234
   if [ ! -s %{_localstatedir}/opendnssec/kasp.db ]; then
      echo y | %{_sbindir}/ods-enforcer-db-setup
      %{_bindir}/sqlite3 -batch %{_localstatedir}/opendnssec/kasp.db < %{_datadir}/opendnssec/migration/1.4-2.0_db_convert/rpmversion.sql
   fi
elif [ -z "$(%{_bindir}/sqlite3 %{_localstatedir}/opendnssec/kasp.db 'select * from rpm_migration;')" ]; then
   if [ -e %{_localstatedir}/opendnssec/rpm-migration-in-progress ]; then
      echo "previous (partial?) migration found - human intervention is needed"
   else
      echo "opendnssec 1.4 database found, migrating to 2.x"
      touch %{_localstatedir}/opendnssec/rpm-migration-in-progress
      mv -n %{_localstatedir}/opendnssec/kasp.db %{_localstatedir}/opendnssec/kasp.db-1.4
      echo "migrating conf.xml from 1.4 to 2.1 schema"
      cp -n %{_sysconfdir}/opendnssec/conf.xml %{_sysconfdir}/opendnssec/conf.xml-1.4
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
ods-enforcer update all >/dev/null 2>/dev/null ||:
%systemd_post ods-enforcerd.service
%systemd_post ods-signerd.service
%preun

%systemd_preun ods-enforcerd.service
%systemd_preun ods-signerd.service
%postun

%systemd_postun_with_restart ods-enforcerd.service
%systemd_postun_with_restart ods-signerd.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.14-3
- Import
