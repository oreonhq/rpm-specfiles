%global source0_hash b713694b004362ba799baca9ee96a5d1c45a5e297711e3312f741ef511e2cc83

Name:           perl-Data-Censor
Version:        0.04
Release:        3%{?dist}
Summary:        Censor sensitive stuff in a data structure
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Data-Censor
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Data-Censor-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)

%description
This module provides methods to censor sensitive stuff in a data structure.
These can be configured to omit sensitive values before logging.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Censor-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING= %{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
