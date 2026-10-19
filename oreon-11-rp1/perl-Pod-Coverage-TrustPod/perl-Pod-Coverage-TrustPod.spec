%global source0_hash 358adc2504f039eb69098aa99bdde6ae9dc935364a8e144f6405e8293b3a7ca3
Name:           perl-Pod-Coverage-TrustPod
Version:        0.100006
Release:        9%{?dist}
Summary:        Allow a module's pod to contain Pod::Coverage hints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Coverage-TrustPod
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Coverage-TrustPod-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Pod::Coverage::TrustPod)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Pod::Coverage::CountParents)
BuildRequires:  perl(Pod::Eventual::Simple)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Coverage-TrustPod-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.100006-9
- Prepare for Oreon 11 (RP1)
