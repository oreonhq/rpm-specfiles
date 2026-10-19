%global source102_hash 5a8171c978be046f19c058b30a14715e7ce85a0ff5890c6c1fe55b06d63de721
%global source101_hash 0465aff61b900fc20b99a8b83db8e8801efe2204814c6f6897c94539b6fe67a5
%global source100_hash 0012834eac53e48e79dbb3612e4d2bd7b9a224e1acd9642d236ea7ab02863629
%global source0_hash da8192cf76d8871830d44d7bdc914bd1641105ac813798ddeac5f65ab8f73cee
%global source1_hash f82128687117113dbe40bdc4e3141b87f96c2b01519c9022597da47e726a613e
%global patricia_deps 0
%global razor_deps 0
%define real_name Mail-SpamAssassin
%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}
%global saversion 4.000002
Summary:        Spam filter for email which can be invoked from mail delivery agents
Name: spamassassin
Version: 4.0.2
Release:        3%{?dist}
License: Apache-2.0
URL: https://spamassassin.apache.org/
Source0:        https://www.apache.org/dist/%{name}/source/%{real_name}-%{version}.tar.bz2
Source1:        https://downloads.apache.org/%{name}/source/%{real_name}-rules-%{version}.r1928015.tgz
Source2: redhat_local.cf
Source3: spamassassin-default.rc
Source4: spamassassin-spamc.rc
Source5: spamassassin.sysconfig
Source6: sa-update.logrotate
Source7: sa-update.crontab
Source8: sa-update.cronscript
Source9: sa-update.force-sysconfig
Source10: spamassassin-helper.sh
Source11: spamassassin-official.conf
Source13: README.RHEL.Fedora
Source14: spamassassin.service
Source15: spamassassin.sysconfig.el
Source16: sa-update.service
Source17: sa-update.timer
Source100:        https://www.apache.org/dist/%{name}/source/%{real_name}-%{version}.tar.bz2.asc
Source101:        https://www.apache.org/dist/%{name}/source/%{real_name}-rules-%{version}.r1928015.tgz.asc
Source102: https://www.apache.org/dist/spamassassin/KEYS
Patch0: spamassassin-4.0.0-gnupg2.patch
Patch1: spamassassin-4.0.0-add-logfile-homedir-options.patch
Patch2: spamassassin-4.0.1-remove_dep_to_digest_sha1.patch
Requires(post): diffutils
Requires: perl(HTTP::Date)
Requires: perl(LWP::UserAgent)
Requires: perl(DB_File)
Requires: perl(Mail::SPF)
Requires: perl(Net::CIDR::Lite)
Requires: perl(Encode::Detect)
Requires: perl(BSD::Resource)
Requires: procmail
Requires: gnupg2
Requires: perl-HTML-Parser >= 3.43
Requires: perl(Archive::Tar)
Requires: perl(Net::Patricia)
Requires: perl-Razor-Agent
Requires: perl(IO::Socket::SSL)
Requires: perl(IO::Socket::IP)
Requires: perl(Mail::DKIM)
Requires: perl(Mail::DMARC)
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mail::DKIM)
BuildRequires:  perl(Mail::DMARC)
BuildRequires:  perl(Mail::SPF)
BuildRequires:  perl(Net::CIDR::Lite)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::Patricia)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl-HTML-Parser
BuildRequires:  perl-Razor-Agent
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  re2c
BuildRequires:  systemd-units
# /oreon:deps
%description
SpamAssassin provides you with a way to reduce if not completely eliminate
Unsolicited Commercial Email (SPAM) from your incoming email.  It can
be invoked by a MDA such as sendmail or postfix, or can be called from
a procmail script, .forward file, etc.  It uses a genetic-algorithm
evolved scoring system to identify messages which look spammy, then
adds headers to the message so they can be filtered by the user's mail
reading software.  This distribution includes the spamd/spamc components
which create a server that considerably speeds processing of mail.

To enable spamassassin, if you are receiving mail locally, simply add
this line to your ~/.procmailrc:
INCLUDERC=/etc/mail/spamassassin/spamassassin-default.rc

To filter spam for all users, add that line to /etc/procmailrc
(creating if necessary).

%package compile
Summary: Spamassassin sa-compile
BuildRequires: re2c
Requires: re2c
Requires: perl(XSLoader)
Requires: perl(ExtUtils::MakeMaker)
Requires: %{name} = %{version}-%{release}
%description compile
This subpackage provides the 'sa-compile' tool.
sa-compile uses "re2c" to compile the site-wide parts of the SpamAssassin ruleset.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE102}' --signature='%{SOURCE100}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE102}' --signature='%{SOURCE101}' --data='%{SOURCE1}'
%setup -q -n Mail-SpamAssassin-%{version}
# Patches 0-99 are RH specific
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
# end of patches

echo "RHEL=%{?rhel} FEDORA=%{?fedora}"

%build

export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="%{build_ldflags}"
%{__perl} Makefile.PL DESTDIR=$RPM_BUILD_ROOT/ SYSCONFDIR=%{_sysconfdir} INSTALLDIRS=vendor ENABLE_SSL="yes" < /dev/null
%make_build OPTIMIZE="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%buildroot/%{prefix} \
        INSTALLMAN1DIR=%buildroot/%{_mandir}/man1 \
        INSTALLMAN3DIR=%buildroot/%{_mandir}/man3 \
        LOCAL_RULES_DIR=%{buildroot}/etc/mail/spamassassin
chmod 755 %buildroot/%{_bindir}/* # allow stripping
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/local.cf
install -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/spamassassin
install -m 0644 %{SOURCE3} %buildroot/etc/mail/spamassassin
install -m 0644 %{SOURCE4} %buildroot/etc/mail/spamassassin
install -m 0755 %{SOURCE10} %buildroot/etc/mail/spamassassin
install -m 0644 %{SOURCE6} %buildroot/etc/logrotate.d/sa-update
install -m 0644 %{SOURCE9} %buildroot%{_sysconfdir}/sysconfig/sa-update
install -m 0744 %{SOURCE8} %buildroot%{_datadir}/spamassassin/sa-update.cron
mkdir -p %buildroot%{_unitdir}
install -m 0644 %{SOURCE14} %buildroot%{_unitdir}/spamassassin.service
install -m 0644 %{SOURCE16} %buildroot%{_unitdir}/sa-update.service
install -m 0644 %{SOURCE17} %buildroot%{_unitdir}/sa-update.timer
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
cd $RPM_BUILD_ROOT%{_datadir}/spamassassin/
tar xfvz %{SOURCE1}
sed -i -e 's|\@\@VERSION\@\@|%{saversion}|' *.cf
cd -
find $RPM_BUILD_ROOT/usr -type f -print |
        sed "s@^$RPM_BUILD_ROOT@@g" |
        grep -v perllocal.pod |
        grep -v %{_unitdir} |
        grep -v "\.packlist" > %{name}-%{version}-filelist
if [ "$(cat %{name}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi
find $RPM_BUILD_ROOT%{perl_vendorlib}/* -type d -print |
        sed "s@^$RPM_BUILD_ROOT@%dir @g" >> %{name}-%{version}-filelist
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/spamassassin
mkdir   -m 0700             $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sa-update-keys/
mkdir   -m 0755             $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/channel.d/
install -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/channel.d/
install -m 0644 %{SOURCE13} $RPM_BUILD_DIR/Mail-SpamAssassin-%{version}/
mkdir   -m 0700 -p          $RPM_BUILD_ROOT%{_sharedstatedir}/razor/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post spamassassin.service
%systemd_post sa-update.timer
TMPFILE=$(/bin/mktemp /etc/sysconfig/spamassassin.XXXXXX) || exit 1
cp /etc/sysconfig/spamassassin $TMPFILE
perl -p -i -e 's/(["\s]-\w+)a/$1/ ; s/(["\s]-)a(\w+)/$1$2/ ; s/(["\s])-a\b/$1/' $TMPFILE
perl -p -i -e 's/ --auto-whitelist//' $TMPFILE
cmp /etc/sysconfig/spamassassin $TMPFILE || cp $TMPFILE /etc/sysconfig/spamassassin
rm $TMPFILE
if [ -f /etc/spamassassin.cf ]; then
        %{__mv} /etc/spamassassin.cf /etc/mail/spamassassin/migrated.cf
fi
if [ -f /etc/mail/spamassassin.cf ]; then
        %{__mv} /etc/mail/spamassassin.cf /etc/mail/spamassassin/migrated.cf
fi
%postun

%systemd_postun spamassassin.service
%systemd_postun sa-update.timer
%preun

rm -f %{_sharedstatedir}/razor/*
%systemd_preun spamassassin.service
%systemd_preun sa-update.timer
%files -f %{oreon_filedir}/main.list
%files -n spamassassin-compile -f %{oreon_filedir}/spamassassin-compile.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.2-3
- Prepare for Oreon 11 (RP1)
