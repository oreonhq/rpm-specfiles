%global source0_hash 64fa5fdb1ae3a823134aaa95aec75354bc17bdd9ca12ba0a7ae34a7e51b3ded2
%bcond_without perl_Term_Size_Any_enabels_optional_test
Name:           perl-Term-Size-Any
Version:        0.002
Release:        46%{?dist}
Summary:        Retrieve terminal size
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Size-Any
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-Any-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Term_Size_Any_enabels_optional_test}
%endif
Requires:       perl(Term::Size::Perl)
%{?perl_default_filter}
Provides:       perl(Term::Size::Any)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Term::Size::Perl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a unified interface to retrieve terminal size. It loads one module
of a list of known alternatives, each implementing some way to get the
desired terminal information. This loaded module will actually do the job
on behalf of Term::Size::Any.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Term-Size-Any-%{version}

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

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.002-46
- Import
