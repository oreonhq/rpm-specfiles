%global source0_hash 245579b025b63f577c727743011984723871ca40dc35ecec8ead39ae24a48e12

Name:		perl-URI-cpan
Version:	1.009
Release:	7%{?dist}
Summary:	URLs that refer to things on the CPAN
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/URI-cpan
Source0:	https://cpan.metacpan.org/modules/by-module/URI/URI-cpan-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.78
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(URI::_generic)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(URI)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

%description
This module is for handling URLs that refer to things on the CPAN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-cpan-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/URI/
%{_mandir}/man3/URI::cpan.3*
%{_mandir}/man3/URI::cpan::author.3*
%{_mandir}/man3/URI::cpan::dist.3*
%{_mandir}/man3/URI::cpan::distfile.3*
%{_mandir}/man3/URI::cpan::module.3*
%{_mandir}/man3/URI::cpan::package.3*

%changelog
%autochangelog
