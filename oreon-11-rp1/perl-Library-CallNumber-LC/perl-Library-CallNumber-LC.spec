%global source0_hash 225ccdf39f5224955786cc9df3971bb15cf15611a460a6a45c85376405a267aa

Name:           perl-Library-CallNumber-LC
Version:        0.23
Release:        30%{?dist}
Summary:        Normalize Library of Congress call numbers for sorting

# Automatically converted from old format: (GPL+ or Artistic) or BSD - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) OR LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/Library-CallNumber-LC
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBWELLS/Library-CallNumber-LC-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Math::BigInt)
# Tests:
BuildRequires:  perl(Test::More)

%description
This module takes Library of Congress (LC) call numbers and normalizes them so
that they are comparable with each other. This supports sorting and
left-anchored searching, such that searching "A11*" should give you all the A11
call numbers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Library-CallNumber-LC-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Library/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
