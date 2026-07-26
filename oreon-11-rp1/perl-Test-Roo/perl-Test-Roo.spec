%global source0_hash 21129a3cecb507b00948e16cf15fcde5dc4db235aba84afd7f47d22013a9ded6

Name:           perl-Test-Roo
Version:        1.004
Release:        30%{?dist}
Summary:        Composable, reusable tests with roles and Moo
License:        Apache-2.0

URL:            https://metacpan.org/release/Test-Roo/
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Roo-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
# not used - bareword::filehandles
# not used - indirect
# not used - multidimensional
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(strictures)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::More)
# Tests
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigInt)

%description
This module allows you to compose Test::More tests from roles. It is inspired
by the excellent Test::Routine module, but uses Moo instead of Moose. This
gives most of the benefits without the need for Moose as a test dependency.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Test-Roo-%{version}

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
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Test::Roo*.*

%changelog
%autochangelog
