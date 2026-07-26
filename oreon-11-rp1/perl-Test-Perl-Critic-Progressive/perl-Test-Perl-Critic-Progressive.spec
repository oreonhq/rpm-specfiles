%global source0_hash 665d717b4a4c35077b703115090aaa64f24ae12c6193674c8a096f031bc15b36

Name:           perl-Test-Perl-Critic-Progressive
Version:        0.03
Release:        45%{?dist}
Summary:        Gradually enforce coding standards
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Perl-Critic-Progressive
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Test-Perl-Critic-Progressive-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Perl::Critic) >= 1.082
BuildRequires:  perl(Perl::Critic::Utils) >= 1.082
BuildRequires:  perl(Test::Builder)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(Perl::Critic) >= 1.082
Requires:       perl(Perl::Critic::Utils) >= 1.082

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic(::Utils)?\\)$

%description
Applying coding standards to large amounts of legacy code is a daunting
task. Often times, legacy code is so non-compliant that it seems downright
impossible. But, if you consistently chip away at the problem, you will
eventually succeed! Test::Perl::Critic::Progressive uses the Perl::Critic
engine to prevent further deterioration of your code and gradually steer it
towards conforming with your chosen coding standards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Perl-Critic-Progressive-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
