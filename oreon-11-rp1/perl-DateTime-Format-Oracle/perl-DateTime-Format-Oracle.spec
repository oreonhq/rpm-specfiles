%global source0_hash 9f18d1eb3dff38e046ba063d6b54cc7d68464640ce69d7d1578a2ccd285ca8d4
Name:           perl-DateTime-Format-Oracle
Version:        0.06
Release:        1%{?dist}
Summary:        Parse and format Oracle dates and timestamps
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Oracle
Source0:        https://cpan.metacpan.org/authors/id/K/KO/KOLIBRIE/DateTime-Format-Oracle-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::NLS_DATE_FORMAT)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module may be used to convert Oracle date and timestamp values into
DateTime objects. It also can take a DateTime object and produce a date
string matching the NLS_DATE_FORMAT.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-Oracle-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
