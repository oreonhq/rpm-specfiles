%global source0_hash a5fa93bec2dab76d883da12d4f344b73bf8beb0cc4b66c24376f3e0f387aef07

Name:		perl-Parse-Distname
Version:	0.05
Release:	12%{?dist}
Summary:	Parse a distribution name
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/dist/Parse-Distname
Source0:	https://cpan.metacpan.org/modules/by-module/Parse/Parse-Distname-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(ExtUtils::MakeMaker::CPANfile) >= 0.08
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::UseAllModules) >= 0.17
# Dependencies
# (none)

Provides:       perl(Parse::Distname)
%description
Parse::Distname is yet another distribution name parser. It works almost the
same as CPAN::DistnameInfo, but Parse::Distname takes a different approach. It
tries to extract the version part of a distribution and treat the rest as a
distribution name, contrary to CPAN::DistnameInfo which tries to define a name
part and treat the rest as a version.

Because of this difference, when Parse::Distname parses a weird distribution
name such as "AUTHOR/v1.0.tar.gz", it says the name is empty and the version
is "v1.0", while CPAN::DistnameInfo says the name is "v" and the version is
"1.0". See test files in this distribution if you need more details. As of this
writing, Parse::Distname returns a different result for about 200+
distributions among about 320000 BackPan distributions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Parse-Distname-%{version}

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
%{perl_vendorlib}/Parse/
%{_mandir}/man3/Parse::Distname.3*

%changelog
%autochangelog
