%global source0_hash c78111ab857e48c69824903d4b6ce8293feffc6b5d670db550a767f853acc7da

Name:           perl-HTTP-Headers-ActionPack
Version:        0.09
Release:        14%{?dist}
Summary:        A Perl module to handle the inflation and deflation of complex HTTP header types
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            http://search.cpan.org/dist/HTTP-Headers-ActionPack/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/HTTP-Headers-ActionPack-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Test::Fatal) >= 0.0003
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
# Commented out to break the cycle 'perl(Web::Machine) <-> perl(HTTP::Headers::ActionPack)'
# BuildRequires:  perl(Web::Machine)

%description
This is a module to handle the inflation and deflation of complex HTTP
header types. In many cases header values are simple strings, but in
some cases they are complex values with a lot of information encoded in
them. The goal of this module is to make the parsing and analysis of
these headers as easy as calling inflate on a compatible object.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Headers-ActionPack-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md eg
%license LICENSE
%{perl_vendorlib}/HTTP*
%{_mandir}/man3/HTTP*

%changelog
%autochangelog
