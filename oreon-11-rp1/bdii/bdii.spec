%global source0_hash 9e32ae581b13572950a340bab2dd71ab6a8401e4a5621f36a0679ce921efd7e7
%global use_systemd 0
%global use_mdb 0
Name:		bdii
Version:	6.0.3
Release:        7%{?dist}
Summary:        The Berkeley Database Information Index (BDII)
License:	Apache-2.0
URL:		https://github.com/EGI-Federation/bdii
Source0:        https://github.com/EGI-Federation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	openldap-clients
Requires:	openldap-servers
Requires:	glue-schema >= 2.0.10
Requires:	logrotate
Requires(post):		/usr/bin/mkpasswd
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts
Requires(post):		policycoreutils-python
Requires(postun):	policycoreutils-python
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The Berkeley Database Information Index (BDII) consists of a standard
LDAP database which is updated by an external process. The update process
obtains LDIF from a number of sources and merges them. It then compares
this to the contents of the database and creates an LDIF file of the
differences. This is then used to update the database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
make install prefix=%{buildroot}
if [ %{_sbindir} != %{_prefix}/sbin ] ; then
   mv %{buildroot}%{_prefix}/sbin %{buildroot}%{_sbindir}
fi
sed 's!%{_bindir}/env .*!%{__python3}!' -i %{buildroot}%{_sbindir}/bdii-update
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main

%post

sed "s/\(rootpw *\)secret/\1$(mkpasswd -s 0 | tr '/' 'x')/" \
    -i %{_sysconfdir}/%{name}/bdii-slapd.conf \
       %{_sysconfdir}/%{name}/bdii-top-slapd.conf
/sbin/chkconfig --add %{name}
semanage port -a -t ldap_port_t -p tcp 2170 2>/dev/null || :
semanage fcontext -a -t slapd_db_t "%{_localstatedir}/lib/%{name}/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "%{_localstatedir}/run/%{name}/db(/.*)?" 2>/dev/null || :
semanage fcontext -d -t slapd_db_t "%{_localstatedir}/run/%{name}(/.*)?" 2>/dev/null || :
%preun

if [ $1 -eq 0 ]; then
  service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi
%postun

if [ $1 -ge 1 ]; then
  service %{name} condrestart > /dev/null 2>&1
fi
if [ $1 -eq 0 ]; then
  semanage port -d -t ldap_port_t -p tcp 2170 2>/dev/null || :
  semanage fcontext -d -t slapd_db_t "%{_localstatedir}/lib/%{name}/db(/.*)?" 2>/dev/null || :
  semanage fcontext -d -t slapd_var_run_t "%{_localstatedir}/run/%{name}/db(/.*)?" 2>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
