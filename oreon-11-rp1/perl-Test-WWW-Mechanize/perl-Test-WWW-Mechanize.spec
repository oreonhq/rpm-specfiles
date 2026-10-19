%global source0_hash 23fd72e7ed1be79de1d02a2d15f0df093415e0eab6fc615ff6bb688741268677
Name:           perl-Test-WWW-Mechanize
Version:        1.60
Release:        1%{?dist}
Summary:        Testing-specific WWW::Mechanize subclass
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-WWW-Mechanize
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Test-WWW-Mechanize-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(WWW::Mechanize) >= 1.68
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(WWW::Mechanize\\)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert::More)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Lint)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Test::WWW::Mechanize is a subclass of WWW::Mechanize that incorporates
features for web application testing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-WWW-Mechanize-%{version}

# Propagate build-time requirement Carp::Assert::More >= 1.16 to run-time
sed -i -e 's|use Carp::Assert::More|use Carp::Assert::More 1.16|' Mechanize.pm

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
