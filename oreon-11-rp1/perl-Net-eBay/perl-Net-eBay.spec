%global source0_hash aa9662a441e2174db77d55491621c4dc3a88fd2a594d4a79d842faee30e332d5

Name:           perl-Net-eBay
Version:        0.66
Release:        2%{?dist}
Summary:        Perl Interface to XML based eBay API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-eBay
Source0:        https://cpan.metacpan.org/authors/id/I/IC/ICHUDOV/Net-eBay-%{version}.tar.gz
# Do no load a private IgorBusinessRules module, CPAN RT#105379
Patch0:         Net-eBay-0.61-Do-use-non-existent-IgorBusinessRules.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Dumper)
BuildRequires:  perl(XML::Simple)
# Run-time:
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime::Precise)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::PrettyPrinter)
BuildRequires:  perl(HTML::TreeBuilder)
# LWP::Protocol::https for HTTPS, not Crypt::SSLeay or Net::SSLeay,
# CPAN RT#105378
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Text::Format)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
# Test::Pod::Coverage 1.04 disabled, CPAN RT#97511
# LWP::Protocol::https for HTTPS, not Crypt::SSLeay or Net::SSLeay,
# CPAN RT#105378
Requires:       perl(LWP::Protocol::https)

%description
This module helps user to easily execute queries against eBay's XML API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-eBay-%{version}
%patch -P0 -p1
# Skip Test::Pod::Coverage tests because they are not useful and fail,
# CPAN RT#97511
rm t/pod-coverage.t
perl -i -ne 'print $_ unless m{^t\/pod-coverage.t$}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README
%{_bindir}/ebay-add-item.pl
%{_bindir}/ebay-get-categories.pl
%{_bindir}/ebay-get-item.pl
%{_bindir}/ebay-official-time.pl
%{_bindir}/ebay-revise-item.pl
%{_bindir}/ebay-search.pl
%{_bindir}/ebay-validate-test-user.pl
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::eBay.3pm*

%changelog
%autochangelog
