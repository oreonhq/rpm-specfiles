%global source0_hash 96b24d47f02df306bec091ff57acdad183c14edceb2bf2180c25d34a234c4277

Name:           perl-WWW-Pastebin-PastebinCom-Create
Version:        1.003
Release:        34%{?dist}
Summary:        Paste to http://pastebin.com from Perl without API keys
# Build.PL: Artistic-2.0
# lib/WWW/Pastebin/PastebinCom/Create.pm:   Artistic-2.0
# LICENSE:  GPL-1.0-or-later OR Artistic-1.0-Perl
# README:   Artistic-2.0
# WWW-Pastebin-PastebinCom-Create-1.001 changed a licenese declaration in all
# files except of LICENSE file. A clarification requested from the upstream,
# CPAN RT#146431.
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)

URL:            https://metacpan.org/release/WWW-Pastebin-PastebinCom-Create
Source0:        https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/WWW-Pastebin-PastebinCom-Create-%{version}.tar.gz
# Do not use /usr/bin/env in shebangs, not suitable for upstream
Patch0:         WWW-Pastebin-PastebinCom-Create-1.003-Do-not-use-usr-bin-env-in-shell-bangs.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Moo) >= 1.004001
BuildRequires:  perl(overload)
BuildRequires:  perl(WWW::Mechanize) >= 1.73
# Tests:
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
Requires:       perl(Moo) >= 1.004001
Requires:       perl(WWW::Mechanize) >= 1.73

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Moo|WWW::Mechanize)\\)$

%description
This module provides the means to paste on <http://www.pastebin.com> pastebin,
without the need for API keys which limits a number of pastes per day. If you
need pasting more oftern, consider using WWW::Pastebin::PastebinCom::API Perl
module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n WWW-Pastebin-PastebinCom-Create-%{version}
# Disable the 01-paste test as it requires network access which we don't
# have when building in koji
rm t/01-paste.t
perl -i -ne 'print $_ unless m{^t/01-paste\.t\>}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
