%global source0_hash 4b88de549597eecddf7c3c38a4d0204a16f59ad804577b671896ac04e24e040f

Name:		perl-Test-Requires
Summary:	Checks to see if a given module can be loaded
Version:	0.11
Release:	18%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Requires
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Test-Requires-0.11.tar.gz

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Test::More) >= 0.47
# Runtime

%description
Test::Requires checks to see if the module can be loaded.

If this fails, rather than failing tests this skips all tests.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test-Requires-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
# note the "skipped" warnings indicate success :)
make test

%files
%license LICENSE
%doc Changes README.md t/ xt/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Requires.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11-18
- Prepare for Oreon 11 (RP1)
