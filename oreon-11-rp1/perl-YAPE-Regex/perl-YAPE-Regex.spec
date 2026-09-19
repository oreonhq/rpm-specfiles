%global source0_hash 587bf4d9a3a4e0e91b5dbf0c8ee24e8cf72b6df629e33c5d3e8e1f9e0fe6a7fd

Name:           perl-YAPE-Regex
Version:        4.00
Release:        42%{?dist}
Summary:        Yet Another Parser/Extractor for Regular Expressions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAPE-Regex
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSULLIVAN/YAPE-Regex-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(vars)
# Tests only
# -

%description
This module is yet another parser and tree-builder for Perl regular
expressions. It builds a tree out of a regex, but at the moment, the extent
of the extraction tool for the tree is quite limited. However, the tree can be
useful to extension modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n YAPE-Regex-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
