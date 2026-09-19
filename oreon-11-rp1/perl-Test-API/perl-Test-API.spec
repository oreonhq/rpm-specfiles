%global source0_hash 7e6034f0eb29314d31d3354828106ace2745f2160cd3c1443a29b68f53ca2313

Name:		perl-Test-API
Version:	0.010
Release:	24%{?dist}
Summary:	Test a list of subroutines provided by a module
License:	Apache-2.0
URL:		https://metacpan.org/release/Test-API
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-API-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::Builder::Module) >= 0.86
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Builder::Tester) >= 1.18
BuildRequires:	perl(Test::More)
# Optional Test Requirements
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120900
# Dependencies
# (none)

%description
This simple test module checks the subroutines provided by a module. This is
useful for confirming a planned API in testing and ensuring that other
functions aren't unintentionally included via import.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-API-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::API.3*

%changelog
%autochangelog
