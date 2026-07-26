%global source0_hash b9f1c4b36a97cdfefaa53ed1115dd38f4b483037775f6559ee1df14acfd1ce04

# Perform optinal tests
%bcond_without perl_Test_More_UTF8_enables_optional_test

Name:           perl-Test-More-UTF8
Version:        0.05
Release:        19%{?dist}
Summary:        Test::More enhanced for UTF-8
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-More-UTF8/
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONS/Test-More-UTF8-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.7.3
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IO::Handle)
%if %{with perl_Test_More_UTF8_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(utf8)

%description
This Perl module enhances Test::More so that it can print Unicode strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-More-UTF8-%{version}
%if !%{with perl_Test_More_UTF8_enables_optional_test}
rm t/pod.t t/pod-coverage.t
perl -i -nle 'print $_ unless m{\At/(pod|pod-coverage)\.t\b}' MANIFEST
%endif

%build
unset AUTHOR
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
