%global source0_hash 924ad35113fd0a71c8e2dbe85b5d03445532e2b7b37a9f8a48983beea238b332
%ifarch %{ix86}
%bcond tests 0
%else
%bcond tests 0
%endif
Name:       pgbouncer
Version:    1.25.2
Release:        1%{?dist}
Summary:        Lightweight connection pooler for PostgreSQL
License:    ISC and BSD-2-Clause
URL:        https://www.pgbouncer.org
Source0:        https://www.%{name}.org/downloads/files/%{version}/%{name}-%{version}.tar.gz
Source3:    %{name}.logrotate
Source4:    %{name}.service
Source6:    %{name}.pam
Patch0:     %{name}-ini.patch
%if %{with tests}
%endif
Requires:   systemd
Requires:   logrotate
Requires:   python3-psycopg2
Requires:   c-ares >= 1.11
# oreon:deps
BuildRequires:  c-ares-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pandoc
BuildRequires:  pkgconfig(libevent)
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(psycopg)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  systemd-devel
# /oreon:deps
%description
pgbouncer is a lightweight connection pooler for PostgreSQL and uses libevent
for low-level socket handling.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i -e 's|/usr/bin/env python.*|%__python3|g' etc/mkauth.py

# Create a sysusers.d config file
cat >pgbouncer.sysusers.conf <<EOF
u pgbouncer - 'PgBouncer Server' - -
EOF

%build

%configure \
    --enable-debug \
    --with-cares \
    --with-ldap \
    --with-pam \
    --with-systemd
%make_build V=1
%install
%make_install
install -p -d %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 etc/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}
install -p -m 600 etc/userlist.txt %{buildroot}%{_sysconfdir}/%{name}
install -p -m 700 etc/mkauth.py %{buildroot}%{_sysconfdir}/%{name}/
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/%{name}
mkdir -p %{buildroot}%{_rundir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %{_rundir}/%{name} 0755 %{name} %{name} -
EOF
install -p -d %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
rm -fr %{buildroot}%{_docdir}/%{name}
install -m0644 -D pgbouncer.sysusers.conf %{buildroot}%{_sysusersdir}/pgbouncer.conf
%oreon_autofiles main
%if %{with tests}
%check

pytest
%endif
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
