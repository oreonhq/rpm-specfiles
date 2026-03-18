Name:           perl-Test-Pod-Coverage
Version:        1.10
Release:        32%{?dist}
Summary:        Check for pod coverage in your distribution
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Pod-Coverage
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Builder)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Coverage::CountParents)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14

%description
Test::Pod::Coverage is used to create a test for your distribution, to
ensure that all relevant files in your distribution are appropriately
documented in pod.

%prep
%setup -q -n Test-Pod-Coverage-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10-32
- Prepare for Oreon 11 (RP1)
