%global source0_hash f95b6e5f8d7feebe116d05bf59a2b7cf1a51ed9d30bca80123430ec4567543bf
%bcond_with     live_test
Name:           perl-Web-Scraper
Version:        0.38
Release:        1%{?dist}
Summary:        Web Scraping Toolkit using HTML and CSS Selectors or XPath expressions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Web-Scraper
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Web-Scraper-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(LWP::UserAgent)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/ps
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Selector::XPath)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::TreeBuilder::LibXML)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(LWP)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::XPathEngine)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
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
install -m 755 -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/scraper ${RPM_BUILD_ROOT}%{_bindir}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

LEAK_TEST=1 %{?with_live_test:LIVE_TEST=1} ./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
