%global source0_hash 53b880a3aec043e4e370ce12682b4756de45dd742dab57294fe21a15453cefe3

Name:           perl-Array-RefElem
Version:        1.00
Release:        55%{?dist}
Summary:        Set up array elements as aliases
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-RefElem
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/Array-RefElem-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
# Devel::Peek not used

%description
This module gives direct access to some of the internal Perl routines that
let you store things in arrays and hashes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Array-RefElem-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Array*
%{_mandir}/man3/*

%changelog
%autochangelog
