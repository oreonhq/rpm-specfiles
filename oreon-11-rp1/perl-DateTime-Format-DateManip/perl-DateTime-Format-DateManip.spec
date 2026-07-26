%global source0_hash 2077c9a420e3c0659b61298bff4ede1269120cf690bfeb35f49f6e6c6be8ee43

Name:           perl-DateTime-Format-DateManip
Version:        0.04
Release:        49%{?dist}
Summary:        Convert Date::Manip to DateTime and vice versa
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-DateManip
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBENNETT/dt-fmt-datemanip/DateTime-Format-DateManip-%{version}.tar.gz
# Use full time zone name instead of an ambiguous abbreviation, CPAN RT#55771
Patch0:         DateTime-Format-DateManip-01conversion.patch
# Pass test with Date-Manip-6.49, bug #1199969, CPAN RT#102670
Patch1:         DateTime-Format-DateManip-0.04-Set-system-time-zone-in-test.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)

%description
DateTime::Format::DateManip is a class that knows how to convert between
Date::Manip dates and durations and DateTime and DateTime::Duration
objects. Recurrences are note yet supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-DateManip-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
