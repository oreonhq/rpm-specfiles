%global source0_hash 775586866c5bfbdf9e4592e009fabfc9ebd6f6901f2c2d7bd8a696b21149d21b

Name:           perl-RDF-TrineX-Compatibility-Attean
Version:        0.100
Release:        18%{?dist}
Summary:        Compatibility layer between Attean and RDF::Trine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-TrineX-Compatibility-Attean
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/RDF-TrineX-Compatibility-Attean-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(RDF::Trine::Model)
BuildRequires:  perl(RDF::Trine::Node)
BuildRequires:  perl(RDF::Trine::Node::Blank)
BuildRequires:  perl(RDF::Trine::Node::Literal)
BuildRequires:  perl(RDF::Trine::Node::Resource)
BuildRequires:  perl(Test::More) >= 0.96

# Do not provide private redefinitions
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(RDF::Trine::(Model|Node|Node::Literal|Node::Resource)\\)

%description
This Perl module adds a support for the methods of certain Attean classes to
an RDF::Trine framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RDF-TrineX-Compatibility-Attean-%{version}

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
%doc Changes COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
