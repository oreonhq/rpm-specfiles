%global source0_hash dd6877232b834673eb7086233f14320e19d49f4febd6db1d9e3ba860de42b65b

Summary:        SpamAssassin plugin for Spamhaus Data Query Service (DQS)
Name:           spamassassin-dqs
Version:        1.5.1
Release:        6%{?dist}
License:        Apache-2.0
URL:            https://github.com/spamhaus/spamassassin-dqs
Source0:        https://github.com/spamhaus/spamassassin-dqs/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         spamassassin-dqs-1.5.1-loadplugin.patch
%if 0%{?fedora} || 0%{?rhel} >= 10
Requires:       spamassassin >= 4.0.0
%else
Requires:       spamassassin >= 3.4.1, spamassassin < 4.0.0
%endif
Recommends:     bind-utils
BuildRequires:  perl-generators
%if 0%{!?_without_tests:1}
%if 0%{?fedora} || 0%{?rhel} >= 10
BuildRequires:  spamassassin >= 4.0.0
%else
BuildRequires:  spamassassin >= 3.4.1, spamassassin < 4.0.0
%endif
%endif
BuildArch:      noarch

%description
The Spamhaus Data Query Service (DQS) plugin for SpamAssassin enhances
existing functions by checking HELO/EHLO, From, Reply-To, Envelope-From
and Return-Path against Spamhaus DBL/ZRD blacklists. It also scans the
e-mail body for e-mail addresses and performs blacklist lookups against
the domains or its authoritative nameservers. Further checks cover the
reverse DNS matches in DBL/ZRD blacklists or the SBL/CSS lookups for IP
addresses or IP addresses of authoritative nameservers of domains being
part of the e-mail body.

While the DQS usage is free under the same terms like when using public
mirrors (which are shipped in SpamAssassin as default configuration), a
registration procedure for a free DQS key is mandatory nevertheless.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .loadplugin
touch -c -r 4.0.0+/sh.pre{.loadplugin,}
touch -c -r 3.4.1+/sh.pre{.loadplugin,}

%build

%install
%if 0%{?fedora} || 0%{?rhel} >= 10
install -D -p -m 0644 4.0.0+/SH.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/SpamAssassin/Plugin/SH.pm
install -D -p -m 0644 4.0.0+/sh.pre $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sh.pre
install -D -p -m 0644 4.0.0+/sh.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sh.cf
install -D -p -m 0644 4.0.0+/sh_scores.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sh_scores.cf
install -D -p -m 0755 4.0.0+/hbltest.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-hbltest
%else
install -D -p -m 0644 3.4.1+/SH.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/SpamAssassin/Plugin/SH.pm
install -D -p -m 0644 3.4.1+/sh.pre $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sh.pre
install -D -p -m 0644 3.4.1+/sh.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sh.cf
install -D -p -m 0644 3.4.1+/sh_scores.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/sh_scores.cf
install -D -p -m 0755 3.4.1+/hbltest.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-hbltest
%endif

%if 0%{!?_without_tests:1}
%check
mkdir tests
cp -pf {,$RPM_BUILD_ROOT}%{_sysconfdir}/mail/spamassassin/*.{pre,cf} tests/
cp -pf $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/SpamAssassin/Plugin/SH.pm tests/
sed -e 's/^#\(loadplugin Mail::SpamAssassin::Plugin::SH\).*/\1 SH.pm/' -i tests/sh.pre
spamassassin --siteconfigpath=tests --lint > tests/lint.log 2>&1 || { cat tests/lint.log; exit 1; }
grep -q -i fail tests/lint.log && { cat tests/lint.log; exit 1; } || :
%endif

%files
%license LICENSE
%doc Changelog.md NOTICE README.md
%if 0%{?fedora} || 0%{?rhel} >= 10
%doc 4.0.0+/sh_hbl.cf 4.0.0+/sh_hbl_scores.cf
%else
%doc 3.4.1+/sh_hbl.cf 3.4.1+/sh_hbl_scores.cf
%endif
%{_bindir}/%{name}-hbltest
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh.cf
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh_scores.cf
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sh.pre
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/SH.pm

%changelog
%autochangelog
