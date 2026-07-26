%global source0_hash 27740eec1c4ce601bafcebe7d61ec77e83247b0a8ac81bbf12777cafdd1ca35e

Name:           perl-Net-IP-Match-Regexp
Version:        1.01
Release:        41%{?dist}
Summary:        Efficiently match IP addresses against ranges
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IP-Match-Regexp
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-IP-Match-Regexp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(base)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)

%description
This module allows you to check an IP address against one or more IP
ranges. It employs Perl's highly optimized regular expression engine to do
the hard work, so it is very fast. It is optimized for speed by doing the
match against a regexp which implicitly checks the broadest IP ranges
first. An advantage is that the regexp can be computed and stored in
advance (in source code, in a database table, etc) and reused, saving much
time if the IP ranges don't change too often. The match can optionally
report a value (e.g. a network name) instead of just a boolean, which makes
module useful for mapping IP ranges to names or codes or anything else.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IP-Match-Regexp-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc CHANGES README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
