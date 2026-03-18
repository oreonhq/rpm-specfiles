Name:		perl-Package-DeprecationManager
Version:	0.18
Release:	8%{?dist}
Summary:	Manage deprecation warnings for your distribution
License:	Artistic-2.0
URL:		https://metacpan.org/release/Package-DeprecationManager
Source0:	https://cpan.metacpan.org/modules/by-module/Package/Package-DeprecationManager-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(List::Util) >= 1.33
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Sub::Util)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warnings)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Runtime

%description
This module allows you to manage a set of deprecations for one or more modules.

When you import Package::DeprecationManager, you must provide a set of
-deprecations as a hash ref. The keys are "feature" names, and the values are
the version when that feature was deprecated.

%prep
%setup -q -n Package-DeprecationManager-%{version}

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorlib}/Package/
%{_mandir}/man3/Package::DeprecationManager.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.18-8
- Prepare for Oreon 11 (RP1)
