%global source0_hash fe340eba8765f9263694674e5dff14833443e19865e5ff427bbd79b7b5f8a9b8
Name:           perl-Time-Duration
Summary:        Time-Duration - rounded or exact English expression of durations
Version:        1.21
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Url:            https://metacpan.org/release/Time-Duration
Buildarch:      noarch
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Time-Duration-%{version}.tar.gz
Provides:       perl(Time::Duration)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides functions for expressing durations in rounded or exact
terms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Time-Duration-%{version} 

%check

make test
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
