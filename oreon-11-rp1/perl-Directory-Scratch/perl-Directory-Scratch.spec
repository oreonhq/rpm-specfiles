%global source0_hash b87b6b1bccc60d1b3ce147cd218fe2c600d7119ea4e00da7b099cd4afe32ac01

Name:       perl-Directory-Scratch
Version:    0.18
Release:    31%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Self-cleaning scratch space for tests
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/Directory-Scratch-%{version}.tar.gz
Url:        https://metacpan.org/release/Directory-Scratch
BuildArch:  noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Tiny) >= 0.060
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Random)
# Tests only
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test::More)
Requires:       perl(String::Random)

%description
When writing test suites for modules that operate on files, it's often
inconvenient to correctly create a platform-independent temporary storage
space, manipulate files inside it, then clean it up when the test exits.
The inconvenience usually results in tests that don’t work everywhere, or
worse, no tests at all.

This module aims to eliminate that problem by making it easy to do things
right.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Directory-Scratch-%{version}

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
%doc Changes CONTRIBUTING examples/ README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
