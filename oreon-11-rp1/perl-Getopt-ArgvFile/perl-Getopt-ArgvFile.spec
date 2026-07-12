%global source0_hash 3709aa513ce6fd71d1a55a02e34d2f090017d5350a9bd447005653c9b0835b22

Name:           perl-Getopt-ArgvFile
Version:        1.11
Release:        47%{?dist}
Summary:        Interpolates script options from files into @ARGV or another array
License:        Artistic-2.0
URL:            https://metacpan.org/release/Getopt-ArgvFile
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSTENZEL/Getopt-ArgvFile-%{version}.tar.gz
Source1:        license.txt
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
# Tests only
BuildRequires:  perl(Test::More) >= 0.11
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

Provides:       perl(Getopt::ArgvFile)
%description
This module simply interpolates option file hints in @ARGV by the contents
of the pointed files. This enables option reading from files instead of or
additional to the usual reading from the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Getopt-ArgvFile-%{version}
cp %{SOURCE1} .
perl -pi -e 's/\r//' Changes

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README demos license.txt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
