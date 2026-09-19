%global source0_hash 9cf538faa12c54ffb4a91439945e488f1856f62b89ac5072a922119e01880da6

Name:           perl-Tree-Simple-VisitorFactory
Version:        0.16
Release:        14%{?dist}
Summary:        Factory object for dispensing Visitor objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree-Simple-VisitorFactory
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-Simple-VisitorFactory-%{version}.tgz
BuildArch:      noarch

# Core
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tree::Simple) >= 1.12
BuildRequires:  perl(Tree::Simple::Visitor)
# Testing
BuildRequires:  perl(Test::Exception) >= 0.15
BuildRequires:  perl(Test::More)

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

%check
make test

%files
%license LICENSE
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
