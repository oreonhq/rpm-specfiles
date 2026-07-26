%global source0_hash 865e198e98d904be1683ef5a53a4948f02dabdacde59fc554a082ffbcc5baefd

Name:           perl-XML-Bare
Version:        0.53
Release:        44%{?dist}
Summary:        Minimal XML parser implemented via a C state engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Bare
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CODECHILD/XML-Bare-%{version}.tar.gz
Patch0:         perl-XML-Bare-c99.patch
Patch1: perl-XML-Bare-c99-2.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This module is a 'Bare' XML parser. It is implemented in C. The parser
itself is a simple state engine that is less than 500 lines of C. The
parser builds a C struct tree from input text. That C struct tree is
converted to a Perl hash by a Perl function that makes basic calls back to
the C to go through the nodes sequentially.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n XML-Bare-%{version}
chmod 644 Bare.pm

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/XML*
%{_mandir}/man3/XML*

%changelog
%autochangelog
