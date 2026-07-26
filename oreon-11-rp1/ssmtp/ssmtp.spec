%global source0_hash 22c37dc90c871e8e052b2cab0ad219d010fa938608cd66b21c8f3c759046fa36

Name:		ssmtp
Version:	2.64
Release:	41%{?dist}
Summary:	Extremely simple MTA to get mail off the system to a Mailhub
License:	GPL-2.0-or-later
URL:		http://packages.debian.org/stable/mail/ssmtp
Source0:	ftp://ftp.debian.org/debian/pool/main/s/%{name}/%{name}_%{version}.orig.tar.bz2
Source1:	mailq.8
Source2:	newaliases.8
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=340803
# replaces RSA's md5 with a GPL compatible implementation
Patch1:		%{name}-md5auth-non-rsa.patch

#bug fixing patches
Patch2:		%{name}-garbage_writes.patch
Patch8:		%{name}-authpass.patch

#enhancements
#enhancement not present in Debian
Patch10:	%{name}-aliases.patch
# add X-Originating-IP field
#http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=557741
Patch11:	%{name}-remote-addr.patch
Patch12:	%{name}-validate-TLS-server-cert.patch

#fixes for Fedora PATHs
Patch21:	%{name}-defaultvalues.patch

Patch22:	ssmtp-configure-c99.patch
Patch23: ssmtp-c99.patch
Patch24:	ssmtp-c23.patch

#hack around wrong requires for mutt and mdadm
%if 0%{?rhel}
Provides:	MTA smtpdaemon
%endif
%if 0%{?fedora} < 8
Provides:	MTA smtpdaemon
%endif
Requires(post):	%{_sbindir}/alternatives
Requires(preun):	%{_sbindir}/alternatives
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	openssl-devel

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/sendmail
%endif

%description
A secure, effective and simple way of getting mail off a system to your mail
hub. It contains no suid-binaries or other dangerous things - no mail spool
to poke around in, and no daemons running in the background. Mail is simply
forwarded to the configured mailhost. Extremely easy configuration.

WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .gplmd5
%patch -P2 -p1 -b .garbage
%patch -P8 -p1 -b .authpass
%patch -P10 -p1 -b .aliases
%patch -P11 -p1 -b .remote-ip
%patch -P12 -p1 -b .tls

%patch -P21 -p1 -b .saneconf

%patch -P22 -p1 -b .configure-c99
%patch -P 23 -p1
%patch -P24 -p1 -b .c23

%build
%configure --enable-ssl --enable-md5auth --enable-inet6
make %{?_smp_mflags}

%install 
rm -rf %{buildroot}
install -p -D -m 2750 %{name} %{buildroot}%{_sbindir}/%{name}
#install -p -D -m 755 generate_config_alt %{buildroot}%{_bindir}/generate_config_alt
mkdir -p %{buildroot}%{_bindir}/
install -p -D -m 644 revaliases %{buildroot}%{_sysconfdir}/ssmtp/revaliases
install -p -m 640 ssmtp.conf %{buildroot}%{_sysconfdir}/ssmtp/ssmtp.conf
install -p -D -m 644 ssmtp.8 %{buildroot}%{_mandir}/man8/ssmtp.8
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man8/mailq.ssmtp.8
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/newaliases.ssmtp.8
install -p -D -m 644 ssmtp.conf.5 %{buildroot}%{_mandir}/man5/ssmtp.conf.5
ln -s --relative %{_sbindir}/%{name} %{buildroot}%{_sbindir}/sendmail.ssmtp
ln -s --relative %{_sbindir}/%{name} %{buildroot}%{_bindir}/newaliases.ssmtp
ln -s --relative %{_sbindir}/%{name} %{buildroot}%{_bindir}/mailq.ssmtp
touch %{buildroot}%{_sbindir}/sendmail
touch %{buildroot}%{_bindir}/mailq
touch %{buildroot}%{_bindir}/newaliases
touch %{buildroot}%{_mandir}/man8/mailq.8.gz
touch %{buildroot}%{_mandir}/man8/newaliases.8.gz
touch %{buildroot}%{_mandir}/man8/sendmail.8.gz

%post
%{_sbindir}/alternatives  --install %{_sbindir}/sendmail mta %{_sbindir}/sendmail.ssmtp 30 \
	--slave %{_bindir}/mailq mta-mailq %{_bindir}/mailq.ssmtp \
	--slave %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.ssmtp \
	--slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man8/mailq.ssmtp.8.gz \
	--slave %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man8/newaliases.ssmtp.8.gz \
	--slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man8/ssmtp.8.gz 

%preun
#only remove in case of erase (but not at upgrade)
if [ $1 -eq 0 ] ; then
	%{_sbindir}/alternatives --remove mta %{_sbindir}/sendmail.ssmtp
fi
exit 0

%postun
if [ "$1" -ge "1" ]; then
	if [ "`readlink %{_sysconfdir}/alternatives/mta`" == "%{_sbindir}/sendmail.ssmtp" ]; then
		%{_sbindir}/alternatives --set mta %{_sbindir}/sendmail.ssmtp
	fi
fi

%files
%doc COPYING INSTALL README TLS CHANGELOG_OLD ChangeLog COPYRIGHT 
%{_mandir}/man5/*
%{_mandir}/man8/*
%attr(2755, root, mail) %{_sbindir}/%{name}

%ghost %{_sbindir}/sendmail
%ghost %{_bindir}/mailq
%ghost %{_bindir}/newaliases
%ghost %{_mandir}/man8/mailq.8.gz 
%ghost %{_mandir}/man8/newaliases.8.gz
%ghost %{_mandir}/man8/sendmail.8.gz

%{_sbindir}/sendmail.ssmtp
%{_bindir}/newaliases.ssmtp
%{_bindir}/mailq.ssmtp
%attr(2750, root, mail) %dir %{_sysconfdir}/ssmtp/
%config(noreplace) %{_sysconfdir}/ssmtp/revaliases
%attr(640, root, mail) %config(noreplace) %{_sysconfdir}/ssmtp/ssmtp.conf

%changelog
%autochangelog
