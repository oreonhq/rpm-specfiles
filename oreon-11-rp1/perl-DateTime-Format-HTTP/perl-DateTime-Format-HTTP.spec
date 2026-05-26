# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 4e7e82211f3749a73f6f2556f7048cff0725c7d7e52cb819fd51b1bba9fa0b58
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-DateTime-Format-HTTP
Version:        0.43
Release:        4%{?dist}
Summary:        HTTP protocol date conversion routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-HTTP
Source0:        https://cpan.metacpan.org/authors/id/C/CK/CKRAS/DateTime-Format-HTTP-0.43.tar.gz

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(DateTime) >= 0.17
BuildRequires:  perl(HTTP::Date) => 1.44
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
# Dependencies
Requires:       perl(DateTime) >= 0.17
Requires:       perl(HTTP::Date) >= 1.44

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(HTTP::Date\\)$

%description
This module provides functions that deal with the date formats used by the
HTTP protocol (and then some).

%prep
%oreon_verify_sources
%setup -q -n DateTime-Format-HTTP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CREDITS README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::HTTP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.43-4
- Prepare for Oreon 11 (RP1)
