%global source0_hash fa10d21a0037e682601efe66738a758ff7521094aa01229e93c888a679b2c8f6

Name:           perl-REST-Client
Version:        281
Release:        14%{?dist}
Summary:        Simple client for interacting with RESTful http/https resources
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/REST-Client
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKHUETTEL/REST-Client-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
# test requirements
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(Test::More) >= 0.8
Requires:       perl(XML::LibXML)

%description
REST::Client provides a simple way to interact with HTTP RESTful resources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n REST-Client-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
