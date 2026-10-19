%global source10_hash 187de8fe1f246b997f55b88d9a9e402ced8ca1b73aaf3c91b74801f03764d952
%global source0_hash 030417d302a7eadf1963a2b8b5f8e56870704b4327f780bed1dff41c0dc95bdc
%global use_sysusers 1
Name:		milter-regex
Version:	2.7
Release:        1%{?dist}
Summary:        Milter plug-in for regular expression filtering
License:	BSD-2-Clause
URL:		http://www.benzedrine.ch/milter-regex.html
Source0:        http://www.benzedrine.ch/milter-regex-%{version}.tar.gz
Source10:	http://www.benzedrine.ch/milter-regex-%{version}.tar.gz.asc
Source1:	milter-regex.service
Source2:	milter-regex-options
Source3:	milter-regex.conf
%if !%{use_sysusers}
Requires(pre):	shadow-utils
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  byacc
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  groff
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  sendmail-milter-devel
BuildRequires:  systemd
# /oreon:deps
%description
Milter-regex is a milter based filter that makes it possible to filter
emails using regular expressions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Customize config file location and dæmon user
sed -i -e	's|/etc/milter-regex\.conf|%{_sysconfdir}/mail/milter-regex.conf|;
		 s|_milter-regex|mregex|' milter-regex.[8c]

# Copy out the license text from the source code
head -n +31 milter-regex.c > LICENSE

# Create a sysusers.d config file
cat >milter-regex.sysusers.conf <<EOF
u mregex - 'Regex Milter' %{_localstatedir}/spool/milter-regex -
EOF

%build

make %{?_smp_mflags} -f Makefile.linux \
	CFLAGS="%{optflags} -Wextra -Wwrite-strings -DYYMAXDEPTH=8192 -DSM_CONF_STDBOOL_H=1" \
	LDFLAGS="-Wl,-z,now -Wl,-z,relro %{?__global_ldflags} -Wl,--as-needed -L/usr/lib/libmilter -lmilter -lpthread"
%install
mkdir -p \
	%{buildroot}%{_unitdir} \
	%{buildroot}%{_localstatedir}/spool/milter-regex \
	%{buildroot}%{_mandir}/man8 \
	%{buildroot}%{_sbindir} \
	%{buildroot}%{_sysconfdir}/{mail,sysconfig}
install -p -m 755 milter-regex %{buildroot}%{_sbindir}/
install -p -m 644 milter-regex.8 %{buildroot}%{_mandir}/man8/
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/milter-regex.service
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/milter-regex
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mail/milter-regex.conf
install -m0644 -D milter-regex.sysusers.conf %{buildroot}%{_sysusersdir}/milter-regex.conf
: > %{buildroot}%{_localstatedir}/spool/milter-regex/sock
%oreon_autofiles main
%if !%{use_sysusers}
%pre

getent group mregex >/dev/null || groupadd -r mregex
getent passwd mregex >/dev/null || \
	useradd -r -g mregex -d %{_localstatedir}/spool/milter-regex \
		-s /sbin/nologin -c "Regex Milter" mregex
exit 0
%endif
%post

%systemd_post milter-regex.service
%preun

%systemd_preun milter-regex.service
%postun

%systemd_postun_with_restart milter-regex.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
