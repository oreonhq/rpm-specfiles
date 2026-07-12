%global source0_hash 8d34dbe314cfa2d99bd9aae546bbde94c38bb05b74b07c89bde1673a6f6c55f4

Name:           perl-Data-Perl
Version:        0.002011
Release:        18%{?dist}
Summary:        Base classes wrapping fundamental Perl data types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Perl
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Data-Perl-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(parent)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Output)

# rpm's automatic deptracking misses to add this:
Requires:       perl(Exporter)


Provides:       perl(Data::Perl)
Provides:       perl(Data::Perl::Role::Bool)
Provides:       perl(Data::Perl::Role::Code)
Provides:       perl(Data::Perl::Role::Collection::Array)
Provides:       perl(Data::Perl::Role::Collection::Hash)
Provides:       perl(Data::Perl::Role::Counter)
Provides:       perl(Data::Perl::Role::Number)
Provides:       perl(Data::Perl::Role::String)
%description
Data::Perl is a collection of classes that wrap fundamental data types
that exist in Perl. These classes and methods as they exist today are an
attempt to mirror functionality provided by Moose's Native Traits. One
important thing to note is all classes currently do no validation on
constructor input.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Perl-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README.mkdn
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
