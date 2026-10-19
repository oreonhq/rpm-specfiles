%global source0_hash 18401fd2aa73f6ef4b85bb8f6f69c48452b554ab8c4397808c178c36c34beca5
Name:           perl-License-Syntax
Version:        0.13
Release:        31%{?dist}
Summary:        Coding and decoding of license strings using SPDX and SUSE syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/License-Syntax
Source0:        https://cpan.metacpan.org/authors/id/J/JN/JNW/License-Syntax-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DBD::SQLite)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
License::Syntax is an object oriented module.  When constructing new
License::Syntax objects, you can provide a mapping table for license
names.  The table is used for recognizing alternate alias names for the
licenses (left hand side) and also defines the canonical short names of
the licenses (right hand side).  The mapping table is consulted twice,
before and after decoding the syntax, thus non-terminal mappings may
actually be followed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n License-Syntax-%{version}
chmod -c a-x license_syntax.pl

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
rm -f %{buildroot}/%{perl_vendorlib}/License/license_syntax.pl
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
