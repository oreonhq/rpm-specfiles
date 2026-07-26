%global source0_hash e077bb549eac02bd301fc7703009715305f71d6597346f67e316dcd1ae506604

Name:           perl-DateTime-Format-DB2
Version:        0.06
Release:        3%{?dist}
Summary:        Parse and format DB2 dates and times
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-DB2
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JROBINSON/DateTime-Format-DB2-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)

%description
This module understands the formats used by DB2 for its DATE, TIME, and
TIMESTAMP data types. It can be used to parse these formats in order to
create DateTime objects, and it can take a DateTime object and produce a
string representing it in the DB2 format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-DB2-%{version}
chmod -c -x t/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes t/
%{perl_vendorlib}/DateTime*
%{_mandir}/man3/DateTime::Format::DB2*

%changelog
%autochangelog
