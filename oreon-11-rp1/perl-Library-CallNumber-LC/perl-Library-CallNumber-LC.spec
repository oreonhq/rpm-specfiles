%global source0_hash 225ccdf39f5224955786cc9df3971bb15cf15611a460a6a45c85376405a267aa
Name:           perl-Library-CallNumber-LC
Version:        0.23
Release:        1%{?dist}
Summary:        Normalize Library of Congress call numbers for sorting
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) OR LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/Library-CallNumber-LC
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBWELLS/Library-CallNumber-LC-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
