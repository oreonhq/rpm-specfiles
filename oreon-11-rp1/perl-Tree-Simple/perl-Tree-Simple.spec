%global source0_hash b7e9799bd222bb94cff993f7d765980cbea1b6cd2aaa5ecbead635abdf47d29c

Name: 		perl-Tree-Simple
Version: 	1.34
Release: 	15%{?dist}
Summary: 	Tree::Simple Perl module
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Tree-Simple
Source0: 	https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-Simple-%{version}.tgz
BuildArch: 	noarch

BuildRequires:  perl-generators
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(Test::Exception) >= 0.15 
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::Memory::Cycle) >= 1.02
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
A simple tree object.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tree-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Tree
%{_mandir}/man3/*

%changelog
%autochangelog
