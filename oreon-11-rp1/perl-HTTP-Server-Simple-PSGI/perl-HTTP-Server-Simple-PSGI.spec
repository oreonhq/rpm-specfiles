%global source0_hash 5f7ccb8453043b97278492a757328116e11e0352f2854a28a9c634e6e9131dba

Name:           perl-HTTP-Server-Simple-PSGI
Version:        0.16
Release:        35%{?dist}
Summary:        PSGI handler for HTTP::Server::Simple
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Server-Simple-PSGI
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/HTTP-Server-Simple-PSGI-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.42
BuildRequires:  perl(Test::More)

%description
HTTP::Server::Simple::PSGI is a HTTP::Server::Simple based HTTP server that
can run PSGI applications. This module only depends on
HTTP::Server::Simple, which itself doesn't depend on any non-core modules
so it's best to be used as an embedded web server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Server-Simple-PSGI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
