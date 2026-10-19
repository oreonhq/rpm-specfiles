%global source0_hash b9f1c4b36a97cdfefaa53ed1115dd38f4b483037775f6559ee1df14acfd1ce04
%bcond_without perl_Test_More_UTF8_enables_optional_test
Name:           perl-Test-More-UTF8
Version:        0.05
Release:        1%{?dist}
Summary:        Test::More enhanced for UTF-8
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-More-UTF8/
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONS/Test-More-UTF8-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Test_More_UTF8_enables_optional_test}
%endif
Requires:       perl(utf8)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
