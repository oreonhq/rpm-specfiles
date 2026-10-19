%global source0_hash ba237fe792c93e8c13879c58fead45de2d1185e53793b792db1a3c9e77dd7b55
%bcond_with perl_DateTime_enables_optional_test
Name:           perl-DateTime
Epoch:          2
Version:        1.67
Release:        1%{?dist}
Summary:        Date and time object for Perl
License:        Artistic-2.0
URL:            https://metacpan.org/release/DateTime
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz
%if %{with perl_DateTime_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Requires:       perl(XSLoader)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((DateTime::Locale|DateTime::TimeZone)\\)$
Provides:       perl(DateTime)
Provides:       perl(DateTime::Duration)
Provides:       perl(DateTime::Infinite)
Provides:       perl(DateTime::Span)
Provides:       perl(DateTime::SpanSet)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Dist::CheckConflicts)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Specio::Subs)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(integer)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DateTime is a class for the representation of date/time combinations.  It
represents the Gregorian calendar, extended backwards in time before its
creation (in 1582). This is sometimes known as the "proleptic Gregorian
calendar". In this calendar, the first day of the calendar (the epoch), is the
first day of year 1, which corresponds to the date which was (incorrectly)
believed to be the birth of Jesus Christ.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-%{version}

%build

perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
