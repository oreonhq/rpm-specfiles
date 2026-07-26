%global source0_hash 95aab98d316ce5289e80840301da7dea8f7fffc4931506afaf092aec1c063fe3

Name:           perl-Hardware-Vhdl-Parser
Version:        0.12
Release:        49%{?dist}
Summary:        Complete grammar for parsing VHDL code using perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hardware-Vhdl-Parser
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSLONDON/Hardware-Vhdl-Parser-%{version}.tar.gz
# rt#102452
Patch0:         Hardware-Vhdl-Parser-0.12-unreachable.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only

%description
This module defines the complete grammar needed to parse any VHDL code. By
overloading this grammar, it is possible to easily create perl scripts
which run through VHDL code and perform specific functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hardware-Vhdl-Parser-%{version}
%patch -P0 -p1
find . -type f | xargs perl -pi -e 's|#!\s*/bin/perl|#!%{__perl}|'
# rt#102450
rm -rf Hardware

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
rm -f %{buildroot}%{perl_vendorlib}/Hardware/Vhdl/*.pl
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes readme.txt test1.vhd
%doc parser.pl hierarchy.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
