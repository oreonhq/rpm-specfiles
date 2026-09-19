%global source0_hash 92a36754b5118d57ee561e282d113e59fdd1e7437828e20872a1fbfe41d61726

%global cpan_version 2.99042

Name:           perl-Net-Whois-Raw
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        2%{?dist}
Summary:        Get Whois information for domains
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Whois-Raw
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Whois-Raw-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{_bindir}/iconv
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Encode)
# HTTP::Headers not used at tests
# HTTP::Request not used at tests
BuildRequires:  perl(IO::Socket::IP)
# LWP::UserAgent not used at tests
BuildRequires:  perl(Regexp::IPv6)
# URI::URL not used at tests
BuildRequires:  perl(utf8)

# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
Requires:       perl(Data::Dumper)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI::URL)

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

%check
%{make_build} test

%files
%license LICENSE COPYRIGHT
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n pwhois
Summary:        Perl written whois client
# Getopt::Long not used at tests
# Net::IDN::Punycode 1 not used at tests
# Win32API::Registry not used on Linux
Requires:       perl(Getopt::Long) >= 2
Requires:       perl(Net::IDN::Punycode) >= 1
# Win32API::Registry not used on Linux

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IDN::Punycode\\)$

%description -n pwhois
Command line whois client.  Invoke with a domain name, optionally with a whois
server name.

%files -n pwhois
%license LICENSE COPYRIGHT
%doc README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
