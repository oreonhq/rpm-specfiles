%global source0_hash b7314cb365209d93557b8054e0311ae8c3cb5d1c9d228d1eb3e3fc193a5b77b4

Name:           perl-Template-Timer
Version:        1.00
Release:        45%{?dist}
Summary:        Template::Timer Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Timer
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Template-Timer-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Template::Context)
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14

%description
Template::Timer provides inline timings of the template processing
througout your code.  It's an overridden version of Template::Context that
wraps the process() and include() methods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Timer-%{version}
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
