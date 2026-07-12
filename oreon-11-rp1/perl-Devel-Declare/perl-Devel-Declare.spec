%global source0_hash 72f29ca35646a593be98311ffddb72033ae1e8a9d8254c62aa248bd6260e596e

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Devel_Declare_enables_extra_test
%else
%bcond_with perl_Devel_Declare_enables_extra_test
%endif

Name:           perl-Devel-Declare
Version:        0.006022
Release:        26%{?dist}
Summary:        Adding keywords to perl, in perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Declare
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Declare-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.05
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.19
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Scalar::Util) >= 1.11
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl-debugger
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
# Optional Tests
BuildRequires:  perl(B::Compiling)
%if !%{defined perl_bootstrap} && %{with perl_Devel_Declare_enables_extra_test}
# Break build-cycle: perl-Devel-Declare → perl-Devel-CallParser → perl-Devel-Declare
BuildRequires:  perl(Devel::CallParser)
%endif
BuildRequires:  perl(Filter::Util::Call)
# Dependencies
# Necessary minimum versions not automatically detected
Requires:       perl(B::Hooks::EndOfScope) >= 0.05

# Avoid provides from perl shared objects
%{?perl_default_filter}

Provides:       perl(Devel::Declare)
Provides:       perl(Devel::Declare::MethodInstaller::Simple)
Provides:       perl(Devel::Declare)
%description
Devel::Declare can install subroutines called declarators which locally take
over Perl's parser, allowing the creation of new syntax.

This module is now deprecated: keyword handling has been included in the perl
core since perl 5.14, and better alternatives for Devel::Declare functionality
include Devel::CallParser, Function::Parameters, and Keyword::Simple.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-Declare-%{version}

%build
perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/Devel/
%{_mandir}/man3/Devel::Declare.3*

%changelog
%autochangelog
