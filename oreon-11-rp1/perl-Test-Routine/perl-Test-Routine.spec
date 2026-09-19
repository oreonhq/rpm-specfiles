%global source0_hash 7fd929ed33f254ca099022501926089c7794ef577bba86076e7d9816560f5c07

Name:           perl-Test-Routine
Summary:        Composable units of assertion
Version:        0.031
Release:        9%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Routine
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Routine-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Test::Abortable)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Moose::Meta::Method)
Requires:       perl(Test::More) >= 0.96

%{?perl_default_filter}

%description
Test::Routine is a very simple framework for writing your tests as
composable units of assertion. In other words: roles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Routine-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::Routine*3pm*

%changelog
%autochangelog
