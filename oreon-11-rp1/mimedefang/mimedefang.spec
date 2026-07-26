%global source0_hash b7cc488e4cc376cd57dd0292523284553d023aa9959da3c645784fc069edb51e

Summary:        E-mail filtering framework using Sendmail's Milter interface
Name:           mimedefang
Version:        3.6
Release:        4%{?dist}
# {event{,_tcp}.{c,h},eventpriv.h} are GPL-2.0-or-later, rest is GPL-2.0-only
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://mimedefang.org/
Source0:        https://mimedefang.org/releases/%{name}-%{version}.tar.gz
Source1:        https://mimedefang.org/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/9F9B564003DFF9E4D904301E3B6DDB11E78FEBD2
Source3:        README.FEDORA
Source4:        mimedefang.service
Source5:        mimedefang-multiplexor.service
Source6:        mimedefang-wrapper
Source7:        mimedefang.tmpfilesd
Source8:        mimedefang.sysusersd
Patch0:         https://github.com/The-McGrail-Foundation/MIMEDefang/commit/7379afce07b19c04a1927172ddd2ebb9213d87fa.patch#/mimedefang-3.6-tests.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mail::DKIM)
BuildRequires:  perl(Mail::SPF)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(MIME::Tools) >= 5.410
BuildRequires:  perl(MIME::WordDecoder)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  systemd-rpm-macros
BuildRequires:  %{_sbindir}/sendmail
BuildRequires:  sendmail-milter-devel >= 8.12.0
Recommends:     perl(Mail::SpamAssassin) >= 1.6
Requires(post): perl(Digest::SHA)
%{?systemd_requires}
%{?sysusers_requires_compat}

# Testsuite in %%check
%if 0%{!?_without_tests:1}
BuildRequires:  %{_bindir}/prove
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Mail::DKIM::ARC::Signer) >= 0.44
BuildRequires:  perl(Mail::DKIM::Signer)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Most)
%endif

%description
MIMEDefang is an e-mail filter program which works with Sendmail 8.12
and later, or Postfix. It filters all e-mail messages sent via SMTP.
MIMEDefang splits multi-part MIME messages into their components and
potentially deletes or modifies the various parts. It then reassembles
the parts back into an e-mail message and sends it on its way.

There are some caveats users should be aware of before using MIMEDefang.
MIMEDefang potentially alters e-mail messages. This breaks a "gentleman's
agreement" that mail transfer agents do not modify message bodies. This
could cause problems, for example, with encrypted or signed messages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp -pf %{SOURCE3} .

%build
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export CFLAGS="$CFLAGS -std=gnu17"  # RHBZ#2336394, comment #4
%endif

%configure --with-milterlib=%{_libdir} --with-user=defang --disable-anti-virus
%make_build

%install
%make_install INSTALL_STRIP_FLAG='' install-redhat

# Fix config file, create log directory and remove duplicate
sed -e '1d' -i $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/mail/sa-mimedefang.cf.example

# Install systemd unit files and tmpfiles
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/%{name}-multiplexor.service
install -D -p -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/%{name}-wrapper
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}

# Create a dummy file and install perl script for later executing
touch $RPM_BUILD_ROOT%{_sysconfdir}/mail/mimedefang-ip-key
sed -e '1s@^@#!%{_bindir}/perl\n@' gen-ip-validator.pl > gen-ip-validator.pl.new
install -m 0755 gen-ip-validator.pl.new $RPM_BUILD_ROOT%{_bindir}/gen-ip-validator.pl
touch -c -r gen-ip-validator.pl $RPM_BUILD_ROOT%{_bindir}/gen-ip-validator.pl

# Only for regression tests; depends on Test::Class, Test::Most and Net::SMTP
find $RPM_BUILD_ROOT \( -name Unit.pm -o -name "*::Unit.3" \) -exec rm -f {} \;

%if 0%{!?_without_tests:1}
%check
make test
%endif

%pre
%sysusers_create_compat %{SOURCE8}

%post
%systemd_post %{name}.service
if [ ! -f %{_sysconfdir}/mail/mimedefang-ip-key ]; then
  %{_bindir}/gen-ip-validator.pl > %{_sysconfdir}/mail/mimedefang-ip-key
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md README.{NONROOT,SECURITY,SOPHIE,SPAMASSASSIN,FEDORA}
%doc Changelog contrib/{word-to-html,linuxorg,fang.pl} examples/*filter*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/mail/mimedefang-filter
%ghost %config(noreplace) %{_sysconfdir}/mail/mimedefang-ip-key
%config(noreplace) %{_sysconfdir}/mail/sa-mimedefang.cf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/gen-ip-validator.pl
%{_bindir}/md-mx-ctrl
%{_bindir}/%{name}
%{_bindir}/%{name}.pl
%{_bindir}/%{name}-multiplexor
%{_bindir}/%{name}-release
%{_bindir}/%{name}-util
%{_bindir}/watch-%{name}
%{_bindir}/watch-multiple-%{name}s.tcl
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-multiplexor.service
%{_libexecdir}/%{name}-wrapper
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{perl_vendorlib}/Mail/MIMEDefang.pm
%{perl_vendorlib}/Mail/MIMEDefang/
%{_mandir}/man1/%{name}-util.1*
%{_mandir}/man3/Mail::MIMEDefang*.3*
%{_mandir}/man5/%{name}-filter.5*
%{_mandir}/man7/%{name}-notify.7*
%{_mandir}/man7/%{name}-protocol.7*
%{_mandir}/man8/md-mx-ctrl.8*
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}.pl.8*
%{_mandir}/man8/%{name}-multiplexor.8*
%{_mandir}/man8/%{name}-release.8*
%{_mandir}/man8/watch-%{name}.8*
%{_mandir}/man8/watch-multiple-%{name}s.8*
%dir %attr(0750,defang,defang) %{_localstatedir}/log/%{name}/
%dir %attr(0750,defang,defang) %{_localstatedir}/spool/MIMEDefang/
%dir %attr(0750,defang,defang) %{_localstatedir}/spool/MD-Quarantine/

%changelog
%autochangelog
