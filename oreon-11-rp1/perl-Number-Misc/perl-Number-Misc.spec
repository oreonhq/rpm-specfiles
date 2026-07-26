%global source0_hash 77b9b68c600a069cf16f4d8126ecb32151e6bcd34b0edb17b78adee689dc91d8

Name:           perl-Number-Misc
Version:        1.2
Release:        29%{?dist}
Summary:        Handy utilities for numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Number-Misc
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKO/Number-Misc-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test::More)

%description
Number::Misc provides some miscellaneous handy utilities for handling
numbers. These utilities handle processing numbers as strings, determining
basic properties of numbers, or selecting a random number from a range.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Number-Misc-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
