%global source0_hash f5d495b1dfb826d5c0c45d03b4d0e6b6047cbb06cdbf6be15fd4dc902aeeb70b
Name:           perl-Class-Container
Version:        0.13
Release:        1%{?dist}
Summary:        Glues object frameworks together transparently
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Container
Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Class-Container-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(B::Deparse)
Requires:       perl(Params::Validate) >= 0.23
Recommends:     perl(Scalar::Util)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Validate\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for "HTML::Mason", in
which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and
several other objects must create each other transparently, passing the
appropriate parameters to the right class, possibly substituting other
subclasses for any of these objects.

The main features of "Class::Container" are:

*   Explicit declaration of containment relationships (aggregation,
    factory creation, etc.)

*   Declaration of constructor parameters accepted by each member in a
    class framework

*   Transparent passing of constructor parameters to the class that
    needs them

*   Ability to create one (automatic) or many (manual) contained objects
    automatically and transparently

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Container-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
