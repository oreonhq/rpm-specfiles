%if ! (0%{?rhel}) || 0%{?oreon}
# Run extra test
%bcond_without perl_Test_Fatal_enables_extra_test
# Run optional test
%bcond_without perl_Test_Fatal_enables_optional_test
%else
%bcond_with perl_Test_Fatal_enables_extra_test
%bcond_with perl_Test_Fatal_enables_optional_test
%endif

Summary:	Incredibly simple helpers for testing code with exceptions 
Name:		perl-Test-Fatal
Version:	0.018
Release:	2%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Fatal
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Fatal-0.018.tar.gz
# oreon url source checksums begin
%global source0_sha256 b8d2cccf9ee467271bc478f9cf7eba49545452be9302ae359bc538b8bf687cd6
%global source0_file Test-Fatal-0.018.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.12
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:	perl(strict)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Try::Tiny) >= 0.07
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(overload)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More) >= 0.65
%if %{with perl_Test_Fatal_enables_optional_test}
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
%endif
%if %{with perl_Test_Fatal_enables_extra_test}
# Extra Tests
BuildRequires:	findutils
BuildRequires:	perl(Encode)
BuildRequires:	perl(Test::Pod) >= 1.41
%endif
# Dependencies
Requires:	perl(Test::Builder)

%description
Test::Fatal is an alternative to the popular Test::Exception. It does much
less, but should allow greater flexibility in testing exception-throwing code
with about the same amount of typing.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-Fatal-0.018.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b8d2cccf9ee467271bc478f9cf7eba49545452be9302ae359bc538b8bf687cd6" || { echo "oreon: Source0 SHA256 mismatch for Test-Fatal-0.018.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Test-Fatal-%{version}

# Avoid doc-file dependencies
chmod -c -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_Test_Fatal_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Fatal.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.018-2
- Import
