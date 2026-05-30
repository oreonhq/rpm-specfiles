%global source0_hash afabd686fb83d3ebf49ee453974f9122f3eec9b25ff8d2ddf4f12de92af1e5e2

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_DateTime_enables_optional_test
%else
%bcond_with perl_DateTime_enables_optional_test
%endif

Name:           perl-DateTime
Epoch:          2
Version:        1.66
Release:        5%{?dist}
Summary:        Date and time object for Perl
License:        Artistic-2.0
URL:            https://metacpan.org/release/DateTime
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-%{version}.tar.gz


# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Locale) >= 1.06
BuildRequires:  perl(DateTime::TimeZone) >= 2.44
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(integer)
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::ValidationCompiler) >= 0.26
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio) >= 0.50
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Specio::Subs)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Optional Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(utf8)
%if %{with perl_DateTime_enables_optional_test} && !%{defined perl_bootstrap}
# Optional Tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Warn)
%endif
# Dependencies:
Requires:       perl(XSLoader)

# Avoid provides from DateTime.so
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((DateTime::Locale|DateTime::TimeZone)\\)$

%description
DateTime is a class for the representation of date/time combinations.  It
represents the Gregorian calendar, extended backwards in time before its
creation (in 1582). This is sometimes known as the "proleptic Gregorian
calendar". In this calendar, the first day of the calendar (the epoch), is the
first day of year 1, which corresponds to the date which was (incorrectly)
believed to be the birth of Jesus Christ.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS README.md TODO
%{perl_vendorarch}/auto/DateTime/
%{perl_vendorarch}/DateTime/
%{perl_vendorarch}/DateTime.pm
%{_mandir}/man3/DateTime.3*
%{_mandir}/man3/DateTime::Conflicts.3*
%{_mandir}/man3/DateTime::Duration.3*
%{_mandir}/man3/DateTime::Infinite.3*
%{_mandir}/man3/DateTime::LeapSecond.3*
%{_mandir}/man3/DateTime::Types.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.66-5
- Prepare for Oreon 11 (RP1)
