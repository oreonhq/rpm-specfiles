%global source0_hash 11d1a5417b60c09c78ecb187cea84a95daf5fd47aa44810fa6ceff1879b1ad61

Name:           perl-Perl-Critic-Storable
Version:        0.01
Release:        43%{?dist}
Summary:        Policy for Storable.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Storable
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTD/Perl-Critic-Storable-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Test::More)

%description
An additional Perl::Critic policy for using the Storable module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Storable-%{version}

%build
perl Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
