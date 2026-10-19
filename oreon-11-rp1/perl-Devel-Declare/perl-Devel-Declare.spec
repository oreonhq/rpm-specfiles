%global source0_hash 72f29ca35646a593be98311ffddb72033ae1e8a9d8254c62aa248bd6260e596e
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Devel_Declare_enables_extra_test
Name:           perl-Devel-Declare
Version:        0.006022
Release:        26%{?dist}
Summary:        Adding keywords to perl, in perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Declare
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Declare-%{version}.tar.gz
%if !%{defined perl_bootstrap} && %{with perl_Devel_Declare_enables_extra_test}
%endif
Requires:       perl(B::Hooks::EndOfScope) >= 0.05
%{?perl_default_filter}
Provides:       perl(Devel::Declare)
Provides:       perl(Devel::Declare::MethodInstaller::Simple)
Provides:       perl(Devel::Declare)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(B::Compiling)
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-debugger
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
