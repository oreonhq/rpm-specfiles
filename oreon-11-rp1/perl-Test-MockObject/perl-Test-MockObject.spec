# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2b7f80da87f5a6fe0360d9ee521051053017442c3a26e85db68dfac9f8307623
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-Test-MockObject
Version:        1.20200122
Release:        19%{?dist}
Summary:        Perl extension for emulating troublesome interfaces
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-MockObject
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Test-MockObject-1.20200122.tar.gz

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
# Optional run-time:
BuildRequires:  perl(UNIVERSAL::can) >= 1.20110617
BuildRequires:  perl(UNIVERSAL::isa) >= 1.20110614
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(fields)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(vars)
# Dependencies:
Requires:       perl(Carp)

%description
Test::MockObject is a highly polymorphic testing object, capable of
looking like all sorts of objects.  This makes white-box testing much
easier, as you can concentrate on what the code being tested sends to
and receives from the mocked object, instead of worrying about faking
up your own data.  (Another option is not to test difficult things.
Now you have no excuse.)

%prep
%oreon_verify_sources
%setup -q -n Test-MockObject-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::MockObject.3*
%{_mandir}/man3/Test::MockObject::Extends.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20200122-19
- Prepare for Oreon 11 (RP1)
