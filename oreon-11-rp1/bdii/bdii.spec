%global source0_hash 9e32ae581b13572950a340bab2dd71ab6a8401e4a5621f36a0679ce921efd7e7

%if %{?fedora}%{!?fedora:0} >= 25 || %{?rhel}%{!?rhel:0} >= 8
%global use_systemd 1
%else
%global use_systemd 0
%endif

%if %{?fedora}%{!?fedora:0} >= 36 || %{?rhel}%{!?rhel:0} >= 9
%global use_mdb 1
%else
%global use_mdb 0
%endif

Name:		bdii
Version:	6.0.3
Release:	7%{?dist}
Summary:	The Berkeley Database Information Index (BDII)

License:	Apache-2.0
URL:		https://github.com/EGI-Federation/bdii
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python3-devel
%if %{use_systemd}
BuildRequires:	systemd-rpm-macros
%endif

Requires:	openldap-clients
Requires:	openldap-servers
Requires:	glue-schema >= 2.0.10
Requires:	logrotate

Requires(post):		/usr/bin/mkpasswd
%if %{use_systemd}
%{?systemd_requires}
%else
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif

%if %{?fedora}%{!?fedora:0} >= 23 || %{?rhel}%{!?rhel:0} >= 8
Requires(post):		policycoreutils-python-utils
Requires(postun):	policycoreutils-python-utils
%else
Requires(post):		policycoreutils-python
Requires(postun):	policycoreutils-python
%endif

%description
The Berkeley Database Information Index (BDII) consists of a standard
LDAP database which is updated by an external process. The update process
obtains LDIF from a number of sources and merges them. It then compares
this to the contents of the database and creates an LDIF file of the
differences. This is then used to update the database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%if %{use_mdb}
# Use mdb on recent systems
patch -p1 -f < 0001-Use-mdb-slapd-backend.patch
%endif

%build

%install
make install prefix=%{buildroot}

# Work around hardcoded /usr/sbin in the Makefile
if [ %{_sbindir} != %{_prefix}/sbin ] ; then
   mv %{buildroot}%{_prefix}/sbin %{buildroot}%{_sbindir}
fi

# Don't use /usr/bin/env shebang
sed 's!%{_bindir}/env .*!%{__python3}!' -i %{buildroot}%{_sbindir}/bdii-update

%if %{use_systemd}
rm %{buildroot}%{_initrddir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p etc/systemd/bdii.service etc/systemd/bdii-slapd.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p etc/systemd/bdii-slapd-start %{buildroot}%{_datadir}/%{name}
%endif

rm -rf %{buildroot}%{_docdir}/%{name}

%if %{use_systemd}
%pre
# Remove old init config when systemd is used
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
%endif

%post
sed "s/\(rootpw *\)secret/\1$(mkpasswd -s 0 | tr '/' 'x')/" \
    -i %{_sysconfdir}/%{name}/bdii-slapd.conf \
       %{_sysconfdir}/%{name}/bdii-top-slapd.conf

%if %{use_systemd}
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

semanage port -a -t ldap_port_t -p tcp 2170 2>/dev/null || :
semanage fcontext -a -t slapd_db_t "%{_localstatedir}/lib/%{name}/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "%{_localstatedir}/run/%{name}/db(/.*)?" 2>/dev/null || :
# Remove selinux labels for old bdii var dir
semanage fcontext -d -t slapd_db_t "%{_localstatedir}/run/%{name}(/.*)?" 2>/dev/null || :

%preun
%if %{use_systemd}
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
  service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if %{use_systemd}
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ge 1 ]; then
  service %{name} condrestart > /dev/null 2>&1
fi
%endif

if [ $1 -eq 0 ]; then
  semanage port -d -t ldap_port_t -p tcp 2170 2>/dev/null || :
  semanage fcontext -d -t slapd_db_t "%{_localstatedir}/lib/%{name}/db(/.*)?" 2>/dev/null || :
  semanage fcontext -d -t slapd_var_run_t "%{_localstatedir}/run/%{name}/db(/.*)?" 2>/dev/null || :
fi

%files
%attr(-,ldap,ldap) %{_localstatedir}/lib/%{name}
%attr(-,ldap,ldap) %{_localstatedir}/log/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/DB_CONFIG
%config(noreplace) %{_sysconfdir}/%{name}/DB_CONFIG_top
%config(noreplace) %{_sysconfdir}/%{name}/bdii.conf
%config(noreplace) %{_sysconfdir}/%{name}/BDII.schema
%attr(-,ldap,ldap) %config %{_sysconfdir}/%{name}/bdii-slapd.conf
%attr(-,ldap,ldap) %config %{_sysconfdir}/%{name}/bdii-top-slapd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if %{use_systemd}
%{_unitdir}/bdii.service
%{_unitdir}/bdii-slapd.service
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bdii-slapd-start
%else
%{_initrddir}/%{name}
%endif
%{_sbindir}/bdii-update
%{_mandir}/man1/bdii-update.1*
%doc AUTHORS.md README.md
%license COPYRIGHT LICENSE.txt

%changelog
%autochangelog
