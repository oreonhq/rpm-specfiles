%global source0_hash ec36c5d891f31a90a6b6d6198d983a5974603ad5eb4f9376af807ac37493f9a2

# Run optional test
%bcond_without perl_Function_Parameters_enables_optional_test

Name:           perl-Function-Parameters
%global cpan_version 2.002006
Version:        2.2.6
Release:        2%{?dist}
Summary:        Subroutine definitions with parameter lists
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Function-Parameters
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Function-Parameters-%{cpan_version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Util) >= 0.07
BuildRequires:  perl(integer)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if %{with perl_Function_Parameters_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
%endif
# Dependencies
# perl(Moose::Util::TypeConstraints) only used with Moose

Provides:       perl(Function::Parameters)
%description
This module extends Perl with keywords that let you define functions with
parameter lists. It uses Perl's keyword plugin API, so it works reliably
and doesn't require a source filter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Function-Parameters-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Function/
%{perl_vendorarch}/Function/
%{_mandir}/man3/Function::Parameters.3*
%{_mandir}/man3/Function::Parameters::Info.3*

%changelog
%autochangelog
