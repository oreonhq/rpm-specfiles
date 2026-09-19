%global source0_hash 1bd43763c6a373183097a30e787f5d6713b0db27511c52d533266b59d2cfa780

Name:           perl-Class-Std-Fast
Version:        0.0.8
Release:        30%{?dist}
Summary:        Faster but less secure replacement for Class::Std
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Std-Fast
Source0:        https://cpan.metacpan.org/authors/id/A/AC/ACID/Class-Std-Fast-v%{version}.tar.gz
# Based on the statement in the README file:
# "This library is free software; you can redistribute it and/or modify
# it under the same terms as Perl itself."
Source1:        http://dev.perl.org/licenses/#/%{name}-Licensing.html

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Std)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(lib)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

Requires:       perl(Class::Std)
Requires:       perl(Data::Dumper)

%description
Class::Std::Fast allows you to use the beautiful API of Class::Std in a faster
way than Class::Std does. You can get the object's identity via scalar-ifying 
our object. Getting the objects identity is still possible via the ident method.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Std-Fast-v%{version}
cp -a %{SOURCE1} Licensing.html

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%license Licensing.html
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
