%global source0_hash 6d45c8778fa9315f1ba21f99ea95ed1f48b66d9616b7ba7810df6af4a27f9b32

Name:           perl-Perl-Critic-Compatibility
Version:        1.001
Release:        42%{?dist}
Summary:        Perl::Critic policies for compatibility with Perl versions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Compatibility
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/Perl-Critic-Compatibility-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
# Perl::Critic 1.083_001 rounded to 3 decimal digits
BuildRequires:  perl(Perl::Critic::Policy) >= 1.084
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Test::More)
# Perl::Critic 1.083_001 rounded to 3 decimal digits
Requires:       perl(Perl::Critic::Policy) >= 1.084

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Perl::Critic::Policy\\)$

%description
Some Perl::Critic policies that will help you keep your code compatible with
other versions of Perl, regardless of the version that you're developing with.
This includes both backward and forward compatibility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Compatibility-%{version}

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
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
