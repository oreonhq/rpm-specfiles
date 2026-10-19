%global source0_hash 85c97ebd4deb805291b17277032da48807228f24f89b1ce2fb3c09f7a896bb78
Name:           perl-Test-HTTP-Server-Simple
Version:        0.11
Release:        47%{?dist}
Summary:        Test::More functions for HTTP::Server::Simple
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HTTP-Server-Simple
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Test-HTTP-Server-Simple-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(NEXT)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This mixin class provides methods to test an HTTP::Server::Simple-based web
server. Currently, it provides only one such method: started_ok.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-HTTP-Server-Simple-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
