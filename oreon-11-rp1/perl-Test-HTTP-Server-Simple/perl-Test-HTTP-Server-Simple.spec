%global source0_hash 85c97ebd4deb805291b17277032da48807228f24f89b1ce2fb3c09f7a896bb78

Name:           perl-Test-HTTP-Server-Simple
Version:        0.11
Release:        47%{?dist}
Summary:        Test::More functions for HTTP::Server::Simple
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-HTTP-Server-Simple

Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Test-HTTP-Server-Simple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(NEXT)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Builder)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
BuildRequires:  perl(Test::More)
# for improved tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

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

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
