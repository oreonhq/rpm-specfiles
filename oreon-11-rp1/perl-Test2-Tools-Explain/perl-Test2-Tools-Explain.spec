%global source0_hash e476bd1739e68f418617c308c3c3cf742de6a595c23bbac2c270e14159f73122

Name:		perl-Test2-Tools-Explain
Version:	0.02
Release:	19%{?dist}
Summary:	Explain tools for the Perl Test2 framework
License:	Artistic-2.0
URL:		https://metacpan.org/release/Test2-Tools-Explain
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Test2-Tools-Explain-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(:VERSION) >= 5.8.1
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test2::Bundle::Extended)
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(Data::Dumper)

%description
Test2::Suite dropped the explain() function that had been part of Test::More.
For those who miss it in Test2, you can use Test2::Tools::Explain.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Tools-Explain-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/Test2/
%{_mandir}/man3/Test2::Tools::Explain.3*

%changelog
%autochangelog
