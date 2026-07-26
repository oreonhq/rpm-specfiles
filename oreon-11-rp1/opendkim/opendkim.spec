%global source0_hash cdbaf12b0d8f38c19d24b34db998ec156635b8d2f7c9f0245c061348250df6c8

%global upname OpenDKIM
%global bigname OPENDKIM

%global full_version 2.11.0-Beta2

Summary: A DomainKeys Identified Mail (DKIM) milter to sign and/or verify mail
Name: opendkim
Version: 2.11.0
Release: 0.44%{?dist}
License: BSD-3-Clause AND Sendmail-Open-Source-1.1
URL: http://%{name}.org/
Source0: https://github.com/trusteddomainproject/OpenDKIM/archive/%{full_version}.tar.gz
Source1: opendkim.conf
Source2: opendkim.sysconfig
Source3: SigningTable
Source4: KeyTable
Source5: TrustedHosts
Source6: README.fedora

# https://github.com/trusteddomainproject/OpenDKIM/pull/70
Patch0: 0001-support-for-lua-5.3.patch
# https://github.com/trusteddomainproject/OpenDKIM/pull/136
Patch1: opendkim-2.11.0-comment-separator.patch
# systemd service type=simple
Patch2: opendkim-systemd-service-simple.patch
# https://github.com/trusteddomainproject/OpenDKIM/pull/189
Patch3: opendkim-CVE-2022-48521-fix.patch

# Required for all versions
Requires: lib%{name}%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires: openssl-devel, libtool, pkgconfig, libbsd, libbsd-devel, opendbx-devel, lua-devel

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: libdb-devel
# Fedora 35+ and CentOS 9+ changed to libmemcached-awesome
%if 0%{?fedora} >= 35 || 0%{?epel} >= 9
BuildRequires: libmemcached-awesome-devel
%else
BuildRequires: libmemcached-devel
%endif

BuildRequires: sendmail-milter-devel

BuildRequires: openldap-devel

%description
%{upname} allows signing and/or verification of email through an open source
library that implements the DKIM service, plus a milter-based filter
application that can plug in to any milter-aware MTA, including sendmail,
Postfix, or any other MTA that supports the milter protocol.

%package -n %{name}-tools
Summary: An open source DKIM library

%description -n %{name}-tools
This package contains the tools necessary to create artifacts needed
by opendkim.

%package -n lib%{name}
Summary: An open source DKIM library
Obsoletes: %{name}-sysvinit < 2.10.1-5

%description -n lib%{name}
This package contains the library files required for running services built
using libopendkim.

%package -n lib%{name}-devel
Summary: Development files for lib%{name}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopendkim.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upname}-%{full_version}

# Create a sysusers.d config file
cat >opendkim.sysusers.conf <<EOF
u opendkim - '%{upname} Milter' %{_rundir}/%{name} -
m opendkim mail
EOF

%build
autoreconf -iv
# Always use system libtool instead of pacakge-provided one to
# properly handle 32 versus 64 bit detection and settings
%define LIBTOOL LIBTOOL=`which libtool`

%configure --with-odbx --with-db --with-libmemcached --with-openldap --enable-query_cache --with-lua

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build CFLAGS="%{optflags} -std=gnu17"

%install
%make_install
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -Dm 0755 contrib/init/redhat/%{name}-default-keygen %{buildroot}%{_sbindir}/%{name}-default-keygen

install -d -m 0755 %{buildroot}%{_unitdir}

# fix service file for rundir
sed -i -e "s:PIDFile=/var/run/opendkim/opendkim.pid:PIDFile=%{_rundir}/opendkim/opendkim.pid:" contrib/systemd/%{name}.service
install -m 0644 contrib/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf

install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/SigningTable

install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/KeyTable

install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/TrustedHosts

cp %{SOURCE6} ./README.fedora

rm -r %{buildroot}%{_prefix}/share/doc/%{name}
rm %{buildroot}%{_libdir}/*.a
rm %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
mkdir -p %{buildroot}%{_rundir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir %{buildroot}%{_sysconfdir}/%{name}/keys

install -Dm 0755 stats/%{name}-reportstats %{buildroot}%{_sbindir}/%{name}-reportstats
sed -i 's|^%{bigname}STATSDIR="/var/db/%{name}"|%{bigname}STATSDIR="%{_localstatedir}/spool/%{name}"|g' %{buildroot}%{_sbindir}/%{name}-reportstats
sed -i 's|^%{bigname}DATOWNER="mailnull:mailnull"|%{bigname}DATOWNER="%{name}:%{name}"|g' %{buildroot}%{_sbindir}/%{name}-reportstats

chmod 0644 contrib/convert/convert_keylist.sh

install -m0644 -D opendkim.sysusers.conf %{buildroot}%{_sysusersdir}/opendkim.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
# For the switchover from initscript to service file
%triggerun -- %{name} < 2.8.0-1
%systemd_post %{name}.service
%{_sbindir}/chkconfig --del %{name} >/dev/null 2>&1 || :
%systemd_postun_with_restart %{name}.service

%ldconfig_scriptlets -n libopendkim

%files
%license LICENSE LICENSE.Sendmail
%doc FEATURES KNOWNBUGS RELEASE_NOTES RELEASE_NOTES.Sendmail
%doc contrib/convert/convert_keylist.sh %{name}/*.sample
%doc %{name}/%{name}.conf.simple-verify %{name}/%{name}.conf.simple
%doc %{name}/README contrib/lua/*.lua
%doc README.fedora
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/SigningTable
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/KeyTable
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/TrustedHosts
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/miltertest
%{_sbindir}/opendkim
%{_sbindir}/opendkim-reportstats
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/miltertest.8.gz
%{_mandir}/man8/opendkim.8.gz
%dir %attr(-,%{name},%{name}) %{_localstatedir}/spool/%{name}
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%dir %attr(-,root,%{name}) %{_sysconfdir}/%{name}
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/keys
%attr(0755,root,root) %{_sbindir}/%{name}-default-keygen

%attr(0644,root,root) %{_unitdir}/%{name}.service
%{_sysusersdir}/opendkim.conf

%files -n libopendkim
%license LICENSE LICENSE.Sendmail
%doc README
%{_libdir}/lib%{name}.so.*

%files -n opendkim-tools
%license LICENSE LICENSE.Sendmail
%{_mandir}/man8/opendkim-genkey.8.gz
%{_mandir}/man8/opendkim-genzone.8.gz
%{_mandir}/man8/opendkim-testkey.8.gz
%{_mandir}/man8/opendkim-testmsg.8.gz
%{_sbindir}/opendkim-genkey
%{_sbindir}/opendkim-genzone
%{_sbindir}/opendkim-testkey
%{_sbindir}/opendkim-testmsg

%files -n libopendkim-devel
%license LICENSE LICENSE.Sendmail
%doc lib%{name}/docs/*.html
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
