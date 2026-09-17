%global source0_hash 4034de2e92c61fa83eedadb1d8d8bdfe65e57eb50ce9679e0140950e34ca4ab7

# PAM support
%global _with_pam	1

# Berkeley DB support
%global _with_bdb	1

Summary:	Free implementation of the server-side SMTP protocol as defined by RFC 5321
Name:		opensmtpd
Version:	7.8.0p0
Release:	2%{?dist}

License:	ISC
URL:		http://www.opensmtpd.org/
Provides:	MTA smtpd smtpdaemon server(smtp)

Source0:	http://www.opensmtpd.org/archives/%{name}-%{version}.tar.gz
Source1:	opensmtpd.service
Source2:	opensmtpd.pam

%if 0%{?_with_pam}
BuildRequires:	pam-devel
%endif
%if 0%{?_with_bdb}
BuildRequires:	libdb-devel
%endif

BuildRequires:	openssl-devel
BuildRequires:	libevent-devel
BuildRequires:  libxcrypt-devel
BuildRequires:	zlib-devel
BuildRequires:	coreutils
BuildRequires:	bison
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libtool

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/sendmail
%endif

%description
OpenSMTPD is a FREE implementation of the server-side SMTP protocol as defined
by RFC 5321, with some additional standard extensions. It allows ordinary
machines to exchange e-mails with other systems speaking the SMTP protocol.
Started out of dissatisfaction with other implementations, OpenSMTPD nowadays
is a fairly complete SMTP implementation. OpenSMTPD is primarily developed
by Gilles Chehade, Eric Faurot and Charles Longeau; with contributions from
various OpenBSD hackers. OpenSMTPD is part of the OpenBSD Project.
The software is freely usable and re-usable by everyone under an ISC license.

This package uses standard "alternatives" mechanism, you may call
"alternatives --set mta %{_sbindir}/sendmail.opensmtpd"
if you want to switch to OpenSMTPD MTA immediately after install, and
"alternatives --set mta %{_sbindir}/sendmail.sendmail" to revert
back to Sendmail as a default mail daemon.

The package default installation comes with a minimalistic configuration
that uses the "mbox" storage format and protects system directories.
If you require a custom or less restrictive service configuration,
do not modify the default systemd unit file. Instead, create an override
configuration at "/etc/systemd/system/opensmtpd.service".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Create a sysusers.d config file
cat >opensmtpd.sysusers.conf <<EOF
u smtpd - 'opensmtpd privsep user' %{_localstatedir}/empty/smtpd -
u smtpq - 'opensmtpd queue user' %{_localstatedir}/empty/smtpd -
EOF

%build
export CFLAGS="%{optflags}"

%configure \
    --sysconfdir=%{_sysconfdir}/opensmtpd \
    --with-path-CAfile=%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
    --with-mantype=man \
    %if 0%{?_with_pam}
    --with-auth-pam=smtp \
    %endif
    %if 0%{?_with_bdb}
    --with-table-db \
    %endif
    --with-user-smtpd=smtpd \
    --with-user-queue=smtpq \
    --with-group-queue=smtpq \
    --with-path-empty=%{_localstatedir}/empty/smtpd \
    --with-path-mbox=%{_localstatedir}/spool/mail \
    --with-path-socket=%{_rundir} \
    --with-path-pidfile=%{_rundir} \
    --without-rpath

%make_build

%install
%make_install
mkdir -p -m 0755 %{buildroot}/%{_localstatedir}/empty/smtpd

install -Dpm 0644 %SOURCE1 %{buildroot}/%{_unitdir}/opensmtpd.service

%if 0%{?_with_pam}
install -Dpm 0644 %SOURCE2 %{buildroot}/%{_sysconfdir}/pam.d/smtp.opensmtpd
touch %{buildroot}/%{_sysconfdir}/pam.d/smtp
%endif

rm -rf %{buildroot}/%{_bindir}/sendmail
rm -rf %{buildroot}/%{_sbindir}/mailq
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_sbindir}/sendmail.%{name}
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_bindir}/mailq.%{name}
touch %{buildroot}/%{_sbindir}/sendmail
touch %{buildroot}/usr/lib/sendmail
touch %{buildroot}/%{_bindir}/mailq

mv %{buildroot}/%{_mandir}/man1/smtp.1 %{buildroot}/%{_mandir}/man1/smtp.opensmtpd.1
mv %{buildroot}/%{_mandir}/man5/aliases.5 %{buildroot}/%{_mandir}/man5/aliases.opensmtpd.5
mv %{buildroot}/%{_mandir}/man8/sendmail.8 %{buildroot}/%{_mandir}/man8/sendmail.opensmtpd.8
mv %{buildroot}/%{_mandir}/man8/smtpd.8 %{buildroot}/%{_mandir}/man8/smtpd.opensmtpd.8
ln -s %{_mandir}/man1/smtp.opensmtpd.1.gz %{buildroot}/%{_mandir}/man8/smtp.opensmtpd.8
ln -s %{_mandir}/man8/smtpctl.8.gz %{buildroot}/%{_mandir}/man1/mailq.opensmtpd.1
touch %{buildroot}/%{_mandir}/man1/mailq.1
touch %{buildroot}/%{_mandir}/man5/aliases.5
touch %{buildroot}/%{_mandir}/man8/sendmail.8
touch %{buildroot}/%{_mandir}/man8/smtp.8
touch %{buildroot}/%{_mandir}/man8/smtpd.8

%if 0%{?_with_bdb}
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_sbindir}/makemap.%{name}
ln -s %{_sbindir}/smtpctl %{buildroot}/%{_bindir}/newaliases.%{name}
mv %{buildroot}/%{_mandir}/man8/makemap.8 %{buildroot}/%{_mandir}/man8/makemap.opensmtpd.8
mv %{buildroot}/%{_mandir}/man8/newaliases.8 %{buildroot}/%{_mandir}/man8/newaliases.opensmtpd.8
touch %{buildroot}/%{_sbindir}/makemap
touch %{buildroot}/%{_bindir}/newaliases
touch %{buildroot}/%{_mandir}/man1/newaliases.1
touch %{buildroot}/%{_mandir}/man8/makemap.8
%endif

# smtpd spool directory
for i in incoming offline purge queue; do
	mkdir -p %{buildroot}/%{_localstatedir}/spool/smtpd/$i
done

# fix aliases path in the config
sed -i -e 's|/etc/mail/aliases|/etc/aliases|g' %{buildroot}/%{_sysconfdir}/opensmtpd/smtpd.conf
ln -s %{_sysconfdir}/aliases %{buildroot}/%{_sysconfdir}/opensmtpd/aliases

# set mbox delivery method
sed -i -e 's|^action "local" maildir|action "local" mbox|g' %{buildroot}/%{_sysconfdir}/opensmtpd/smtpd.conf

install -m0644 -D opensmtpd.sysusers.conf %{buildroot}%{_sysusersdir}/opensmtpd.conf

%post
%systemd_post %{name}.service
alternatives --install %{_sbindir}/sendmail mta %{_sbindir}/sendmail.opensmtpd 10 \
	--follower %{_bindir}/mailq mta-mailq %{_bindir}/mailq.opensmtpd \
	%if 0%{?_with_pam}
	--follower /etc/pam.d/smtp mta-pam /etc/pam.d/smtp.opensmtpd \
	%endif
	%if 0%{?_with_bdb}
	--follower %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.opensmtpd \
	--follower %{_sbindir}/makemap mta-makemap %{_sbindir}/makemap.opensmtpd \
	--follower %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man8/newaliases.opensmtpd.8.gz \
	--follower %{_mandir}/man8/makemap.8.gz mta-makemapman %{_mandir}/man8/makemap.opensmtpd.8.gz \
	%endif
	--follower /usr/lib/sendmail mta-sendmail %{_sbindir}/sendmail.opensmtpd \
	--follower %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.opensmtpd.1.gz \
	--follower %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.opensmtpd.5.gz \
	--follower %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man8/sendmail.opensmtpd.8.gz \
	--follower %{_mandir}/man8/smtp.8.gz mta-smtpman %{_mandir}/man8/smtp.opensmtpd.8.gz \
	--follower %{_mandir}/man8/smtpd.8.gz mta-smtpdman %{_mandir}/man8/smtpd.opensmtpd.8.gz \
	--initscript opensmtpd

# Make sure that /usr/sbin/sendmail is not missing, if /usr/sbin is a
# directory. The symlink will only be created if there is no symlink
# or file already.
test -h /usr/sbin || ln -s ../bin/sendmail /usr/sbin/sendmail 2>/dev/null || :

exit 0

%preun
%systemd_preun %{name}.service
if [ "$1" = 0 ]; then
    alternatives --remove mta %{_sbindir}/sendmail.opensmtpd
fi
exit 0

%postun
%systemd_postun_with_restart %{name}.service
if [ "$1" -ge "1" ]; then
	mta=`readlink /etc/alternatives/mta`
	if [ "$mta" == "%{_sbindir}/sendmail.opensmtpd" ]; then
	    alternatives --set mta %{_sbindir}/sendmail.opensmtpd
	fi
fi
exit 0

%files
%dir %attr(0711,root,root) %{_localstatedir}/empty/smtpd
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/smtpd.conf
%{_sysconfdir}/%{name}/aliases
%doc CHANGES.md README.md
%license LICENSE
%{_mandir}/man1/lockspool.1.gz
%{_mandir}/man1/mailq.opensmtpd.1.gz
%{_mandir}/man1/smtp.opensmtpd.1.gz
%{_mandir}/man5/aliases.opensmtpd.5.gz
%{_mandir}/man5/forward.5.gz
%{_mandir}/man5/smtpd.conf.5.gz
%{_mandir}/man5/table.5.gz
%{_mandir}/man7/smtpd-filters.7.gz
%{_mandir}/man7/smtpd-tables.7.gz
%{_mandir}/man8/sendmail.opensmtpd.8.gz
%{_mandir}/man8/smtp.opensmtpd.8.gz
%{_mandir}/man8/smtpd.opensmtpd.8.gz
%{_mandir}/man8/smtpctl.8.gz
%{_mandir}/man8/mail.*.8.gz

%dir %attr(0711,root,root) %{_localstatedir}/spool/smtpd
%dir %attr(0700,smtpq,root) %{_localstatedir}/spool/smtpd/incoming
%dir %attr(0770,root,smtpq) %{_localstatedir}/spool/smtpd/offline
%dir %attr(0700,smtpq,root) %{_localstatedir}/spool/smtpd/purge
%dir %attr(0700,smtpq,root) %{_localstatedir}/spool/smtpd/queue

%if 0%{?_with_pam}
%config(noreplace) %{_sysconfdir}/pam.d/smtp.%{name}
%ghost %{_sysconfdir}/pam.d/smtp
%endif

%if 0%{?_with_bdb}
%{_bindir}/newaliases.%{name}
%{_sbindir}/makemap.%{name}
%{_mandir}/man8/newaliases.opensmtpd.8.gz
%{_mandir}/man8/makemap.opensmtpd.8.gz
%ghost %attr(0755,root,root) %{_bindir}/newaliases
%ghost %attr(0755,root,root) %{_sbindir}/makemap
%ghost %{_mandir}/man1/newaliases.1.gz
%ghost %{_mandir}/man8/makemap.8.gz
%endif

%{_unitdir}/%{name}.service
%{_libexecdir}/%{name}
%{_bindir}/smtp
%{_bindir}/mailq.%{name}
%{_sbindir}/sendmail.%{name}
%{_sbindir}/smtpd
%attr(2555,root,smtpq) %{_sbindir}/smtpctl
%ghost %attr(0755,root,root) %{_sbindir}/sendmail
%ghost %attr(0755,root,root) %{_bindir}/mailq
%ghost %attr(0755,root,root) /usr/lib/sendmail
%ghost %{_mandir}/man1/mailq.1.gz
%ghost %{_mandir}/man5/aliases.5.gz
%ghost %{_mandir}/man8/sendmail.8.gz
%ghost %{_mandir}/man8/smtp.8.gz
%ghost %{_mandir}/man8/smtpd.8.gz
%{_sysusersdir}/opensmtpd.conf

%changelog
%autochangelog
