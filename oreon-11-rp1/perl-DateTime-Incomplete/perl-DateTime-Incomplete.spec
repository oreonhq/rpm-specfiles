%global source0_hash b1e852e5cd3f8d5c38aa2e7fa5f8521ba22a52515936eb09597047288272b3ec

Name:           perl-DateTime-Incomplete
Version:        0.08
Release:        30%{?dist}
Summary:        Representing partial dates and times
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
# patch to address https://fedoraproject.org/wiki/Common_Rpmlint_issues#incorrect-fsf-address has been sent upstream at https://rt.cpan.org/Ticket/Display.html?id=97520
URL:            https://metacpan.org/release/DateTime-Incomplete
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Incomplete-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(DateTime::Event::Recurrence)
BuildRequires:  perl(DateTime::Set) >= 0.1401
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(DateTime::Set) >= 0.1401

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DateTime::Set\\)$

%description
DateTime::Incomplete is a class for representing partial dates and times.
These are actually encountered relatively frequently. For example, a birthday
is commonly given as a month and day, without a year.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Incomplete-%{version}
# difficult to cancel out a specific required version in EPEL6
sed -i 's|use DateTime::Set.*;|use DateTime::Set;|' lib/DateTime/Incomplete.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
