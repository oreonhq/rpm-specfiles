%global source0_hash c22d45bd4105b344351cbbfd6da99755182f64120747d18e91b6267a73775099
%global _hardened_build 1
%bcond_without pam
%bcond_without sqlite
%bcond_without db
%bcond_without ldap
%bcond_without mysql
%bcond_without postgresql
%bcond_without systemd
Summary:        OpenSource server implementation of the Jabber protocols
Name:           jabberd
Version:        2.6.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
Source0:        https://github.com/jabberd2/jabberd2/releases/download/jabberd-%{version}/jabberd-%{version}.tar.xz
Source1:        README.fedora
Source2:        jabberd.init
Source3:        jabberd.sysconfig
Patch0:         jabberd-fedora-crypto-policy.patch
Patch1:         jabberd-fix-paths.patch
Patch2:         unbreak-autoreconf.patch
Patch3:         0001-configure.ac-adapt-to-openssl-1.1.patch
Patch4:         0002-authreg_ldapfull-adapt-to-openssl-1.1.patch
Patch5:         0003-sx-ssl.c-adapt-to-openssl-1.1.patch
Patch6:         0001-Fix-build-errors-with-MariaDB-10.2.patch
Patch7:         181e736dcbb19c828266d88837f4343510b4d20e.patch
Patch8:         jabberd-c99.patch
URL:            http://jabberd2.org/
%if %{with systemd}
Requires(post):         systemd-units systemd-sysv
Requires(preun):        systemd-units
Requires(postun):       systemd-units
%else
Requires(post):         openssl chkconfig /sbin/service
Requires(preun):        chkconfig shadow-utils /sbin/service
Requires(postun):       chkconfig /sbin/service
%endif
%if %{with pam}
%endif
%if %{with sqlite}
%endif
%if %{with db}
%endif
%if %{with ldap}
%endif
%if %{with mysql}
%endif
%if %{with postgresql}
%endif
Requires(post):         openssl
Requires(preun):        shadow-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  cppunit-devel
BuildRequires:  db4-devel
BuildRequires:  expat-devel
BuildRequires:  http-parser-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl-generators
BuildRequires:  sqlite-devel
BuildRequires:  systemd-units
BuildRequires:  udns-devel
# /oreon:deps
%description
The jabberd project aims to provide an open-source server implementation of
the Jabber protocols for instant messaging and XML routing. The goal of this
project is to provide a scalable, reliable, efficient and extensible server
that provides a complete set of features and is up to date with the latest
protocol revisions.

jabberd2 is the next generation of the jabberd server. It has been
rewritten from the ground up to be scalable, architecturally sound, and to
support the latest protocol extensions coming out of the JSF.

This package defaults to use pam and sqlite.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# "Utilize system-wide crypto-policies" is only for F21+ (#1179229)
# therefore the patch is not applied on non Fedora builds
%patch -P1 -p1
%patch -P6 -p1

# Create a sysusers.d config file
cat >jabberd.sysusers.conf <<EOF
u jabber - 'Jabber Server' %{_var}/lib/%{name} -
EOF

%build

export CFLAGS="%{optflags}"
%configure \
        --sysconfdir=%{_sysconfdir}/%{name} \
        --localstatedir=%{_var}/lib \
%if %{with pam}
        --enable-pam \
%else
        --disable-pam \
%endif
%if %{with db}
        --enable-db \
%else
        --disable-db \
%endif
%if %{with mysql}
        --enable-mysql \
        --with-extra-library-path=%{_libdir}/mysql \
%else
        --disable-mysql \
%endif
%if %{with ldap}
        --enable-ldap \
%else
        --disable-ldap \
%endif
%if %{with postgresql}
        --enable-pgsql \
%else
        --disable-pgsql \
%endif
%if %{with sqlite}
        --enable-sqlite \
%else
        --disable-sqlite \
%endif
        --enable-fs --enable-anon --enable-pipe --enable-ssl \
        --enable-websocket \
        --enable-debug
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
sed -i "s|/usr/pkg/bin/perl|/usr/bin/env perl|" tools/*.pl
install -dpm 700 $RPM_BUILD_ROOT/%{_var}/lib/%{name}/{log,pid,db}
install -dpm 755 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/
install -Dpm 644 tools/pam_jabberd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/%{name}
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/
for i in `ls tools`; do
    if [ $i == "Makefile" -o $i == "Makefile.am" -o $i == "Makefile.in" \
        -o $i == "jabberd.in" -o $i == "jabberd.rc" -o $i == "pam_jabberd" ]; then
        continue;
    fi
    sed -i "s|\r||g" tools/$i
    install -pm 755 tools/$i $RPM_BUILD_ROOT%{_datadir}/%{name}/
done
install -dpm 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
%if ! %{with systemd}
rm -frv $RPM_BUILD_ROOT%{_prefix}/lib/systemd
install -Dpm 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
sed -i -e "s,__BINDIR__,%{_bindir},g" \
       -e "s,__ETCDIR__,%{_sysconfdir}/%{name}/,g" \
       -e "s,__PIDDIR__,%{_var}/lib/%{name}/pid,g" \
       -e "s,__SYSCONF__,%{_sysconfdir}/sysconfig,g" \
          $RPM_BUILD_ROOT%{_initrddir}/%{name} \
          $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
%endif
find $RPM_BUILD_ROOT -name "*.la" -delete
rm -f $RPM_BUILD_ROOT/etc/jabberd/*.conf
rm -f $RPM_BUILD_ROOT/usr/etc/init/*.conf
sed -i -e ':a;N;$!ba' \
            -e 's,<module>mysql</module>,<module>pam</module>,g' \
            -e "s,register-enable='true'>,realm='' require-starttls='true' pemfile='/etc/%{name}/server.pem'>,g" \
                $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/c2s.xml
touch $RPM_BUILD_ROOT%{_sysconfdir}/jabberd/server.pem
rm -f $RPM_BUILD_ROOT%{_bindir}/jabberd
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/jabberd.cfg*
cp %{SOURCE1} .
install -m0644 -D jabberd.sysusers.conf %{buildroot}%{_sysusersdir}/jabberd.conf
%oreon_autofiles main

%post

%if %{with systemd}
%systemd_post %{name}.service
if [ $1 -eq 1 ] ; then
        export NEWPASS=$( dd if=/dev/urandom bs=20 count=1 2>/dev/null \
                                | sha1sum | awk '{print $1}' )
        cd %{_sysconfdir}/%{name}
        %{__sed} -i -f- router-users.xml router.xml <<END
s,<secret>secret</secret>,<secret>$NEWPASS</secret>,g
END
        %{__sed} -i -f- *.xml <<END
s,<pass>secret</pass>,<pass>$NEWPASS</pass>,g
END
fi
cd %{_sysconfdir}/%{name}
if [ ! -s server.pem ]; then
 if [ -e %{_bindir}/make-dummy-cert ]; then
  %{___build_shell} %{_bindir}/make-dummy-cert
 else
  %{___build_shell} %{_sysconfdir}/pki/tls/certs/make-dummy-cert server.pem
 fi
 chown root.jabber server.pem
 chmod 640 server.pem
fi
%else
if [ "$1" -eq "1" ]; then
        /sbin/chkconfig --add %{name}
        export NEWPASS=$( dd if=/dev/urandom bs=20 count=1 2>/dev/null \
                                | sha1sum | awk '{print $1}' )
        cd %{_sysconfdir}/%{name}
        %{__sed} -i -f- router-users.xml router.xml <<END
s,<secret>secret</secret>,<secret>$NEWPASS</secret>,g
END
        %{__sed} -i -f- *.xml <<END
s,<pass>secret</pass>,<pass>$NEWPASS</pass>,g
END
fi
cd %{_sysconfdir}/%{name}
if [ ! -s server.pem ]; then
 %{___build_shell} %{_sysconfdir}/pki/tls/certs/make-dummy-cert server.pem
 chown root.jabber server.pem
 chmod 640 server.pem
fi
%endif
%preun

%if %{with systemd}
%systemd_preun %{name}.service
%else
if [ "$1" -eq "0" ]; then
        /sbin/service %{name} stop > /dev/null 2>&1
        /sbin/chkconfig --del %{name}
fi
%endif
%postun

%if %{with systemd}
%systemd_postun_with_restart %{name}.service
%triggerun -- jabberd < 2.2.14-3

/usr/bin/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:
/bin/systemctl --no-reload enable %{name}.service >/dev/null 2>&1 ||:
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
%else
if [ "$1" -eq "1" ]; then
        /sbin/service %{name} condrestart > /dev/null 2>&1
fi
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
