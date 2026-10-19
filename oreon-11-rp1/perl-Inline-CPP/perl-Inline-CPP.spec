%global source0_hash 664b220e733c300fb7232738f767ddbfb30332589687eae0f09292a6ba088f06
%bcond_without perl_Inline_CPP_enables_optional_test
Name:           perl-Inline-CPP
Version:        0.80
Release:        21%{?dist}
Summary:        Write Perl subroutines and classes in C++
License:        Artistic-2.0
URL:            https://metacpan.org/release/Inline-CPP
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Inline-CPP-%{version}.tar.gz
Patch0:         Inline-CPP-0.79-Non-interactive-Makefile.PL.patch
Patch1:         Inline-CPP-0.79-Install-into-architecture-specific-path.patch
%global debug_package %{nil}
%if %{with perl_Inline_CPP_enables_optional_test}
%endif
Requires:       gcc-c++(%{__isa})
Requires:       perl-devel(%{__isa})
Requires:       perl(Inline::C) >= 0.80
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Inline::C\\)$
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Inline::Filters)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
