%global source0_hash 94f41c3924aafde4ef7fa6b58e0595d4038d8ac5ffd62ba111b13c5f4dbc0946

Name:           perl-DateTime-Set
Version:        0.3900
Release:        27%{?dist}
Summary:        Datetime sets and set math
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Set
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/DateTime-Set-%{version}.tar.gz
Patch0:         DateTime-Set-0.32-version.patch
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime) >= 0.12
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Infinite)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Set::Infinite) >= 0.59
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
DateTime::Set is a module for datetime sets. It can be used to handle two
different types of sets. The first is a fixed set of predefined datetime
objects. For example, if we wanted to create a set of datetimes containing
the birthdays of people in our family. The second type of set that it can
handle is one based on the idea of a recurrence, such as "every Wednesday",
or "noon on the 15th day of every month". This type of set can have fixed
starting and ending datetimes, but neither is required. So our "every
Wednesday set" could be "every Wednesday from the beginning of time until
the end of time", or "every Wednesday after 2003-03-05 until the end of
time", or "every Wednesday between 2003-03-05 and 2004-01-07".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Set-%{version}
# Make perl/rpm version comparisons work the same way
%patch -P0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir="%{buildroot}" create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3900-27
- Prepare for Oreon 11 (RP1)
