%global source0_hash 291b3043fb46d62f5e5dfc180c4221a36edc02cfca2295571f399dda39e26bed

Name:           perl-Tree-XPathEngine
Version:        0.05
Release:        39%{?dist}
Summary:        Re-usable XPath engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree-XPathEngine
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/Tree-XPathEngine-%{version}.tar.gz
# Fix POD syntax, CPAN RT#78638
Patch0:         Tree-XPathEngine-0.05-Fix-POD-syntax.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
This module provides an XPath engine, that can be re-used by other
modules/classes that implement trees.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tree-XPathEngine-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
