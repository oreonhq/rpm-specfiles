%global source0_hash 32ec8387ca9966bfe24e86f54e247f9a0b7d7799abc000ccfa4f2823afa24441

%bcond author_tests 0

Name:           perl-Finance-Quote
%global cpan_version 1.68
# RPM version needs 4 digits after the decimal to preserve upgrade path
Version:        %(LANG=C printf "%.4f" %(echo %{cpan_version} | tr -d _))
Release:        2%{?dist}
Summary:        A Perl module that retrieves stock and mutual fund quotes
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Finance-Quote
Source0:        https://www.cpan.org/modules/by-module/Finance/Finance-Quote-%{cpan_version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(HTTP::CookieJar::LWP) >= 0.014
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent) >= 6.48
BuildRequires:  perl(Module::Load) >= 0.36
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Util)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Web::Scraper)
BuildRequires:  perl(XML::LibXML)
# Test Suite
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Range)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More)
# Author Tests
%if %{with author_tests}
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
# Dependencies
Requires:       perl(LWP::Protocol::https)

%description
This module retrieves stock and mutual fund quotes from various exchanges
using various source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Finance-Quote-%{cpan_version}

# Remove redundant exec permissions
find lib/ -type f -name '*.pm' -exec chmod -c -x {} \;

# Avoid documentation name clash
cp -p README README.dist

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
unset DEBUG
%if %{with author_tests}
make test TEST_AUTHOR=1 AUTHOR_TESTING=1
%else
make test
%endif

%files
%license LICENSE
%doc Change* CONTRIBUTING.md Documentation/* README.dist
%{perl_vendorlib}/Finance/
%{_mandir}/man3/Finance::Quote.3*
%{_mandir}/man3/Finance::Quote::AEX.3*
%{_mandir}/man3/Finance::Quote::AlphaVantage.3*
%{_mandir}/man3/Finance::Quote::ASEGR.3*
%{_mandir}/man3/Finance::Quote::ASX.3*
%{_mandir}/man3/Finance::Quote::BorsaItaliana.3*
%{_mandir}/man3/Finance::Quote::Bourso.3*
%{_mandir}/man3/Finance::Quote::BSEIndia.3*
%{_mandir}/man3/Finance::Quote::BVB.3*
%{_mandir}/man3/Finance::Quote::Comdirect.3*
%{_mandir}/man3/Finance::Quote::Consorsbank.3*
%{_mandir}/man3/Finance::Quote::CSE.3*
%{_mandir}/man3/Finance::Quote::Currencies.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::AlphaVantage.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::CurrencyFreaks.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::ECB.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::FinanceAPI.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::Fixer.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::OpenExchange.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::YahooJSON.3*
%{_mandir}/man3/Finance::Quote::Deka.3*
%{_mandir}/man3/Finance::Quote::FinanceAPI.3*
%{_mandir}/man3/Finance::Quote::Finanzpartner.3*
%{_mandir}/man3/Finance::Quote::Fondsweb.3*
%{_mandir}/man3/Finance::Quote::Fool.3*
%{_mandir}/man3/Finance::Quote::FTfunds.3*
%{_mandir}/man3/Finance::Quote::GoldMoney.3*
%{_mandir}/man3/Finance::Quote::GoogleWeb.3*
%{_mandir}/man3/Finance::Quote::IndiaMutual.3*
%{_mandir}/man3/Finance::Quote::MarketWatch.3*
%{_mandir}/man3/Finance::Quote::MorningstarCH.3*
%{_mandir}/man3/Finance::Quote::MorningstarJP.3*
%{_mandir}/man3/Finance::Quote::MorningstarUK.3*
%{_mandir}/man3/Finance::Quote::NSEIndia.3*
%{_mandir}/man3/Finance::Quote::NZX.3*
%{_mandir}/man3/Finance::Quote::OnVista.3*
%{_mandir}/man3/Finance::Quote::Sinvestor.3*
%{_mandir}/man3/Finance::Quote::SIX.3*
%{_mandir}/man3/Finance::Quote::StockData.3*
%{_mandir}/man3/Finance::Quote::Stooq.3*
%{_mandir}/man3/Finance::Quote::SwissFundData.3*
%{_mandir}/man3/Finance::Quote::TesouroDireto.3*
%{_mandir}/man3/Finance::Quote::TMX.3*
%{_mandir}/man3/Finance::Quote::Tradegate.3*
%{_mandir}/man3/Finance::Quote::TSP.3*
%{_mandir}/man3/Finance::Quote::TreasuryDirect.3*
%{_mandir}/man3/Finance::Quote::TwelveData.3*
%{_mandir}/man3/Finance::Quote::Union.3*
%{_mandir}/man3/Finance::Quote::USBonds.3*
%{_mandir}/man3/Finance::Quote::XETRA.3*
%{_mandir}/man3/Finance::Quote::YahooJSON.3*
%{_mandir}/man3/Finance::Quote::YahooWeb.3*
%{_mandir}/man3/Finance::Quote::ZA.3*

%changelog
%autochangelog
