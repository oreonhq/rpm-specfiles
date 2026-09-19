%global source0_hash f95b6e5f8d7feebe116d05bf59a2b7cf1a51ed9d30bca80123430ec4567543bf

# Supported rpmbuild options:
#
# --with live-test/--without live-test
#   include/exclude LIVE_TEST testsuite
#   Default: --without (Requires networking, doesn't work in mock)
%bcond_with     live_test

Name:           perl-Web-Scraper
Version:        0.38
Release:        34%{?dist}
Summary:        Web Scraping Toolkit using HTML and CSS Selectors or XPath expressions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Web-Scraper
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Web-Scraper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Selector::XPath) >= 0.03
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::TreeBuilder) >= 3.23
BuildRequires:  perl(HTML::TreeBuilder::XPath) >= 0.08
BuildRequires:  perl(HTML::TreeBuilder::LibXML) >= 0.13
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP) >= 5.827
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::XPathEngine) >= 0.08
BuildRequires:  perl(YAML)
BuildRequires:  perl(strict)

# Required by the testsuite
BuildRequires:  /usr/bin/ps

# rpm's deptracker misses these:
Requires:  perl(LWP::UserAgent)

%{?perl_default_filter}

%description
Web::Scraper is a web scraper toolkit, inspired by Ruby's equivalent
Scrapi. It provides a DSL-ish interface for traversing HTML documents and
returning a neatly arranged Perl data structure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Web-Scraper-%{version}

# Package does not depend on ExtUtils::MakeMaker
sed -i '/ExtUtils::MakeMaker/d' META.*

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

# Web-Scraper >= 0.38 misses to install bin/scaper
# Install it manually
install -m 755 -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/scraper ${RPM_BUILD_ROOT}%{_bindir}

%{_fixperms} $RPM_BUILD_ROOT/*

%check
LEAK_TEST=1 %{?with_live_test:LIVE_TEST=1} ./Build test

%files
%doc Changes README
%{_bindir}/scraper
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
