%global source0_hash 32ec8387ca9966bfe24e86f54e247f9a0b7d7799abc000ccfa4f2823afa24441
%bcond author_tests 0
Name:           perl-Finance-Quote
%global cpan_version 1.68
Version:        %(LANG=C printf "%.4f" %(echo %{cpan_version} | tr -d _))
Release:        2%{?dist}
Summary:        A Perl module that retrieves stock and mutual fund quotes
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Finance-Quote
Source0:        https://www.cpan.org/modules/by-module/Finance/Finance-Quote-%{cpan_version}.tar.gz
BuildArch:      noarch
%if %{with author_tests}
%endif
Requires:       perl(LWP::Protocol::https)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Date::Range)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Web::Scraper)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

unset DEBUG
%if %{with author_tests}
make test TEST_AUTHOR=1 AUTHOR_TESTING=1
%else
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
