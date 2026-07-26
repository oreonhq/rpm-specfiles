%global source0_hash a28ab5151c234df2e0afeb84435b3fe15435410d56372d6839afcd0eb7fbc913

Name:           perl-Tie-Hash-ReadonlyStack
Version:        0.2
Release:        28%{?dist}
Summary:        Treat multiple hashes as a single hash with copy-on-write modifications
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-Hash-ReadonlyStack
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/Tie-Hash-ReadonlyStack-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Perl::Critic not used
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
This Perl module allows you to have your main hash and then assign hashes to
look for the given key in either before or after the main hash. It also allows
you to use hashes that are read-only in said stack and then assign new values
there without modifying the hashes they came from.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Hash-ReadonlyStack-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
