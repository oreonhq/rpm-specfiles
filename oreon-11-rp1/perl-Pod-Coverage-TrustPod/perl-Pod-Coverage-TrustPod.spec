Name:           perl-Pod-Coverage-TrustPod
Version:        0.100006
Release:        9%{?dist}
Summary:        Allow a module's pod to contain Pod::Coverage hints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Coverage-TrustPod
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Coverage-TrustPod-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Pod::Coverage::CountParents)
BuildRequires:  perl(Pod::Eventual::Simple)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Explicit dependencies:

%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

%prep
%setup -q -n Pod-Coverage-TrustPod-%{version}

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
%doc Changes README
%{perl_vendorlib}/Pod/
%{_mandir}/man3/Pod::Coverage::TrustPod.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.100006-9
- Prepare for Oreon 11 (RP1)
