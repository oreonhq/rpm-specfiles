%global source0_hash 4bb44697ef82105bd8d6204e550796a1eea89ce7108a98e0b7bf3ae4700d1c34

Name:           perl-Clone-PP
Version:        1.09
Release:        1%{?dist}
Summary:        Recursively copy Perl data-types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Clone-PP
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
# Dependencies

Provides:       perl(Clone::PP)
%description
This module provides a general-purpose clone function to make deep copies
of Perl data structures. It calls itself recursively to copy nested hash,
array, scalar and reference types, including tied variables and objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Clone-PP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Clone/
%{_mandir}/man3/Clone::PP.3*

%changelog
%autochangelog
