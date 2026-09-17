%global source0_hash 8032c2baca74bf1fa153cd0c0fac0dac7c11d4e8499332d4ccbec1d6f6729358

%global _hardened_build 1

Summary: The InterNetNews system, an Usenet news server
Name: inn
Version: 2.7.3
Release: 5%{?dist}
# most files are under ISC, except:
# contrib/analyze-traffic.in: public-domain
# contrib/mm_ckpasswd: GPL-2.0-or-later
# contrib/nnrp.access2readers.conf.in: public-domain
# contrib/tunefeed.in: Perl
# control/perl-nocem.in: GPL
# control/pgpverify.in: BSD-4-Clause
# innd/tinyleaf.c: MIT
# innfeed/config_y.[ch]: GPL-3.0-or-later with Bison-exception-2.2 exception
# lib/hashtab.c: public-domain
# lib/md5.c: NTP
# lib/newsuser.c: public-domain
# lib/sd-daemon.c: FSFAP
# lib/vector.c: FSFAP
# include/inn/hashtab.h: public-domain
# include/inn/md5.h: NTP
# include/inn/newsuser.h: public-domain
# include/inn/tst.h: BSD-3-Clause
# include/inn/vector.h: FSFAP
# include/portable/sd-daemon.h: FSFAP
License: ISC AND BSD-3-Clause AND BSD-4-Clause AND FSFAP AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LicenseRef-Fedora-Public-Domain AND MIT AND NTP
URL: https://www.eyrie.org/~eagle/software/inn/
Source0: https://downloads.isc.org/isc/inn/inn-%{version}.tar.gz
Source1: https://downloads.isc.org/isc/inn/inn-%{version}.tar.gz.asc
Source2: inn-default-distributions
# gpg2 --recv-key 0xD73934B49674CF5CCD9AC2787D80315C5736DE75
# gpg2 --export --export-options export-minimal 0xD73934B49674CF5CCD9AC2787D80315C5736DE75
Source3: 0xD73934B49674CF5CCD9AC2787D80315C5736DE75.gpg
Source10: http://www.eyrie.org/~eagle/faqs/inn.html#/inn-faq-%{version}.html
Source20: innd.service
Source21: innd-expire.service
Source22: innd-expire.timer
Source23: innd-nntpsend.service
Source24: innd-nntpsend.timer
Source25: innd-rnews.service
Source26: innd-rnews.timer
Source30: inn.rsyslog
# Fedora-specific paths and configuration settings
Patch0: inn-fedora.patch
BuildRequires: autoconf
BuildRequires: byacc
BuildRequires: cyrus-sasl-devel
BuildRequires: e2fsprogs-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: krb5-devel
BuildRequires: libdb-devel
BuildRequires: libcanlock-devel
BuildRequires: libxcrypt-devel
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl(GD)
BuildRequires: perl(MIME::Parser)
BuildRequires: perl(subs)
BuildRequires: perl(Test::MinimumVersion)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: python3-devel
BuildRequires: sqlite-devel
BuildRequires: systemd-rpm-macros
BuildRequires: wget
BuildRequires: zlib-devel
BuildRequires: %{_bindir}/gpgv2
BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: perl(GD)
Recommends: perl(subs)
Recommends: uucp
%endif
Requires: bash >= 2.0
Requires: coreutils
Requires: grep
Requires: sed
Requires: wget
Requires(post): inews

# XXX white out bogus perl requirement for now
Provides: perl(::usr/lib/innshellvars.pl) = %{version}-%{release}

%description
INN (InterNetNews) is a complete system for serving Usenet news and/or
private newsfeeds. INN includes innd, an NNTP (NetNews Transfer Protocol)
server, and nnrpd, a news server that handles connections from news
readers.

Install the inn package if you need a complete system for posting,
injecting, relaying and serving Usenet news. You may also need to
install inn-devel, if you are going to use a separate program which
interfaces to INN, like newsgate or tin.

%package devel
Summary: The INN (InterNetNews) library
Requires: inn = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}

%description devel
The inn-devel package contains the INN (InterNetNews) library, which
several programs that interface with INN need in order to work (for
example, newsgate and tin).

If you are installing a program which must interface with the INN news
system, you should install inn-devel.

%package -n inews
Summary: Sends Usenet articles to a local news server for distribution

%description -n inews
The inews program is used by some news programs (for example, inn and
trn) to post Usenet news articles to local news servers.  Inews reads
an article from a file or standard input, adds headers, performs some
consistency checks and then sends the article to the local news server
specified in the inn.conf file.

Install inews if you need a program for posting Usenet articles to
local news servers.

%package libs
Summary: Libraries provided by INN

%description libs
This package contains dynamic libraries provided by INN project

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --keyring %{S:3} %{S:1} %{S:0}
%autosetup -p1

# Create a sysusers.d config file
cat >inn.sysusers.conf <<EOF
g news 13
g uucp 14
u news 9 'News server user' /etc/news -
u uucp 10 'Uucp user' /var/spool/uucp -
EOF

%build
%configure \
  --disable-static \
  --enable-largefiles \
  --enable-reduced-depends \
  --enable-shared \
  --enable-uucp-rnews \
  --bindir=%{_libexecdir}/news \
  --exec-prefix=%{_libexecdir}/news \
  --sysconfdir=%{_sysconfdir}/news \
  --with-canlock \
  --with-db-dir=%{_sharedstatedir}/news \
  --with-http-dir=%{_sharedstatedir}/news/http \
  --with-libperl-dir=%{perl_vendorlib} \
  --with-log-dir=/var/log/news \
  --with-openssl \
  --with-perl \
  --with-pic \
  --with-python \
  --with-run-dir=/run/news \
  --with-sasl \
  --with-sendmail=/usr/sbin/sendmail \
  --with-spool-dir=/var/spool/news \
  --with-tmp-dir=%{_sharedstatedir}/news/tmp \
  --with-news-group=news \
  --with-news-master=news \
  --with-news-user=news \

# Don't hardcode rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/news/http
%make_install

# -- Install man pages needed by suck et al.
mkdir -p $RPM_BUILD_ROOT%{_includedir}/inn

for f in system.h libinn.h storage.h options.h dbz.h
do
    install -p -m 0644 ./include/inn/$f $RPM_BUILD_ROOT%{_includedir}/inn
done

touch     $RPM_BUILD_ROOT%{_sharedstatedir}/news/subscriptions
chmod 644 $RPM_BUILD_ROOT%{_sharedstatedir}/news/subscriptions

install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sharedstatedir}/news/distributions

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE20} $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0644 %{SOURCE21} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE22} $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0644 %{SOURCE23} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE24} $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0644 %{SOURCE25} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE26} $RPM_BUILD_ROOT%{_unitdir}

cp -p %{SOURCE10} FAQ.html

touch $RPM_BUILD_ROOT%{_sharedstatedir}/news/history
#LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/bin/makedbz -i \
# -f $RPM_BUILD_ROOT/var/lib/news/history
#chmod 644 $RPM_BUILD_ROOT/var/lib/news/*

cat > $RPM_BUILD_ROOT%{_sysconfdir}/news/.profile <<EOF
PATH=/bin:%{_bindir}:%{_libexecdir}/news
export PATH
EOF

#Fix perms in sample directory to avoid bogus dependencies
find samples -type f | xargs chmod a-x

# we get this from cleanfeed
rm -f $RPM_BUILD_ROOT%{_libexecdir}/news/filter/filter_innd.pl

mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_libexecdir}/news/inews $RPM_BUILD_ROOT%{_bindir}/inews
ln -sf %{_libexecdir}/news/rnews $RPM_BUILD_ROOT%{_bindir}/rnews
# fix debuginfo extraction, permissions are set in files section, anyway
chmod u+w $RPM_BUILD_ROOT%{_libdir}/libinn{,hist,storage}.so.*
pushd $RPM_BUILD_ROOT%{_libexecdir}/news
chmod u+w \
          actsync \
          archive \
          auth/passwd/{auth_krb5,ckpasswd,radius} \
          auth/resolv/{domain,ident} \
          batcher \
          {buff,over}chan \
          buffindexed_d \
          convdate \
          ctlinnd \
          cvtbatch \
          expire{,over} \
          fastrm \
          gencancel \
          getlist \
          {grep,make,prune}history \
          imapfeed \
          inews \
          inn{bind,confval,d,df,feed,xbatch,xmit} \
          makedbz \
          ninpaths \
          nnrpd \
          nntpget \
          ovdb_{init,monitor,server,stat} \
          ovsqlite-server \
          ovsqlite-util \
          rnews{,.libexec/{de,en}code} \
          shlock \
          shrinkfile \
          sm \
          tdx-util \
          tinyleaf \

popd

# Remove unwanted files
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

# Documentation is installed via rpm %%doc directive
rm -rf $RPM_BUILD_ROOT/usr/doc/

# Use tmpfiles.d to create /run/news
install -d $RPM_BUILD_ROOT%{_tmpfilesdir}
cat <<EOF >$RPM_BUILD_ROOT%{_tmpfilesdir}/inn.conf
D /run/news 0755 news news -
EOF
install -d -m 0755 $RPM_BUILD_ROOT/run/news

install -d %{buildroot}%{_presetdir}
cat <<EOF >%{buildroot}%{_presetdir}/80-inn.preset
enable innd-expire.timer
enable innd-nntpsend.timer
enable innd-rnews.timer
EOF

install -dm755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -pm644 %{S:30} %{buildroot}%{_sysconfdir}/rsyslog.d/inn.conf

install -m0644 -D inn.sysusers.conf %{buildroot}%{_sysusersdir}/inn.conf

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make -C tests test

%global inn_units_with_restart innd.service innd-expire.timer innd-nntpsend.timer innd-rnews.timer
%global inn_units innd-expire.service innd-nntpsend.service innd-rnews.service

%post
su -m news -c '/usr/libexec/news/makedbz -i -o'

umask 002
touch /var/log/news/news.notice /var/log/news/news.crit /var/log/news/news.err
chown -R news:news /var/log/news*

%systemd_post %{inn_units_with_restart} %{inn_units}

%ldconfig_scriptlets libs

%preun
%systemd_preun %{inn_units_with_restart} %{inn_units}

if [ $1 = 0 ]; then
    if [ -f /var/lib/news/history.dir ]; then
       rm -f /var/lib/news/history.*
    fi
fi

%postun
%systemd_postun_with_restart %{inn_units}
%systemd_postun %{inn_units}

%files
%license doc/GPL
%license LICENSE
%doc NEWS README* HACKING CONTRIBUTORS INSTALL FAQ.html
%doc doc/config-design doc/history-innfeed doc/sample-control
%doc doc/config-semantics doc/external-auth TODO doc/hook-python doc/config-syntax
%doc doc/hook-perl doc/history
%doc samples
%exclude %{_pkgdocdir}/samples/*.in*
%{_unitdir}/innd.service
%{_unitdir}/innd-expire.service
%{_unitdir}/innd-expire.timer
%{_unitdir}/innd-nntpsend.service
%{_unitdir}/innd-nntpsend.timer
%{_unitdir}/innd-rnews.service
%{_unitdir}/innd-rnews.timer
%{_presetdir}/80-inn.preset
%dir %{_sysconfdir}/rsyslog.d
%{_sysconfdir}/rsyslog.d/inn.conf
%{_mandir}/man1/c*.1.gz
%{_mandir}/man1/f*.1.gz
%{_mandir}/man1/g*.1.gz
%{_mandir}/man1/inn*.1.gz
%{_mandir}/man1/n*.1.gz
%{_mandir}/man1/p*.1.gz
%{_mandir}/man1/r*.1.gz
%{_mandir}/man1/s*.1.gz
%{_mandir}/man3/INN::Config.3pm*
%{_mandir}/man3/INN::Utils::Shlock.3pm*
%{_mandir}/man3/libinn_uwildmat.3*
%{_mandir}/man[58]/*
%defattr(-,news,news,-)
# tmpfile.d files
%{_tmpfilesdir}/inn.conf
%dir /run/news
# /etc/news config files
%dir %{_sysconfdir}/news
%config(noreplace) %{_sysconfdir}/news/send-uucp.cf
%config(noreplace) %{_sysconfdir}/news/actsync.cfg
%config(noreplace) %{_sysconfdir}/news/motd.innd.sample
%config(noreplace) %{_sysconfdir}/news/motd.nnrpd.sample
%config(noreplace) %{_sysconfdir}/news/expire.ctl
%config(noreplace) %{_sysconfdir}/news/actsync.ign
%config(noreplace) %{_sysconfdir}/news/innreport.conf
%config(noreplace) %{_sysconfdir}/news/distrib.pats
%config(noreplace) %{_sysconfdir}/news/buffindexed.conf
%config(noreplace) %{_sysconfdir}/news/innwatch.ctl
%config(noreplace) %{_sysconfdir}/news/nntpsend.ctl
%config(noreplace) %{_sysconfdir}/news/innfeed.conf
%config(noreplace) %{_sysconfdir}/news/nnrpd.track
%config(noreplace) %{_sysconfdir}/news/control.ctl.local
%config(noreplace) %{_sysconfdir}/news/storage.conf
%config(noreplace) %{_sysconfdir}/news/moderators
%config(noreplace) %{_sysconfdir}/news/news2mail.cf
%config(noreplace) %{_sysconfdir}/news/cycbuff.conf
%config(noreplace) %{_sysconfdir}/news/subscriptions
%config(noreplace) %{_sysconfdir}/news/control.ctl
%config(noreplace) %{_sysconfdir}/news/localgroups
%config(noreplace) %{_sysconfdir}/news/.profile
%config(noreplace) %{_sysconfdir}/news/nocem.ctl
%config(noreplace) %{_sysconfdir}/news/incoming.conf
%config(noreplace) %{_sysconfdir}/news/inn-radius.conf
%config(noreplace) %attr(0660,news,news) %{_sysconfdir}/news/inn-secrets.conf
%config(noreplace) %{_sysconfdir}/news/ovdb.conf
%config(noreplace) %{_sysconfdir}/news/ovsqlite.conf
%config(noreplace) %{_sysconfdir}/news/newsfeeds
%config(noreplace) %{_sysconfdir}/news/readers.conf
%config(noreplace) %{_sysconfdir}/news/distributions

%dir %{_sharedstatedir}/news
%config(noreplace) %{_sharedstatedir}/news/active.times
%config(noreplace) %{_sharedstatedir}/news/distributions
%config(noreplace) %{_sharedstatedir}/news/newsgroups
%config(noreplace) %{_sharedstatedir}/news/active
%config(noreplace) %{_sharedstatedir}/news/subscriptions
%config(noreplace) %{_sharedstatedir}/news/history

%config(noreplace) %{_sysconfdir}/news/innshellvars.pl.local
%config(noreplace) %{_sysconfdir}/news/innshellvars.local
%config(noreplace) %{_sysconfdir}/news/innshellvars.tcl.local

%defattr(0755,root,news,0755)
%{_bindir}/rnews
%dir %{_libexecdir}/news
%{_libexecdir}/news/controlbatch
%attr(4510,root,news) %{_libexecdir}/news/innbind
%{_libexecdir}/news/delayer
%{_libexecdir}/news/docheckgroups
%{_libexecdir}/news/imapfeed
%{_libexecdir}/news/actmerge
%{_libexecdir}/news/ovdb_server
%{_libexecdir}/news/ovsqlite-server
%{_libexecdir}/news/ovsqlite-util
%{_libexecdir}/news/gencancel
%{_libexecdir}/news/ninpaths
%{_libexecdir}/news/mod-active
%{_libexecdir}/news/news2mail
%{_libexecdir}/news/innconfval
%{_libexecdir}/news/shlock
%{_libexecdir}/news/nnrpd
%{_libexecdir}/news/controlchan
%{_libexecdir}/news/procbatch
%{_libexecdir}/news/expire
%{_libexecdir}/news/convdate
%{_libexecdir}/news/pullnews
%{_libexecdir}/news/archive
%{_libexecdir}/news/cnfsstat
%{_libexecdir}/news/grephistory
%{_libexecdir}/news/send-ihave
%{_libexecdir}/news/tinyleaf
%{_libexecdir}/news/cvtbatch
%{_libexecdir}/news/expirerm
%{_libexecdir}/news/rc.news
%attr(4550,uucp,news) %{_libexecdir}/news/rnews
%{_libexecdir}/news/innxmit
%{_libexecdir}/news/actsyncd
%{_libexecdir}/news/shrinkfile
%{_libexecdir}/news/makedbz
%{_libexecdir}/news/actsync
%{_libexecdir}/news/pgpverify
%{_libexecdir}/news/inndf
%{_libexecdir}/news/scanlogs
%{_libexecdir}/news/simpleftp
%{_libexecdir}/news/ovdb_init
%{_libexecdir}/news/ctlinnd
%{_libexecdir}/news/innstat
%{_libexecdir}/news/send-uucp
%{_libexecdir}/news/buffchan
%{_libexecdir}/news/perl-nocem
%{_libexecdir}/news/scanspool
%{_libexecdir}/news/expireover
%{_libexecdir}/news/batcher
%{_libexecdir}/news/fastrm
%{_libexecdir}/news/innmail
%{_libexecdir}/news/innxbatch
%{_libexecdir}/news/buffindexed_d
%{_libexecdir}/news/nntpget
%{_libexecdir}/news/cnfsheadconf
%{_libexecdir}/news/ovdb_stat
%{_libexecdir}/news/prunehistory
%{_libexecdir}/news/innreport
%attr(0644,root,news) %{_libexecdir}/news/innreport_inn.pm
%attr(0644,root,news) %{_libexecdir}/news/innreport-display.conf
%{_libexecdir}/news/getlist
%{_libexecdir}/news/innd
%{_libexecdir}/news/innupgrade
%{_libexecdir}/news/news.daily
%{_libexecdir}/news/sm
%{_libexecdir}/news/innwatch
%{_libexecdir}/news/inncheck
%{_libexecdir}/news/writelog
%{_libexecdir}/news/tdx-util
%{_libexecdir}/news/tally.control
%{_libexecdir}/news/overchan
%{_libexecdir}/news/sendinpaths
%{_libexecdir}/news/makehistory
%{_libexecdir}/news/nntpsend
%{_libexecdir}/news/mailpost
%{_libexecdir}/news/innfeed
%{_libexecdir}/news/ovdb_monitor
%{_libexecdir}/news/sendxbatches

%define filterdir %{_libexecdir}/news/filter
%dir %{filterdir}
%{filterdir}/filter_nnrpd.pl
%{filterdir}/nnrpd_access.pl
%{filterdir}/startup_innd.pl
%{filterdir}/nnrpd_auth.py*
%{filterdir}/nnrpd_access.py*
%{filterdir}/nnrpd_auth.pl
%{filterdir}/INN.py*
%{filterdir}/nnrpd.py*
%{filterdir}/filter_innd.py*
%{filterdir}/nnrpd_dynamic.py*

%define authdir %{_libexecdir}/news/auth
%dir %{authdir}

%define passwddir %{authdir}/passwd
%dir %{passwddir}
%{passwddir}/auth_krb5
%{passwddir}/ckpasswd
%{passwddir}/radius

%define resolvdir %{authdir}/resolv
%dir %{resolvdir}
%{resolvdir}/domain
%{resolvdir}/ident

%define controldir %{_libexecdir}/news/control
%dir %{controldir}
%{controldir}/ihave.pl
%{controldir}/sendme.pl
%{controldir}/checkgroups.pl
%{controldir}/newgroup.pl
%{controldir}/rmgroup.pl

%define rnewsdir %{_libexecdir}/news/rnews.libexec
%dir %{rnewsdir}
%{rnewsdir}/encode
%{rnewsdir}/gunbatch
%{rnewsdir}/decode
%{rnewsdir}/bunbatch
%{rnewsdir}/c7unbatch

%{_libexecdir}/news/innshellvars.pl
%{_libexecdir}/news/innshellvars
%{_libexecdir}/news/innshellvars.tcl

%attr(0775,root,news) %dir %{_sharedstatedir}/news/http
%{_sharedstatedir}/news/http/innreport.css

%dir %{perl_vendorlib}/INN
%{perl_vendorlib}/INN/Config.pm
%{perl_vendorlib}/INN/Utils/Shlock.pm
%{perl_vendorlib}/INN/ovsqlite_client.pm

%defattr(-,news,news,-)
%dir /var/spool/news
%dir /var/spool/news/archive
%dir /var/spool/news/articles
%attr(0775,news,news) %dir /var/spool/news/incoming
%attr(0775,news,news) %dir /var/spool/news/incoming/bad
%dir /var/spool/news/innfeed
%dir /var/spool/news/outgoing
%dir /var/spool/news/overview
%dir /var/log/news/OLD
%dir %{_sharedstatedir}/news/tmp

%files libs
%{_libdir}/libinn.so.9{,.*}
%{_libdir}/libinnhist.so.3{,.*}
%{_libdir}/libinnstorage.so.3{,.*}

%files devel
%{_includedir}/inn
%{_libdir}/libinn.so
%{_libdir}/libinnhist.so
%{_libdir}/libinnstorage.so
%{_mandir}/man3/*
%exclude %{_mandir}/man3/INN::Config.3pm*
%exclude %{_mandir}/man3/INN::Utils::Shlock.3pm*
%exclude %{_mandir}/man3/libinn_uwildmat.3*

%files -n inews
%config(noreplace) %attr(-,news,news) %{_sysconfdir}/news/inn.conf
%config(noreplace) %attr(-,news,news) %{_sysconfdir}/news/passwd.nntp
%{_bindir}/inews
%attr(0755,root,root) %{_libexecdir}/news/inews
%{_mandir}/man1/inews*
%{_sysusersdir}/inn.conf

%changelog
%autochangelog
