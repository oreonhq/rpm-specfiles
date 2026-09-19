%global source0_hash 664b220e733c300fb7232738f767ddbfb30332589687eae0f09292a6ba088f06

# Perform optional tests
%bcond_without perl_Inline_CPP_enables_optional_test

Name:           perl-Inline-CPP
Version:        0.80
Release:        21%{?dist}
Summary:        Write Perl subroutines and classes in C++
License:        Artistic-2.0
URL:            https://metacpan.org/release/Inline-CPP
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Inline-CPP-%{version}.tar.gz
# Do not ask questions at build time
Patch0:         Inline-CPP-0.79-Non-interactive-Makefile.PL.patch
# Install into archicture specific path because of stored C++ compiler flags,
# CPAN RT#122557
Patch1:         Inline-CPP-0.79-Install-into-architecture-specific-path.patch
# This is a full-arch package because it stores arch-specific C++ options,
# CPAN RT#122557
%global debug_package %{nil}
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.15
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.04
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Perl header files included into generated code
BuildRequires:  perl-devel
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Inline::C) >= 0.80
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Inline) >= 0.82
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.001009
%if %{with perl_Inline_CPP_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Inline::Filters)
%endif
Requires:       gcc-c++(%{__isa})
# Perl header files included into generated code
Requires:       perl-devel(%{__isa})
Requires:       perl(Inline::C) >= 0.80

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Inline::C\\)$

%description
The Inline::CPP Perl module allows you to put C++ source code directly "inline"
in a Perl script or module. You code classes or functions in C++, and you
can use them as if they were written in Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Inline-CPP-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
%autochangelog
