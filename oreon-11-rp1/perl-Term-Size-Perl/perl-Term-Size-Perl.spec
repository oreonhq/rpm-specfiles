%global source0_hash ae9a6746cb1b305ddc8f8d8ca46878552b9c1123628971e13a275183822f209e
Name:           perl-Term-Size-Perl
Version:        0.031
Release:        1%{?dist}
Summary:        Perl extension for retrieving terminal size (Perl version)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Size-Perl
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-Perl-%{version}.tar.gz
%global  debug_package %nil
Provides:       perl(Term::Size::Perl)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Yet another implementation of Term::Size. Now in pure Perl, with the
exception of a C probe run on build time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Term-Size-Perl-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.031-23
- Prepare for Oreon 11 (RP1)
