%global source0_hash f1be35bfccc2ba1c9f75f76d222b29b57024efe89c5b564b86c1a37ce2d1ddb1

Summary:          Latency Logging and Graphing System
Name:             smokeping
Version:          2.9.0
Release:          15%{?dist}
License:          GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
URL:              https://oss.oetiker.ch/smokeping/
Source0:          https://oss.oetiker.ch/smokeping/pub/smokeping-%{version}.tar.gz
Source1:          smokeping.service
Source2:          smokeping-httpd.conf.d
Source3:          http://oss.oetiker.ch/smokeping-demo/img/smokeping.png
Source4:          http://oss.oetiker.ch/smokeping-demo/img/rrdtool.png
Source5:          smokeping-tmpfs.conf
Source6:          smokeping-fix-ownership
Source7:          README.fedora
Source8:          smokeping.sysusers.conf
Patch0:           smokeping-2.9.0-paths.patch
Patch1:           smokeping-2.9.0-config.patch
Patch2:           smokeping-2.6.7-silence.patch
Patch3:           smokeping-2.8.2-no-3rd-party.patch
Patch4:           smokeping-2.8.2-remove-date.patch
BuildRequires:    /usr/bin/pod2man
BuildRequires:    automake
BuildRequires:    coreutils
BuildRequires:    glibc-common
BuildRequires:    make
BuildRequires:    perl(Authen::Radius)
BuildRequires:    perl(CGI)
BuildRequires:    perl(CGI::Fast)
BuildRequires:    perl(Config::Grammar)
BuildRequires:    perl(Data::Dumper)
BuildRequires:    perl(Digest::HMAC_MD5)
BuildRequires:    perl(Digest::MD5)
BuildRequires:    perl(ExtUtils::MakeMaker)
BuildRequires:    perl(ExtUtils::Manifest)
BuildRequires:    perl(FCGI)
BuildRequires:    perl(File::Basename)
BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(IO::Pty)
BuildRequires:    perl(IO::Socket::SSL)
BuildRequires:    perl(LWP)
BuildRequires:    perl(LWP::UserAgent)
BuildRequires:    perl(Net::DNS)
BuildRequires:    perl(Net::LDAP)
BuildRequires:    perl(Net::OpenSSH)
BuildRequires:    perl(Net::SNMP)
BuildRequires:    perl(Net::Telnet)
BuildRequires:    perl(POSIX)
BuildRequires:    perl(Pod::Usage)
BuildRequires:    perl(RRDs)
BuildRequires:    perl(SNMP_Session)
BuildRequires:    perl(SNMP_util) >= 1.13
BuildRequires:    perl(Safe)
BuildRequires:    perl(Socket6)
BuildRequires:    perl(Storable)
BuildRequires:    perl(Sys::Hostname)
BuildRequires:    perl(Sys::Syslog)
BuildRequires:    perl(Time::HiRes)
BuildRequires:    perl(URI::Escape)
BuildRequires:    perl(strict)
BuildRequires:    perl(vars)
BuildRequires:    perl(warnings)
BuildRequires:    perl-generators
BuildRequires:    systemd-units
BuildRequires:    autoconf%{?rhel:2.7x}
Requires:         findutils
Requires:         fping >= 2.4b2
# only httpd supported without config changes
Requires:         httpd
Requires:         mod_fcgid
# not picked up for some reason
Requires:         perl(Config::Grammar)
Requires:         perl(SNMP_util) >= 1.13
Requires:         perl-interpreter >= 5.6.1
Requires:         rrdtool >= 1.0.33
Requires:         traceroute
Requires(pre):    httpd
%if 0%{?rhel} || 0%{?fedora} < 43
Requires(pre):    shadow-utils
%endif
BuildArch:        noarch
%global __provides_exclude_from %{_datadir}/%{name}/
%global __requires_exclude ^perl\\((Authen::.*|Net::OpenSSH|Smokeping)
%{?perl_default_filter}

%description
SmokePing is a latency logging and graphing system. It consists of a
daemon process which organizes the latency measurements and a CGI
which presents the graphs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
install -p -m 0644 %{SOURCE7} .
iconv -f ISO-8859-1 -t utf-8 -o CHANGES.utf8 CHANGES
touch -r CHANGES CHANGES.utf8 
mv CHANGES.utf8 CHANGES

# remove some external modules
rm -f lib/{SNMP_Session,SNMP_util,BER}.pm
rm -rf thirdparty/
[ -e VERSION ] || echo %{version} > VERSION

%build
autoreconf%{?rhel:27} --force --install --verbose --make

%configure --with-htdocs-dir=%{_datadir}/smokeping/htdocs \
    --disable-silent-rules

%install
%make_install

# Some additional dirs and files
install -d %{buildroot}%{_localstatedir}/lib/smokeping/{rrd,images} \
    %{buildroot}/run/smokeping %{buildroot}%{_datadir}/smokeping/cgi
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/smokeping.service
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/smokeping.conf
install  -p -m 0644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/smokeping/htdocs
install -Dp -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/smokeping.conf
install -Dp -m 0755 %{SOURCE6} %{buildroot}%{_libexecdir}/smokeping-fix-ownership

# Fix some files
for f in config basepage.html smokemail tmail smokeping_secrets ; do
    mv %{buildroot}%{_sysconfdir}/smokeping/$f.dist \
       %{buildroot}%{_sysconfdir}/smokeping/$f
done
mv %{buildroot}%{_sysconfdir}/smokeping/examples __examples
mv %{buildroot}%{_bindir}/smokeping_cgi %{buildroot}%{_datadir}/smokeping/cgi
ln -s smokeping_cgi %{buildroot}%{_datadir}/smokeping/cgi/smokeping.fcgi
rm -f %{buildroot}%{_datadir}/smokeping/htdocs/smokeping.fcgi.dist

%if 0%{?fedora} > 42
install -m0644 -D %{SOURCE8} %{buildroot}%{_sysusersdir}/smokeping.conf
%endif

%if 0%{?rhel} || 0%{?fedora} < 43
%pre
getent passwd smokeping >/dev/null || \
    useradd -r -g apache -d /var/lib/smokeping -s /sbin/nologin \
    -c "Smokeping" smokeping
exit 0
%endif

%post
%systemd_post smokeping.service

%preun
%systemd_preun smokeping.service

%postun
%systemd_postun_with_restart smokeping.service

%files
%license COPYRIGHT LICENSE
%doc CHANGES CONTRIBUTORS README.md TODO README.fedora
%doc __examples/*
%{_sbindir}/smokeping
%{_bindir}/smokeinfo
%{_bindir}/tSmoke
%{_libexecdir}/smokeping-fix-ownership
%{_unitdir}/smokeping.service
%dir %{_sysconfdir}/smokeping
%attr(0640, root, apache) %config(noreplace) %{_sysconfdir}/smokeping/config
%config(noreplace) %{_sysconfdir}/smokeping/basepage.html
%config(noreplace) %{_sysconfdir}/smokeping/smokemail
%attr(0640, root, root) %config(noreplace) %{_sysconfdir}/smokeping/smokeping_secrets
%config(noreplace) %{_sysconfdir}/smokeping/tmail
%config(noreplace) %{_sysconfdir}/httpd/conf.d/smokeping.conf
%{_tmpfilesdir}/smokeping.conf
%if 0%{?fedora} > 42
%{_sysusersdir}/smokeping.conf
%endif
%{_datadir}/smokeping
%dir %{_localstatedir}/lib/smokeping
%attr(0755, smokeping, apache) %{_localstatedir}/lib/smokeping/rrd
%attr(0755, smokeping, apache) /run/smokeping
%attr(0755, apache, apache) %{_localstatedir}/lib/smokeping/images
%{_mandir}/man1/smokeping*.1*
%{_mandir}/man1/smokeinfo*.1*
%{_mandir}/man1/tSmoke.1*
%{_mandir}/man3/Smokeping_*.3*
%{_mandir}/man5/smokeping_*.5*
%{_mandir}/man7/smokeping_*.7*

%changelog
%autochangelog
