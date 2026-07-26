%global source0_hash 030417d302a7eadf1963a2b8b5f8e56870704b4327f780bed1dff41c0dc95bdc

# Use sysusers from Fedora 43 onwards
%if (0%{?rhel} && 0%{?rhel} <= 10) || (0%{?fedora} && 0%{?fedora} <= 42)
%global use_sysusers 0
%else
%global use_sysusers 1
%endif

Name:		milter-regex
Version:	2.7
Release:	20%{?dist}
Summary:	Milter plug-in for regular expression filtering
License:	BSD-2-Clause
URL:		http://www.benzedrine.ch/milter-regex.html
Source0:	http://www.benzedrine.ch/milter-regex-%{version}.tar.gz
# Note: signature made with ancient PGP key, needs gpg1 to verify
Source10:	http://www.benzedrine.ch/milter-regex-%{version}.tar.gz.asc
Source1:	milter-regex.service
Source2:	milter-regex-options
Source3:	milter-regex.conf
BuildRequires:	byacc
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	groff
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	sendmail-milter-devel >= 8.13
BuildRequires:	systemd
%if !%{use_sysusers}
Requires(pre):	shadow-utils
%endif
%{?systemd_requires}

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

%if %{use_sysusers}
install -m0644 -D milter-regex.sysusers.conf %{buildroot}%{_sysusersdir}/milter-regex.conf
%endif

# Create a ghost sock file so we can remove it on package deletion
: > %{buildroot}%{_localstatedir}/spool/milter-regex/sock

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

%files
%license LICENSE
%{_sbindir}/milter-regex
%{_unitdir}/milter-regex.service
%config(noreplace) %{_sysconfdir}/sysconfig/milter-regex
%config(noreplace) %{_sysconfdir}/mail/milter-regex.conf
%dir %attr(755,root,mregex) %{_localstatedir}/spool/milter-regex/
%ghost %{_localstatedir}/spool/milter-regex/sock
%{_mandir}/man8/milter-regex.8*
%if %{use_sysusers}
%{_sysusersdir}/milter-regex.conf
%endif

%changelog
%autochangelog
