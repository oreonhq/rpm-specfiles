%global source0_hash 8c48b26a2b16c17626e77839174d6b6f65e74629bad53d274357f6d3996049fe

Name:           perl-Devel-Hexdump
Version:        0.02
Release:        39%{?dist}
Summary:        Print nice hex dump of binary data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Hexdump
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Hexdump-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

%description
This module provides a mechanism to output a nice hex dump of binary data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Hexdump-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
     NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
%autochangelog
