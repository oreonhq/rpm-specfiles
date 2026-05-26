Name:           perl-Term-Size-Perl
Version:        0.031
Release:        23%{?dist}
Summary:        Perl extension for retrieving terminal size (Perl version)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Size-Perl
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-Perl-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ae9a6746cb1b305ddc8f8d8ca46878552b9c1123628971e13a275183822f209e
%global source0_file Term-Size-Perl-0.031.tar.gz
# oreon url source checksums end
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(Test::More)

# although the resulting rpm appears to be noarch, the build is arch-dependent
# and produces different code for ppc and x86
%global  debug_package %nil

%description
Yet another implementation of Term::Size. Now in pure Perl, with the
exception of a C probe run on build time.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Term-Size-Perl-0.031.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ae9a6746cb1b305ddc8f8d8ca46878552b9c1123628971e13a275183822f209e" || { echo "oreon: Source0 SHA256 mismatch for Term-Size-Perl-0.031.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Term-Size-Perl-%{version}

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.031-23
- Prepare for Oreon 11 (RP1)
