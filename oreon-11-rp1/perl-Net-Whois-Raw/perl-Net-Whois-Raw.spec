%global source0_hash 92a36754b5118d57ee561e282d113e59fdd1e7437828e20872a1fbfe41d61726
%global cpan_version 2.99042
Name:           perl-Net-Whois-Raw
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        1%{?dist}
Summary:        Get Whois information for domains
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Whois-Raw
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Whois-Raw-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI::URL)
# oreon:deps
BuildRequires:  /usr/bin/iconv
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Regexp::IPv6)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Net::Whois::Raw queries WHOIS servers about domains. The module supports
recursive WHOIS queries. Also queries via HTTP is supported for some TLDs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Whois-Raw-%{cpan_version}
perl -pi -e 's/^#!.*perl/#!\/usr\/bin\/perl/' bin/pwhois

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{make_build} test
%package -n pwhois
Summary:        Perl written whois client
Requires:       perl(Getopt::Long) >= 2
Requires:       perl(Net::IDN::Punycode) >= 1
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IDN::Punycode\\)$
%description -n pwhois
Command line whois client.  Invoke with a domain name, optionally with a whois
server name.

%files -f %{oreon_filedir}/main.list
%files -n pwhois -f %{oreon_filedir}/pwhois.list

%changelog

%autochangelog
