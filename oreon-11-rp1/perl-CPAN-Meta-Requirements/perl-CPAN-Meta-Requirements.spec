# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 1557093e3ff0d650262a8340a1dafc5d033af986f98ee3e8a889d04b53e18019
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Run optional tests
%bcond_without perl_CPAN_Meta_Requirements_enables_optional_test

Name:           perl-CPAN-Meta-Requirements
Version:        2.145
Release:        1%{?dist}
Summary:        Set of version requirements for a CPAN dist
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Meta-Requirements
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Meta-Requirements-2.145.tar.gz

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.88
BuildRequires:  perl(warnings)
# Test
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
# Extra Tests (not run when bootstrapping due to circular build dependencies)
%if !%{defined perl_bootstrap} && ! ( 0%{?rhel} ) && %{with perl_CPAN_Meta_Requirements_enables_optional_test} || 0%{?oreon}
BuildRequires:  findutils
BuildRequires:  glibc-langpack-en
BuildRequires:  perl(blib)
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire)
BuildRequires:  perl(Perl::Critic::Policy::Miscellanea::RequireRcsKeywords)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Pod::Wordlist)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Spelling) >= 0.17, hunspell-en
BuildRequires:  perl(Test::Version) >= 1
%endif
# Dependencies
Requires:       perl(B)
Requires:       perl(version) >= 0.88

# Had a six-digit version in a previous life
%global six_digit_version %(LC_ALL=C; printf '%.6f' '%{version}')

# Provide the six-digit version of the module
%if "%{version}" != "%{six_digit_version}"
Provides:       perl(CPAN::Meta::Requirements) = %{six_digit_version}
%global __provides_exclude ^perl\\(CPAN::Meta::Requirements\\)
%endif

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions. It
can be built up by adding more and more constraints, and it will reduce them
to the simplest representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep
%oreon_verify_sources
%setup -q -n CPAN-Meta-Requirements-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 UNINST=0
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test AUTHOR_TESTING=1
%if !%{defined perl_bootstrap} && ! ( 0%{?rhel} ) && %{with perl_CPAN_Meta_Requirements_enables_optional_test} || 0%{?oreon}
LANG=en_US make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::Requirements.3*
%{_mandir}/man3/CPAN::Meta::Requirements::Range.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.145-1
- Import
