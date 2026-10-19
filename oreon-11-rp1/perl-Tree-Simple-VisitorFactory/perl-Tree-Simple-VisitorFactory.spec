%global source0_hash 9cf538faa12c54ffb4a91439945e488f1856f62b89ac5072a922119e01880da6
Name:           perl-Tree-Simple-VisitorFactory
Version:        0.16
Release:        14%{?dist}
Summary:        Factory object for dispensing Visitor objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree-Simple-VisitorFactory
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-Simple-VisitorFactory-%{version}.tgz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tree::Simple)
BuildRequires:  perl(Tree::Simple::Visitor)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package contains a collection of Tree::Simple::Visitor::* objects,
and a factory for easily creating instances of them.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tree-Simple-VisitorFactory-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
